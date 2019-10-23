import grpc
from dialog_bot_sdk.bot import DialogBot

from config.config import config
from src.user import User
from src.utils import del_buttons
from static.buttons import check_group, edit_data
from static.phrases import phrases, sequence

users = {}


def on_msg(*params):
    peer = params[0].peer
    id_ = peer.id

    if id_ not in users:
        users[peer.id] = User(peer.id)

    user = users[peer.id]

    if user.lock_msg:
        return

    last_key = user.last_key
    text = params[0].message.textMessage.text

    if peer.type == 1:
        if last_key == "":
            user.last_key = "hello"
            bot.messaging.send_message(peer, phrases["hello"])
        elif "check" in last_key:
            if "to_check" in last_key:
                user.filling_data(last_key[9:], text)
            msg = phrases["check"] + "\n" + user.form()
            group = check_group()
            bot.messaging.send_message(peer, msg, group)
            user.lock_msg = True
        else:
            user.filling_data(last_key, text)
            next_key = sequence[last_key]
            user.last_key = next_key
            next_msg = phrases[next_key]
            if next_key == "check":
                next_msg = phrases[next_key] + "\n" + user.form()
                group = check_group()
                bot.messaging.send_message(peer, next_msg, group)
            elif next_key == "surname":
                bot.messaging.send_message(peer, next_msg.format(text))
            else:
                bot.messaging.send_message(peer, next_msg)


def on_click(*params):
    uid = params[0].uid
    peer = bot.users.get_user_peer_by_id(uid)
    if uid not in users:
        users[uid] = User(uid)
        users[uid].last_key = "hello"
        bot.messaging.send_message(peer, phrases["hello"])
        return
    user = users[uid]

    which_button = params[0].value
    if which_button == "Yes":
        f = open('text.txt', 'w')
        for index in user.org:
            f.write(user.org + '\n')
        bot.messaging.send_message(
            peer,
            "Новые отзывы от {0} получены!\nЕсли хотите сделать это позже, то напишите мне снова."
                .format(user.org))
        user.lock_msg = True
        return
    elif which_button == "No":
        group = edit_data()
        del_buttons(bot, peer)
        bot.messaging.send_message(peer, "Что Вы хотели бы исправить?", group)
        user.lock_msg = True
        return
    elif which_button == "all":
        user.last_key = "second_name"
        del_buttons(bot, peer)
        bot.messaging.send_message(peer, phrases["second_name"])
    else:
        user.last_key = "to_check_" + which_button
        del_buttons(bot, peer)
        bot.messaging.send_message(peer, phrases[which_button])
    user.lock_msg = False


if __name__ == '__main__':
    cfg = config["bot_config"]
    bot = DialogBot.get_secure_bot(
        cfg['endpoint'],
        grpc.ssl_channel_credentials(),
        cfg['token']
    )
    bot.messaging.on_message_async(on_msg, on_click)

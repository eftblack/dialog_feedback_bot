from dialog_bot_sdk import interactive_media


def check_group():
    return [interactive_media.InteractiveMediaGroup(
        [
            interactive_media.InteractiveMedia(
                1,
                interactive_media.InteractiveMediaButton("Yes", "Да"),
                'danger'
            ),
            interactive_media.InteractiveMedia(
                2,
                interactive_media.InteractiveMediaButton("No", "Нет, хочу внести изменения"),
                'danger'
            ),
        ]
    )]


def edit_data():
    return [interactive_media.InteractiveMediaGroup(
        [
            interactive_media.InteractiveMedia(
                11,
                interactive_media.InteractiveMediaButton("second_name", "Имя"),
                'danger'
            ),
            interactive_media.InteractiveMedia(
                12,
                interactive_media.InteractiveMediaButton("second_surname", "Фамилия"),
                'danger'
            ),
            interactive_media.InteractiveMedia(
                13,
                interactive_media.InteractiveMediaButton("org", "Компания"),
                'danger'
            ),
            interactive_media.InteractiveMedia(
                14,
                interactive_media.InteractiveMediaButton("all", "Ввести все данные заново"),
                'danger'
            ),
        ]
    )]


def new_form():
    return [interactive_media.InteractiveMediaGroup(
        [
            interactive_media.InteractiveMedia(
                21,
                interactive_media.InteractiveMediaButton("all", "Заполнить заново"),
                'danger'
            ),
        ]
    )]

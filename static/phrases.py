phrases = {
    "hello":
        """Привет!
 Я –– чат-бот платформы dialog, и я помогу вам собрать отзывы о Вашей компании.
 Пожалуйста, введите Ваше имя.""",
    "surname": "Очень приятно, {0}! Укажите Вашу фамилию.",
    "org": "Введите сокращенное наименование Вашей организации",
    "check": "Данные указаны верно?",
    "second_name": "Введите Ваше имя",
    "second_surname": "Введите Вашу фамилию",
    "text":
        """ Вот отзывы о вашей организации """,
    "subject": " a "
}

sequence = {
    "hello": "surname",
    "second_name": "second_surname",
    "second_surname": "org",
    "surname": "org",
    "org": "check",
    "to_check": "check"
}

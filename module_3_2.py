def send_email (message, recipient, sender = "university.help@gmail.com"):
    sender_ = str (sender)
    recipient_ = str(recipient)
    impossible = ('.ru', '.com', '.net')
    if sender_.endswith(impossible) and recipient_.endswith(impossible) and '@' in sender_ and '@' in recipient_:
        if sender_ == recipient_:
            print('Hельзя отправить письмо самому себе!')
        else:
            if sender_ == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')






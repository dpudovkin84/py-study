username = input('Введите имя пользователя: ' )
password = input('Введите пароль: ' )
password_correct=False
retry=0
while not password_correct and retry<3:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
        password = input('Введите пароль еще раз: ' )
        retry=retry+1
    elif username in password:
        print('Пароль содержит имя пользователя\n')
        password = input('Введите пароль еще раз: ' )
        retry=retry+1
    else:
        print('Пароль для пользователя {} установлен'.format( username ))
        password_correct = True

username = input('Введите имя пользователя: ' )
password = input('Введите пароль: ' )
retry=0
while True:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
    else:
        print('Пароль для пользователя {} установлен'.format( username ))
        break
    retry=retry+1
    if not retry<3:
        print('To much retries')
        break
    password = input('Введите пароль еще раз: ' )

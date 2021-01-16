username = input('Введите имя пользователя: ' )
password = input('Введите пароль: ' )
retry=0
pass_correct=False
while not pass_correct and retry<3:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
    else:
        print('Пароль для пользователя {} установлен'.format( username ))
        pass_correct=True
        continue
    retry=retry+1
    if retry<3:
        print('Retries left:', 3-retry)
    else:
        print('To much retries')
        break
    password = input('Введите пароль еще раз: ' )

idade = int(input('Qual a sua idade? '))

if 0 < idade <= 12:
    print('KID')
elif 13 <= idade <= 18:
    print('Adolescente')
else:
    print('Adulto')
    
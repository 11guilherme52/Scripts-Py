usuario = 'Ana'
senha = 1234

nome = str(input('Usuário: '))
autenticacao = int(input('Senha: '))

if nome != usuario:
    print('Usuario ou Senha incorretos')
elif autenticacao != senha:
    print('Senha incorreta')
else:
    print('ACESSO AUTORIZADO')
    
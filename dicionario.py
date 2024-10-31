pessoas = [
    {
    'nome':'Bruna',
    'idade':'20',
    'cidade':'Londres'
    },
    {
        
    }
]


pessoas[0].update({'idade':18})
pessoas[0].update({'profissao':'biologa'})
del pessoas[0]['cidade']

print(pessoas[0])
lista = [10, 5, 8, 3, 7]
soma = 0

try:
    for n in lista:
        soma += n
    print(soma)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
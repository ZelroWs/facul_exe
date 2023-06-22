import os
from ex4 import maior, menor
nome_arquivo = os.path.basename(__file__)

def media(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma / len(lista)

def ex5():
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(
    f"""                    {nome_arquivo}
    \nA lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T =
[-10,-9,0,1,2,5,-2,-4]. Faça um programa que imprima a menor e a maior temperatura, assim
como a temperatura média, usando funções.\n
    """
    )
    lista = [-10,-9,0,1,2,5,-2,-4]
    print(lista)
    print(f'A menor temperatura da lista é: {int(menor(lista))}')
    print(f'A maior temperatura da lista é: {int(maior(lista))}')
    print(f'A média des temperaturas da lista é: {media(lista)}')
    input()
    resp = 0
    while resp != '1' and resp != '2':
        try:
            os.system('cls')
        except:
            os.system('clear')
        resp = input(f'Digite 1 para executar o código {nome_arquivo} novamente e 2 para retornar ao menu:\n  ')
    if resp == '1':
        return ex5()
    return 
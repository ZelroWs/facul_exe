import os
from ex2 import func_v_p
nome_arquivo = os.path.basename(__file__)

def calcular_viagem(distancia):
    if distancia > 200:
        preco = distancia * 0.45
        return f'o preço da viagem é: {preco:,.2f}'
    preco = distancia * 0.50
    return f'o preço da viagem é: R${preco:,.2f}'

def ex3():
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(
    f"""                    {nome_arquivo}
    \nEscreva um programa que pergunte a distância que um passageiro deseja percorrer em
km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e
R$ 0,45 para viagens para longas.\n
    """
    )
    try:
        res = input('Qual a distância em km será percorrida?\n ')
        res = func_v_p(res)
        res = float(res)
    except:
        input('Digite um número amigo :(\n')
        return ex3()
    print(f'Com a distância {res}, {calcular_viagem(res)}')
    input()
    resp = 0
    while resp != '1' and resp != '2':
        try:
            os.system('cls')
        except:
            os.system('clear')
        resp = input(f'Digite 1 para executar o código {nome_arquivo} novamente e 2 para retornar ao menu:\n  ')
    if resp == '1':
        return ex3()
    return 

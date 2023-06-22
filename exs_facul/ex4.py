import os
nome_arquivo = os.path.basename(__file__)

def maior(lista):
    try:
        maior = float(lista[0])
        for i in range(0, len(lista)):
            maior = float(maior)
            a = float(lista[i])
            if a > maior:
                maior = lista[i]
        return maior 
    except:
        input('Digite apenas números amigo :(\n')
        return ex4()
def menor(lista):
    menor = float(lista[0])
    for i in range(0, len(lista)):
        menor = float(menor)
        if float(lista[i]) < menor:
            menor = lista[i]
    return menor 

def ex4():
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(
    f"""                    {nome_arquivo}
    \nFaça um programa que recebe três números do usuário, e identifica o maior através de
uma função e o menor número através de outra função.\n
    """
    )
    resp = []
    resp.append(input('Digite um número: '))
    for i in range(0, 2):
        try:
            os.system('cls')
        except:
            os.system('clear')
        print(
    f"""                    {nome_arquivo}
    \nFaça um programa que recebe três números do usuário, e identifica o maior através de
uma função e o menor número através de outra função.\n
    """
    )
        resp.append(input('Digite um número: '))
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(resp)
    print(f'O maior número Digitado é {maior(resp)}')  
    print(f'O menor número Digitado é {menor(resp)}')
    input()
    resp = 0
    while resp != '1' and resp != '2':
        try:
            os.system('cls')
        except:
            os.system('clear')
        resp = input(f'Digite 1 para executar o código {nome_arquivo} novamente e 2 para retornar ao menu:\n  ')
    if resp == '1':
        return ex4()
    return 
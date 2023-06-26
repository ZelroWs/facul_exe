#importando a biblioteca os
import os
#var que recebe o nome do arquivo
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
        return ':('
def menor(lista):
    try:
        menor = float(lista[0])
        for i in range(0, len(lista)):
            menor = float(menor)
            if float(lista[i]) < menor:
                menor = lista[i]
        return menor 
    except:
        return ':('
#função main do arquivo ex4
def ex4():
    #limpar a tela no windows e no linux
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
        #limpar a tela no windows e no linux
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
    #limpar a tela no windows e no linux
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(resp)
    if maior(resp) == ':(':
        input('Digite apenas números amigo :(\n')
        return ex4()
    elif menor(resp) == ':(':
        input('Digite apenas números amigo :(\n')
        return ex4()
    print(f'O maior número Digitado é {maior(resp)}')  
    print(f'O menor número Digitado é {menor(resp)}')
    input()
    #retorna ao painel principal em main ou retorna ao código que acabou de executar
    resp = 0
    while resp != '1' and resp != '2':
        #limpar a tela no windows e no linux
        try:
            os.system('cls')
        except:
            os.system('clear')
        resp = input(f'Digite 1 para executar o código {nome_arquivo} novamente e 2 para retornar ao menu:\n  ')
    if resp == '1':
        return ex4()
    return 
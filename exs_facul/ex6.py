#importando a biblioteca os
import os
#var que recebe o nome do arquivo
nome_arquivo = os.path.basename(__file__)


def gerar_lista(lista_1, lista_2):
    lista_3 = []
    for i in range(0, len(lista_1)):
        if lista_1[i] not in lista_3:
            lista_3.append(lista_1[i])
    for i in range(0, len(lista_2)):
        if lista_2[i] not in lista_3:
            lista_3.append(lista_2[i])
    return lista_3





#função main do arquivo ex6
def ex6():
    lista_1 = []
    lista_1_aux = []
    lista_2 = []
    lista_2_aux = []
    lista_3 = []
    lista_aux = []
    resp = 1
    while resp != '':
        #limpar a tela no windows e no linux
        try:
            os.system('cls')
        except:
            os.system('clear')
        print(
    f"""                    {nome_arquivo}
    \nFaça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.\n
    """
    )
        
        print(f'Lista 1: {lista_1}\n')
        print(f'Lista 2: {lista_2}\n')
        print('A condição de parada é um enter vazio!!')
        resp = input('Digite algo para ser inserido na primeira lista: ')
        lista_1.append(resp)
    del lista_1[-1]
    resp = 1
    while resp != '':
        #limpar a tela no windows e no linux
        try:
            os.system('cls')
        except:
            os.system('clear')
        print(
    f"""                    {nome_arquivo}
    \nFaça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.\n
    """
    )
        
        print(f'Lista 1: {lista_1}\n')
        print(f'Lista 2: {lista_2}\n')
        print('A condição de parada é um enter vazio!!')
        resp = input('Digite algo para ser inserido na segunda lista: ')
        lista_2.append(resp)
    del lista_2[-1]
    print(f'Lista 1: {lista_1}\n')
    print(f'Lista 2: {lista_2}\n')
    lista_aux = gerar_lista(lista_1, lista_2)
    for i in range(0, len(lista_1)):
        #limpar a tela no windows e no linux
        try:
            os.system('cls')
        except:
            os.system('clear')
        lista_1_aux.append(lista_1[i])
        print(f'Lista 1: {lista_1_aux}')
    
    for i in range(0, len(lista_2)):
        #limpar a tela no windows e no linux
        try:
            os.system('cls')
        except:
            os.system('clear')
        lista_2_aux.append(lista_2[i])
        print(f'Lista 2: {lista_2_aux}')
       
    
    
    for i in range(0, len(lista_aux)):
        #limpar a tela no windows e no linux
        try:
            os.system('cls')
        except:
            os.system('clear')
        lista_3.append(lista_aux[i])
        print(f'Lista 3: {lista_3}')
    #limpar a tela no windows e no linux
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(f'Lista 1: {lista_1}\n')
    print(f'Lista 2: {lista_2}\n')  
    print('Lista gerada com sucesso!')
    print(lista_3)

    input()
    #retorna ao painel principal em main ou retorna ao código que acabou de executar
    resp = 0
    while resp != '1' and resp != '2':
        try:
            os.system('cls')
        except:
            os.system('clear')
        resp = input(f'Digite 1 para executar o código {nome_arquivo} novamente e 2 para retornar ao menu:\n  ')
    if resp == '1':
        return ex6()
    return 
#importando a biblioteca os
import os
#var que recebe o nome do arquivo
nome_arquivo = os.path.basename(__file__)

#função que recebe os dados
def painel():
    try:    
        dias  = int(input('Digite a quantidade de dias que você trabalhou: '))
        horas  = int(input('Digite a quantidade de horas que você trabalhou: '))
        minutos  = int(input('Digite a quantidade de minutos que você trabalhou: '))
        segundos  = int(input('Digite a quantidade de segundos que você trabalhou: '))
        return calcular(segundos, minutos, horas, dias)
    except:
        input('Você deve digitar apenas números inteiros')
        return painel()
#função que transforma as medidas de tempo em segundos 
def calcular(segundos=0, minutos=0, horas=0, dias=0):
    if dias != 0:
        horas += dias * 24
        return calcular(segundos, minutos, horas)
    elif horas !=0:
        minutos += horas * 60
        return calcular(segundos, minutos)
    elif minutos !=0:
        segundos += minutos * 60
        return calcular(segundos)
    return segundos
#iniciar o código
if __name__ == '__main__':
    print(f'\nVocê trabalhou {painel()} segundos.')
#função main do arquivo ex1
def ex1():
    #limpar a tela no windows e no linux
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(
    f"""                    {nome_arquivo}
    \nEscreva um programa que leia a quantidade de dias, horas, minutos e segundos do
    usuário e calcule o total em segundos.
    """
    )

    print(f'\nVocê trabalhou {painel()} segundos.')
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
        return ex1()
    return 
    

#importando a biblioteca os
import os
#var que recebe o nome do arquivo
nome_arquivo = os.path.basename(__file__)
#função main do projeto que inicia o painel do menu e chama os outros arquivos
def main():
    #importando os arquivos do projeto
    import ex1, ex2, ex3, ex4, ex5, ex6
    #limpar a tela no windows e no linux
    try:
        os.system('cls')
    except:
        os.system('clear')
    #painel
    print(nome_arquivo)
    print(
    """
        Menu dos exercícios
    """
    )
    
    print("""Selecione o número do exercício que deseja resolver:

        1- Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do
        usuário e calcule o total em segundos.

        2- Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
        Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou
        iguais, de 15%.

        3- Escreva um programa que pergunte a distância que um passageiro deseja percorrer em
        km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e
        R$ 0,45 para viagens para longas.

        4- Faça um programa que recebe três números do usuário, e identifica o maior através de
        uma função e o menor número através de outra função.

        5- A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T =
        [-10,-9,0,1,2,5,-2,-4]. Faça um programa que imprima a menor e a maior temperatura, assim
        como a temperatura média, usando funções.

        6 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

    """)
    #input da resposta e chamada de cada exercício
    resp = input()
    if resp == '1':
        ex1.ex1()
    elif resp == '2':
        ex2.ex2()
    elif resp == '3':
        ex3.ex3()
    elif resp == '4':
        ex4.ex4()
    elif resp == '5':
        ex5.ex5()
    elif resp == '6':
        ex6.ex6()
    #sempre retornar ao painel
    return main()
#chamada a função main para iniciar o projeto
main()
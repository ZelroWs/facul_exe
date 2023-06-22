import os
nome_arquivo = os.path.basename(__file__)


def calculo_aumento(sal):
    salario = sal
    salario = float(salario)
    if salario > 1250.00:
        aumento = (salario / 100) * 10
        return f'Com um salário de R${salario:.2f} seu aumento é de R${aumento:.2f}, totalizando: R${(salario + aumento):.2f}'
    aumento = (salario / 100) * 15
    return f'Com um salário de R${salario:.2f} seu aumento é de R${aumento:.2f}, totalizando: R${(salario + aumento):.2f}'

def ex2():
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(
    f"""                    {nome_arquivo}
    \nEscreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou
iguais, de 15%.\n
    """
    )
    salario = (input('Digite seu salário: '))
    salario = func_v_p(salario)
    print(f'\n{calculo_aumento(salario)}')
    input()
    resp = 0
    while resp != '1' and resp != '2':
        try:
            os.system('cls')
        except:
            os.system('clear')
        resp = input(f'Digite 1 para executar o código {nome_arquivo} novamente e 2 para retornar ao menu:\n  ')
    if resp == '1':
        return ex2()
    return 

def func_v_p(numero):
    if ',' in numero:
        numero = numero.replace(',', '.')
        return float(numero)
    return numero
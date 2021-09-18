# calculadora simples

num1 = 0
num2 = 0
resultado = 0
operacao = ''

while True:
    num1 = int(input('Digite o numero 1:'))
    operacao = input('Digite a operação: ')
    num2 = int(input('Digite o numero 2:'))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '/':
        resultado = num1 / num2
    elif operacao == '*':
        resultado = num1 * num2
    else:
        resultado = 'Operação inválida'

    print(str (num1) + ' ' + str(operacao) + ' ' + str(num2) + ' = ' + str(resultado))

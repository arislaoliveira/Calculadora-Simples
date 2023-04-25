print('Hello, World!')

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def exponenciacao(a, b):
    return a ** b

print('Selecione a operação: ')
op = input('[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Exponenciação\n')

num1 = float(input('1º Número: '))
num2 = float(input('2º Número: '))

if op == '1':
    print(num1, '+', num2, '=', adicao(num1, num2))
elif op == '2':
    print(num1, '-', num2, '=', subtracao(num1, num2))
elif op == '3':
    print(num1, '*', num2, '=', multiplicacao(num1, num2))
elif op == '4':
    print(num1, '/', num2, '=', divisao(num1, num2))
elif op == '5':
    print(num1, '^', num2, '=', exponenciacao(num1, num2))
else:
    print('Insira uma opção válida.')
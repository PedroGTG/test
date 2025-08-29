def soma():
    return a / b

def multiplicar():
    return a * b

operador = int(input("escolha: "))
a = int(input("num 1: "))
b = int(input("num 2: "))

if operador == 1:
    print(soma())
elif operador == 2:
    print(multiplicar())
def soma():
    a = int(input())
    b = int(input())
    return a + b

def multiplicar():
    a = int(input())
    b = int(input())
    return a * b

operador = int(input("escolha: "))

if operador == 1:
    print(soma())
elif operador == 2:
    print(multiplicar())
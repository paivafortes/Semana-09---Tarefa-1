#Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os valores lidos:

#Todos os valores são diferentes;

#Existem dois valores iguais e um diferente;

#Todos os valores são iguais.

def verificador (numero1, numero2, numero3):
    if numero1 == numero2 and numero2 == numero3:
        print("Todos os valores são iguais")
    elif numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
        print("Existem dois valores iguais e um diferente")
    else:
        print("Todos os valores são diferentes")

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
resultado=verificador(numero1,numero2,numero3)
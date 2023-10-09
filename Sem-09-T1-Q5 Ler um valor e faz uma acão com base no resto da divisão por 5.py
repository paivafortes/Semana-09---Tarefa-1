# Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco). A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:

# Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
# Se 1 (um), escreva se o valor lido é par ou ímpar;
# Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
# Se 3 (três), escreva a divisão inteira do valor lido por 10;
# Se 4 (quatro), escreva o quadrado do valor lido;

def definir_tarefa(numero, resto_divisao):
    if (resto_divisao == 0):
        return ((9 * numero) + 7)

    elif (resto_divisao == 1):
        if (numero % 2 == 0):
            return 'par'
        else:
            return 'ímpar'

    elif (resto_divisao == 2):
        return ((5 * numero ** 2) - (3 * numero) + 42)

    elif (resto_divisao == 3):
        return (numero // 10)

    elif (resto_divisao == 4):
        return (numero ** 2)

def main():
    numero = input().strip()
    numero = int(numero)

    resto_divisao = numero % 5

    resultado = definir_tarefa(numero, resto_divisao)

    print(resultado)

if __name__ == '__main__':
    main()
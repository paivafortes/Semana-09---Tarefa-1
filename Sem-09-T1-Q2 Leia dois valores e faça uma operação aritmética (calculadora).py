#Escreva um programa que leia dois valores e uma das seguintes operações, codificadas dessa forma, será executada:
#1 – Adição
#2 – Subtração
#3 – Multiplicação
#4 – Divisão
#Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

def calculadora (numero_um, operacao, numero_dois):
    resultado = 0
    if(operacao == 1):
        resultado = numero_um + numero_dois
    elif(operacao == 2):
        resultado = numero_um - numero_dois
    elif(operacao == 3):
        resultado = numero_um * numero_dois
    elif(operacao == 4):
        resultado = numero_um / numero_dois
    else:
        raise ValueError('Entrada de dados incorreta')

    return resultado
def main():
    valor_um = input()
    valor_dois = input()
    operacao = input()

    valor_um = float(valor_um)
    valor_dois = float(valor_dois)
    operacao = int(operacao)

    resultado = calculadora(valor_um, operacao, valor_dois)
    if(resultado.is_integer()):
        resultado = int(resultado)
        print(f'{resultado}')
    else:
        print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()
# Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. 

# O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. 

# Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. 

# Separe esses valores com um hífen.

def e_quadrado(valor_um, valor_dois):
    return valor_um == valor_dois

def calcula_perimetro(valor_um, valor_dois):
    return (valor_um + valor_dois) * 2

def calcula_area(valor_um, valor_dois):
    return valor_um * valor_dois

def main():
    valor_base = input()
    valor_altura = input()

    valor_base = int(valor_base)
    valor_altura = int(valor_altura)

    if(e_quadrado(valor_base, valor_altura)):
        print(f'QUADRADO')

    elif(not e_quadrado(valor_base, valor_altura)):
        perimetro = calcula_perimetro(valor_base, valor_altura)
        area = calcula_area(valor_base, valor_altura)

        print(f'{perimetro} - {area}')
    else:
        raise ValueError('Entradas inválidas')

if __name__ == '__main__':
    main()
num = []

def menu():
    print('Escolhe uma das opções\n\n1-Ordenar numeros\n2-Ordenar nomes\n3-Exit')

while True:
    try:
        print('Insira a quantidade de numeros que deseja inserir')
        quantidade = int(input('R:. '))
        if 0 < quantidade:
            print('Insira os numeros desejados, sabendo que cada vez que meter um valor invalido vai ter que meter todos de novo')
            while True:
                try:
                    num = [int(input(f'Insira o {x+1} numero:'))for x in range(quantidade)]
                    break
                except:
                    print('Valor Invalido!')

            print('Numeros por ordem:\n\n')
            print(f'Ordem que foi inserido ... {num}')
            num.sort()
            print(f'Ordem crescente .......... {num}')
            num.sort(reverse=True)
            print(f'Ordem decrescente ........ {num}')
            break
        else:
            print('Valor muito pequeno, precisa ser pelo menos 1!')

    except:
        print('Valor invalido, por favor insira apenas um numero')

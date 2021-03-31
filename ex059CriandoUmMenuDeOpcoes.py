# =============================== CRIANDO UM MENU DE OPÇÕES ===================================
#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
opção = 0
while opção != 5:
    print("""Escolha uma opção para executar:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] Informe os numeros
    [ 5 ] sair do programa""")
    opção = int(input('Informa sua opção: '))
    if opção == 4:
        n1 = float(input('Informe o primeiro valor: '))
        n2 = float(input('Informe o segundo valor: '))
    elif opção == 1:
        soma = n1 + n2
        print('A soma ente {} + {} é {}' .format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O produto de {} * {} é {}' .format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            print('O maior numero é o primeiro: {}' .format(n1))
        elif n1 < n2:
            print('O maior número é o segundo: {}' .format(n2))
        elif n1 == n2:
            print('Os números o primeiro {} e o segundo {}, são iguais' .format(n1, n2))
    elif 1 > opção > 5:
            print('Opção invalida, tente novamente.')
print('Encerrando...')

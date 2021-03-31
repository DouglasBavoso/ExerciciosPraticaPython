# ========================== ANALISADOR COMPLETO ==================================================
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nome = ' '
idade = 0
totidade = 0
totmulher = 0
for pess in range(1, 5):
    print('----- {}a PESSOA-----'.format(pess))
    nome2 = input('Nome: ').strip()
    idade2 = int(input('Idade: '))
    sexo2 = input('Sexo [M/F]: ').upper()
    totidade += idade2
    if sexo2 == 'F' and idade2 < 20:
        totmulher += 1
    if pess == 1:
        nome = nome2
        idade = idade2
    if sexo2 == 'M' and idade2 > idade:
        nome = nome2
        idade = idade2
média = totidade / pess
print('A média de idade do grupo é de {} anos.'.format(média))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade, nome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))

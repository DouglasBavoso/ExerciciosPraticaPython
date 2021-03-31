# =============================== CLASSIFICANDO ATLETAS ==============================================
#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import  date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento?'))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('classificação:MIRIM')
elif idade <= 14:
    print('classificação:INFATIL')
elif idade <=  19:
    print('classificação:JUNIOR')
elif idade <= 25:
    print('classificação:Sênior')
else:
    print('Master')

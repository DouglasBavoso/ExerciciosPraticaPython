# ================================= JOGO DE ADIVINHAÇÃO ====================================
# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# Peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu

from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 18)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))


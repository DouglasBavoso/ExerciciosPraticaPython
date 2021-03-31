# ================================ ANALISANDO TRIÂNGULOS v2.0 ===========================================
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a == b == c:
    tipo = 'EQUILÁTERO'
elif a == b and a != c or a == c and a != b or b == c and b != a:
    tipo = 'ISÓSCELES'
elif a != b != c:
    tipo = 'ESCALENO'
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo {}'.format(tipo))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')


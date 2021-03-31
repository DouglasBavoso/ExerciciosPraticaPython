# ==================== CONVERSOR DE MOEDAS ========================
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostrar quantos Dólares ela pode comprar
# Considera US$1,00 = R$5,78    ===== CONVERSOR DE MOEDAS ====

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.78
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))


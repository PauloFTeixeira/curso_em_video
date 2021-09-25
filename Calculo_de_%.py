"""
Calculando porcentagem em Python de forma simples

Quanto é 10% de R$238.55
"""
valor = 238.55
txdesconto = 10
desconto = valor*txdesconto/100  
valordesconto = valor - desconto
print(desconto)
print(f'10% de {valor} e {desconto}')
print(f'O valor com desconto é {valordesconto:.2f}')

# :.2f  indica quantas casas decimais devem aparecer


#  Reajuste de salário

salario = float(input('Qual o salario do funcionario: R$'))
aumento = float(input('Qual aumento deseja dar? '))
novo = salario + (salario * aumento / 100)
print(novo)

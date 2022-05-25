#Este programa faz um calculo simples de soma de pares
#e multiplicação dos impares com inteiros

while True:
    try:
        num1 = int(input('Digite um número:'))
        break
    except:
        print('Ocorreu um erro')

while True:
    try:
        num2 = int(input('Digite outro número:'))
        break
    except:
        print('Tente novamente')

while True:
    try:
        num3 = int(input('Digite outro:'))
        break
    except:
        print('Algo de errado não está certo kkkk')

while True:
    try:
        num4 = int(input('Digite outro n:'))
        break
    except:
        print('Tente denovo')

soma = 0
mult = 1
if num1 % 2 == 0:
    soma = soma + num1
else:
    mult = mult * num1

if num2 % 2 == 0:
    soma = soma + num2
else:
    mult = mult * num2

if num3 % 2 == 0:
    soma = soma + num3
else:
    mult = mult * num3
if num4 % 2 == 0:
    soma = soma + num4 
else:
    mult = mult * num4 

print('Soma dos pares:',soma)
print('Mult dos impares:',mult)


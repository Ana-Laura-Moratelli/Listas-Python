#1)Faça um programa que peça dois números inteiros e imprima a soma desses dois números?
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print ('A soma dos valores é: ', soma)

#2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
metros = float(input("Digite o valor em metros para ser convertido em milimetros: "))
conv = metros * 1000
print (f"O valor em milimetros é: {conv:.2f}")

#3)Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))
resdias = dias * 86400
reshoras = horas * 3600
resminutos = minutos * 60
resfinal = resdias + reshoras + resminutos + segundos
print("O total em segundos é:", resfinal)

#4)Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Digite seu salario atual em reais: "))
aumento = int(input("Digite a porcentagem do aumento: "))
aumsal = salario * (aumento/100)
print(f"O valor do aumento é: {aumsal:.2f}")
print(f"O novo salario é: {aumsal + salario:.2f}")

#5)Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
preço = float(input("Digite o preço da mercadoria: "))
desconto = int(input("Digite o percentual de desconto: "))
valordes = preço * (desconto/100)
print ('O valor do desconto é: ', valordes)
valorpagar = preço - valordes
print (f'O preço a pagar com o desconto é: {valorpagar:.2f}')

#6)Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem
distancia = int(input("Qual a distância que você irá percorrer em KM? "))
velocidade = int(input("Qual a velocidade média em KM/H? "))
tempo = distancia/velocidade
print ("O tempo esperado para essa viagem de carro é de: ",tempo, "horas")

#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
temp = int(input("Digite a temperatura em Celsius: "))
conv = 9*temp/5+32
print ("A temperatura convertida em Fahrenheit é:",conv)           

#8) Faça agora o contrário, de Fahrenheit para Celsius. F = 9*C/5 + 32
temp = float(input("Digite a temperatura em Fahrenheit: "))
conv = (temp-32)/1.8
print (f"A temperatura convertida em Celsius é: {conv:.2f}")           

#9)Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado
km = int(input("Qual a quantidade de Km percorridos com o carro alugado? "))
dias = int(input("Qual a quantidade de dias que o carro foi alugado? "))
pagar = (km*0.15)+(dias*60)
print (f"O preço a pagar pelo carro é: {pagar:.2f}")
       
#10) Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro
#calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Quantos anos você já fumou? "))
#Para um fumante perder 1 dia ele precisa fumar 144 cigarros
# 1 ano tem 365 dias
dias = cigarros*(anos*365)
diasperdidos = dias / 144
print (f"Você fumante perderá {diasperdidos:.0f} dias ")

#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a 10 mil
print (len(str(2**10000)))


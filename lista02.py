#1) Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input("Informe o primeiro lado do triângulo: "))
b = int(input("Informe o segundo lado do triângulo: "))
c = int(input("Informe o terceiro lado do triângulo: "))

if (b-c)<a<b+c and (a-c)<b<a+c and(a-b)<c<a+b:
    print("Isso é um triângulo")

    if a == b == c:
        print("Esse triângulo é equilátero")
    elif a != b != c:
        print("Esse triângulo é escaleno")
    else:
        print("Esse triângulo é isósceles")
    
else:
    print("Isso não é um triângulo")

#2)Determine se um ano é bissexto. Verifique no Google como fazer isso...
ano = int(input("Digite o ano: "))
if ano % 4 == 0 and (ano % 100 == 0 and ano % 400 ==0):
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")

#3) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO
peso = int(input("Informe o peso dos peixes: "))
multa = 4 * (peso - 50)
excesso = peso - 50
if peso < 50:
    print("Você está com o peso ideal dos peixes")
else:
    print("Você está com o peso acima do permitido, o valor da multa é:", multa, "e a quantidade de peso que você passou é:", excesso)

#4)Faça um Programa que leia três números e mostre o maior deles
primeiro = int(input("Informe o primeiro número: "))
segundo  = int(input("Informe o segundo número : "))
terceiro = int(input("Informe o terceiro número: "))

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print("O maior número é o: ",maior)

#5) Faça um Programa que leia três números e mostre o maior e o menor deles.
primeiro = int(input("Informe o primeiro número : "))
segundo  = int(input("Informe o segundo número : "))
terceiro = int(input("Informe o terceiro número : "))

maior = primeiro
menor = primeiro
if (segundo > maior):
    maior = segundo

if (segundo < menor):
    menor = segundo
    
if (terceiro > maior):
    maior = terceiro

if (terceiro < menor):
    menor = terceiro

print("O maior número é o:",maior, "e o menor número é o:",menor)

#6)Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

salario = float(input("Qual você ganha por hora? "))
horas = int(input("Quantas horas trabalhadas no mês? "))
salariobruto = salario * horas
print (f"O seu salário bruto é: {salariobruto:.2f}")
ir = salariobruto * (11/100)
print (f"Você pagou {ir:.2f} de imposto de renda")
inss = salariobruto * (8/100)
print (f"Você pagou {inss:.2f} de INSS")
sindicato = salariobruto * (5/100)
print (f"Você pagou {sindicato:.2f} de sindicato")
salarioliquido = salariobruto - ir - inss - sindicato
print (f"Seu salário líquido é {salarioliquido:.2f}")

#7)Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

tamanho = int(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
litros = tamanho / 3

if tamanho % 54 == 0:
	latas = tamanho / 54
else: 
	latas = int(tamanho / 54) + 1

preco = latas * 80
print ("Serão utulizadas %d latas" %latas)
print ("O valor total é R$ %.2f" %preco)

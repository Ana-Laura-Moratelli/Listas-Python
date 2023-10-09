#1)Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido
n = float(input("Digite uma nota de 0 a 10: "))
while n > 10 or n < 0:
    print ("Digite novamente uma nota de 0 a 10.")
    n = float(input("Digite a nota: "))
    
#2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
while usuario == senha:
    print("O usuário e senha estão iguais, por favor digitar novamente")
    usuario = input("Digite novamente seu usuário: ")
    senha = input("Digite novamente sua senha: ")

#3)Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxaanual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
a = 80000
b = 200000
anos = 0
while a < b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1
print (f"A quantidade de anos para A ultrapassar B é de aproximadamente: {anos} anos ")

#4)A seqüencia de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule oseu número de Fibonacci. F1= 1, F2= 1, F3= 2, etc
n = int (input ( 'Digite o valor de n: '))
a = 1
b = 1
c = 1
while c <= n-2:
    
    a, b = b, a + b
    c += 1
    
print ("O seu número de Fibonacci é:", b)

#5)Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
while a % b != 0:
    a, b = b, a % b
print(f"O mdc desses dois números é: {b}")

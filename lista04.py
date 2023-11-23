#1)Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
from random import sample
sorteio = sample(range(100),10)
maior = menor = sorteio[0]
x = 1
while x < 10:
    if sorteio[x] > maior: maior = sorteio[x]
    if sorteio[x] < menor: menor = sorteio[x]
    x = x + 1
print("Números sorteados: ", sorteio)
print(f"Maior: {maior}")
print(f"Menor: {menor}")

#2)Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
from random import sample
sorteio = sample(range(100),20)

par = []
impar = []
for x in sorteio:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
 
print("Números sorteados: ", sorteio)
print(f"Números pares: {par}")
print(f"Números ímpares: {impar}")

#3)Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.
from random import sample
sorteio1 = sample(range(100),10)
sorteio2 = sample(range(100),10)
sorteio3 = []
for x in zip(sorteio1, sorteio2):
    sorteio3.extend(list(x))
    
print(sorteio1)
print(sorteio2)
print(sorteio3)

#4)Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''.lower()
import string
for k in string.punctuation:
    texto = texto.replace(k,' ')
    
x = []
for p in texto.split():
    if p[0] in 'python' or p[-1] in 'python':
        x.append(p)
print(x)


#5)Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''.lower()
import string
for k in string.punctuation:
    texto = texto.replace(k, ' ')


def py(y):
    for k in y:
        if k in 'python':
            return True
    return False

x = [p for p in texto.split()
        if py(p) and len (p) > 4]
print ('O texto possui:',len(x),'palavras com uma das letras de python e com mais de 4 caracteres')


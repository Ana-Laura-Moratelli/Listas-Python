# ANA LAURA MORATELLI E MICHAEL DA SILVA SOUZA 
import requests
import random

# PARA PEGAR AS PALAVRAS DA PÁGINA
def escolhe():
    url = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        palavra = data.split('\n') 

        if palavra:
            return random.choice(palavra).lower()
        else:
            return None
    else:
        print("Falha em carregar a página")
        return None


def desenha(erro):
    if erro == 1:
        print(r"    +-----+   ")
        print(r"    |     |   ")
        print(r"    O     |   ")
        print(r"          |   ")
        print(r"          |   ")
        print(r"          |   ")
        print(r"==============")

    if erro == 2:
        print(r"    +-----+   ")
        print(r"    |     |   ")
        print(r"    O     |   ")
        print(r"    |     |   ")
        print(r"          |   ")
        print(r"          |   ")
        print(r"==============")

    if erro == 3:
        print(r"    +-----+   ")
        print(r"    |     |   ")
        print(r"    O     |   ")
        print(r"   \|     |   ")
        print(r"          |   ")
        print(r"          |   ")
        print(r"==============")

    if erro == 4:
        print(r"    +-----+   ")
        print(r"    |     |   ")
        print(r"    O     |   ")
        print(r"   \|/    |   ")
        print(r"          |   ")
        print(r"          |   ")
        print(r"==============")

    if erro == 5:
        print(r"    +-----+   ")
        print(r"    |     |   ")
        print(r"    O     |   ")
        print(r"   \|/    |   ")
        print(r"   /      |   ")
        print(r"          |   ")
        print(r"==============")

    if erro == 6:
        print(r"    +-----+   ")
        print(r"    |     |   ")
        print(r"    O     |   ")
        print(r"   \|/    |   ")
        print(r"   / \    |   ")
        print(r"          |   ")
        print(r"==============")

def ganhou(letras, certas):
    return set(letras) <= certas

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (Digite 's' para sim ou 'n' para não): ").lower()
    return resposta == 's'

def chute(letras):
    certas = set()
    erradas = set()
    max_tentativas = 7
    erro = 0

    while True:
        palavra_oculta = ''.join([letra if letra in certas else '_' for letra in letras])
        print("Palavra:", palavra_oculta)
        print("Letras corretas:", ', '.join(certas))
        print("Letras erradas:", ', '.join(erradas))
        desenha(erro)

        chute = input("Chute uma letra: ").lower()

        if chute.isalpha() and len(chute) == 1:
            chute = chute.lower() 
            if chute in certas or chute in erradas:
                print("Você já tentou esta letra. Tente outra.")
            elif chute in letras:
                print("Letra correta!")
                certas.add(chute)
            else:
                print("Letra errada.")
                erradas.add(chute)
                erro += 1
        else:
            print("Digite apenas uma letra.")

        if ganhou(set(letras), certas):
            print("Parabéns! Você descobriu a palavra:", letras)
            if jogar_novamente():
                letras = escolhe()
                if letras:
                    certas.clear()
                    erradas.clear()
                    erro = 0
                else:
                    print("Não foi possível obter a palavra")
                    break
            else:
                break

        if erro >= max_tentativas:
            print("Você atingiu o limite de tentativas. A palavra era:", letras)
            if jogar_novamente():
                letras = escolhe()
                if letras:
                    certas.clear()
                    erradas.clear()
                    erro = 0
                else:
                    print("Não foi possível obter a palavra.")
                    break
            else:
                break

# TESTE
palavra_sorteada = escolhe()

if palavra_sorteada:
    print("Bem-vindo ao jogo da Forca!")
    chute(palavra_sorteada)
else:
    print("Não foi possível obter a palavra.")

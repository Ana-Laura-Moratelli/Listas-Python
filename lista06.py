# A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
    return not dia_semana or feriado

# B. alunos_problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
  return a_sorri == b_sorri

# C. soma_dobro
# dados dois números inteiros retorna sua soma
# porém se os números forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8
def soma_dobro(a, b):
  return 2*(a + b) if a == b else a + b 

# D. diff21
# dado um inteiro n retorna a diferença absoluta entre n e 21
# porém se o número for maior que 21 retorna dobro da diferença absoluta
# diff21(19) -> 2
# diff21(25) -> 8
# dica: abs(x) retorna o valor absoluto de x
def diff21(n):
  return 2*abs(n - 21) if n > 21 else abs(n - 21)

# E. papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  return falando and (hora < 7 or hora > 20)

# F. dez
# dados dois inteiros a e b
# retorna True se um dos dois é 10 ou a soma é 10
def dez(a, b):
  return a == 10 or b == 10 or a + b == 10

# G. dista10
# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10

# H. apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  return s[:n] + s[n+1:]

# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]



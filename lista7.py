# A. multstring
# seja uma string s e um inteiro positivo n
# retorna uma string com n cópias da string original
# multstring('Hi', 2) -> 'HiHi'
def multstring(s, n):
  return n * s

# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  k = 1
  resp = ''
  while k <= len(s):
    resp = resp + s[:k]
    k = k + 1
  return resp

# C. array_count9
# conta quantas vezes aparece o 9 numa lista nums
def array_count9(nums):
  return nums.count(9)

# D. array_front9
# verifica se pelo menos um dos quatro primeiros é nove
# array_front9([1, 2, 9, 3, 4]) -> True
# array_front9([1, 2, 3, 4, 9]) -> False
# array_front9([1, 2, 3, 4, 5]) -> False
def array_front9(nums):
  return 9 in nums[:4]

# E. hello_name
# seja uma string name
# hello_name('Bob') -> 'Hello Bob!'
# hello_name('Alice') -> 'Hello Alice!'
# hello_name('X') -> 'Hello X!'
def hello_name(name):
  return f'Hello {name}!' 

# F. make_tags
# make_tags('i', 'Yay'), '<i>Yay</i>'
# make_tags('i', 'Hello'), '<i>Hello</i>'
# make_tags('cite', 'Yay'), '<cite>Yay</cite>'
def make_tags(tag, word):
  return f'<{tag}>{word}</{tag}>'

# G. extra_end
# seja um string s com no mínimo duas letras
# retorna três vezes as duas últimas letras
# extra_end('Hello'), 'lololo'
# extra_end('ab'), 'ababab'
# extra_end('Hi'), 'HiHiHi'  
def extra_end(s):
  return 3 * s[-2:]

# H. first_half
# seja uma string s
# retorna a primeira metade da string
# first_half('WooHoo') -> 'Woo'
# first_half('HelloThere') -> 'Hello'
# first_half('abcdef') -> 'abc'
def first_half(s):
  return s[:len(s)//2]

# I. sem_pontas
# seja uma string s de pelo menos dois caracteres
# retorna uma string sem o primeiro e último caracter
# without_end('Hello') -> 'ell'
# without_end('python') -> 'ytho'
# without_end('coding') -> 'odin'
def sem_pontas(s):
  return s[1:-1]

# J. roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# left2('Hello') -> 'lloHe'
# left2('Hi') -> 'Hi'
def roda2(s):
   return s[2:] + s[:2]

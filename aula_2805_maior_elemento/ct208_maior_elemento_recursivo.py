
# Programa phyton para dado um numero gera uma lista de suas permutações 
# Verifica quantas iterações necessárias para achar o maior elemento da lista
# Utiliza Tn,k trocas para calcular o valor das iterações até o número 15
# Daniela América da Silva
# Disciplina: ct208

# Importa library de permutações 
from itertools import permutations 

import numpy as np 
  
#seta vetor contador de trocas  
def set_contador (col):
   n = 0
   conta = []
   while n < col:
     conta.append(0)
     n+=1
   return (conta)

#cria a lista de números  
def cria_lista (num):
   n = 0
   lista = []
   while n < num:
     lista.append(n+1)
     n+=1
   return (lista)

#conta numero de trocas
def maior_trocas (elements):
  m = elements[0]
  n = 1
  t = 0
  while n < (len(elements)):
    if m < elements[n]: 
       m = elements[n]
       t+=1
    n+=1
  return (t)

# inicializa matriz t que armazena resultados das trocas
t = np.zeros((15, 16))   
t[0][0] = 1


#processa lista de permutações do número 2 ao 10
x = 2
while x < 11:
  # inicializa lista de trocas 
  trocas = []

  numeros = cria_lista (x)

  #inicializa contador trocas
  conta_trocas = set_contador(len(numeros))

  # realiza as permutações
  perm = permutations(numeros)
    
  # Conta as trocas
  for i in list(perm): 
    #print (i)
    number = maior_trocas (i)
    #imprime 
    #print (i, '(', number ,')')
    conta_trocas[number]+=1
  

  #print (trocas)    
  #print ('numero:', x, conta_trocas)

  #atualiza matriz trocas
  j = 0
  t[x-1][j]=x
  j = 1
  while j < x+1:
    t[x-1][j] = conta_trocas[j-1]
    j+=1 

  x+=1

#np.set_printoptions(precision=10, suppress=True, linewidth=10000)

np.set_printoptions(formatter={'float': lambda x: ' ' + str(x)})


#processa lista de permutações do número 11 ao 15, utilizando a recorrencia
l=10
c=1
while l < 15:
  t[l][0] = l+1
  t[l][c] = l*t[l-1][c]
  while c < l:
     c+=1
     t[l][c] = t[l-1][c-1] + l*t[l-1][c]
  c+=1
  t[l][c] = t[l-1][c-1] + l*t[l-1][c]
  l+=1
  c=1


print (t)

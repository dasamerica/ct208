
# Programa phyton para dado um numero gera uma lista de suas permutações 
# Verifica quantas iterações necessárias para achar o maior e menor elemento da lista
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
def maior_menor_trocas (elements):
  me = elements[0]
  ma = elements[0]
  n = 1
  t= [0,0,0,0]
  while n < (len(elements)):
    # conta trocas maior
    if ma < elements[n]: 
       ma = elements[n]
       t[0]+=1
    # conta trocas menor
    if me > elements [n]:
       me = elements[n]
       t[1]+=1
    n+=1
  return (t)

# inicializa matriz t que armazena resultados das trocas
t_maior = np.zeros((15, 16))   
t_maior[0][0] = 1

t_menor = np.zeros((15, 16))   
t_menor[0][0] = 1


#processa lista de permutações do número 2 ao 10
x = 2
while x < 11:
  # inicializa lista de trocas 
  trocas = []

  numeros = cria_lista (x)

  #inicializa contador trocas
  conta_trocas_maior = set_contador(len(numeros))
  conta_trocas_menor = set_contador(len(numeros))


  # realiza as permutações
  perm = permutations(numeros)
    
  # Conta as trocas
  for i in list(perm): 
    #print (i)
    number = maior_menor_trocas (i)
    #imprime 
    #print (i, '(', number ,')')
    conta_trocas_maior[number[0]]+=1
    conta_trocas_menor[number[1]]+=1
  

  #print (trocas)    
  #print ('numero:', x, conta_trocas)

  #atualiza matriz trocas
  j = 0
  t_maior[x-1][j]=x
  t_menor[x-1][j]=x
  j = 1
  while j < x+1:
    t_maior[x-1][j] = conta_trocas_maior[j-1]
    t_menor[x-1][j] = conta_trocas_menor[j-1]
    j+=1 

  x+=1

#np.set_printoptions(precision=10, suppress=True, linewidth=10000)

np.set_printoptions(formatter={'float': lambda x: ' ' + str(x)})


#processa lista de permutações do número 11 ao 15, utilizando a recorrencia
l=10
c=1
while l < 15:
  t_maior[l][0] = l+1
  t_maior[l][c] = l*t_maior[l-1][c]
  t_menor[l][0] = l+1
  t_menor[l][c] = l*t_menor[l-1][c]

  while c < l:
     c+=1
     t_maior[l][c] = t_maior[l-1][c-1] + l*t_maior[l-1][c]
     t_menor[l][c] = t_menor[l-1][c-1] + l*t_menor[l-1][c]

  c+=1
  t_maior[l][c] = t_maior[l-1][c-1] + l*t_maior[l-1][c]
  t_menor[l][c] = t_menor[l-1][c-1] + l*t_menor[l-1][c]

  l+=1
  c=1


print ('CONTA TROCAS PARA MAIOR NUMERO')
print (t_maior)
print ('CONTA TROCAS PARA MENOR NUMERO')
print (t_menor)


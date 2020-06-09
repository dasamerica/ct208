# Programa phyton para dado um numero gera uma lista de suas permutações 
# Utiliza divide and conquer e memoization
# Verifica quantas iterações necessárias para achar o maior elemento, menor elemento, o segundo maior elemento, e segundo menor elemento da lista
# Daniela América da Silva
# Disciplina: ct208

# Importa library de permutações 
from itertools import permutations 
# Importa library para matriz 
import numpy as np 
# Importa library para truncate 
import math
  
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

#divide and conquer min
def two_min(arr, iter):
    n = len(arr)
    m=math.trunc(n/2)

    #print(arr, n, iter)
    if n==2: # Oops, we don't consider this as comparison, right?
        
        if arr[0]<arr[1]:                   # Line 1
            iter+=1
            return (arr[0], arr[1], iter)
        else:
            iter+=1
            return (arr[1], arr[0], iter)
    if m == 1:
       if arr[0]<arr[1]:
          (least_left, sec_least_left) = (arr[0],arr[1])
       else:
          (least_left, sec_least_left) = (arr[1],arr[0])
    else: # always compare at least pairs
      (least_left, sec_least_left, iter) = two_min(arr[0:m], iter)
    (least_right, sec_least_right, iter) = two_min(arr[m:n], iter)
    if least_left < least_right:            # Line 2
        iter+=1
        least = least_left
        if least_right < sec_least_left:    # Line 3
            return (least, least_right, iter)
        else:
            return (least, sec_least_left, iter)
    else:
        iter+=1
        least = least_right
        if least_left < sec_least_right:    # Line 4
            return (least, least_left, iter)
        else:
            return (least, sec_least_right, iter)


#divide and conquer max
def two_max(arr, iter):
    n = len(arr)
    m=math.trunc(n/2)


    #print(arr, n, iter)
    if n==2: # Oops, we don't consider this as comparison, right?

        if arr[0]>arr[1]:                   # Line 1
            iter+=1
            return (arr[0], arr[1], iter)
        else:
            iter+=1
            return (arr[1], arr[0], iter)
    if m == 1:
       if arr[0]>arr[1]:
          (biggest_left, sec_biggest_left) = (arr[0],arr[1])
       else:
          (biggest_left, sec_biggest_left) = (arr[1],arr[0])
    else: # always compare at least pairs
      (biggest_left, sec_biggest_left, iter) = two_max(arr[0:m], iter)
    (biggest_right, sec_biggest_right, iter) = two_max(arr[m:n], iter)
    if biggest_left > biggest_right:            # Line 2
        iter+=1
        biggest = biggest_left
        if biggest_right > sec_biggest_left:    # Line 3
            return (biggest, biggest_right, iter)
        else:
            return (biggest, sec_biggest_left, iter)
    else:
        iter+=1
        biggest = biggest_right
        if biggest_left > sec_biggest_right:    # Line 4
            return (biggest, biggest_left, iter)
        else:
            return (biggest, sec_biggest_right, iter)

#conta numero de trocas incluindo o segundo elemento
#utiliza divide and conquer
def maior_menor_trocas (elements):
  me = 0
  ma = 0
  ma_2 = 0
  me_2 = 0
  t_ma = 0
  t_me = 0
  t= [0,0,0,0]

 
  (ma, ma_2, t_ma) = two_max(elements,-1)
  t[0]=t_ma
  t[2]=t_ma
 
  (me, me_2, t_me) = two_min(elements,-1)
  t[1]=t_me
  t[3]=t_me

  return (t)

#calculo do fatorial utilizando memoization
factorial_memo = {}
def factorial(k):
    if k < 2: return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]


# inicializa matriz t que armazena resultados das trocas
t_maior = np.zeros((15, 16))   
t_maior[0][0] = 1

t_menor = np.zeros((15, 16))   
t_menor[0][0] = 1

t_maior_segundo = np.zeros((15, 16))   
t_maior_segundo[0][0] = 1

t_menor_segundo = np.zeros((15, 16))   
t_menor_segundo[0][0] = 1

#processa lista de permutações do número 2 ao 10
x = 2
while x < 11:
  # inicializa lista de trocas 
  trocas = []

  numeros = cria_lista (x)

  #inicializa contador trocas
  conta_trocas_maior = set_contador(15)
  conta_trocas_menor = set_contador(15)
  conta_trocas_maior_segundo = set_contador(15)
  conta_trocas_menor_segundo = set_contador(15)


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
    conta_trocas_maior_segundo[number[2]]+=1
    conta_trocas_menor_segundo[number[3]]+=1
  

  #print (trocas)    
  #print ('numero:', x, conta_trocas)

  #atualiza matriz trocas
  j = 0
  t_maior[x-1][j]=x
  t_menor[x-1][j]=x
  t_maior_segundo[x-1][j]=x
  t_menor_segundo[x-1][j]=x

  j = 1
  while j < x+1:
    t_maior[x-1][j] = conta_trocas_maior[j-1]
    t_menor[x-1][j] = conta_trocas_menor[j-1]
    t_maior_segundo[x-1][j] = conta_trocas_maior_segundo[j-1]
    t_menor_segundo[x-1][j] = conta_trocas_menor_segundo[j-1]
    j+=1 

  x+=1


#utilizando dividde and conquer o número de iterações é o fatorial do número
#é possível utilizar memoization para calcular o fatorial a partir do número 11

#processa lista de permutações do número 11 ao 15, utilizando a recorrencia
l=10
while l < 15:
  t_maior[l][0] = t_menor[l][0] = t_maior_segundo[l][0] = t_menor_segundo[l][0] = l+1
  t_maior[l][l+1] = t_menor[l][l+1] = t_maior_segundo[l][l+1] = t_menor_segundo[l][l+1] = factorial(l+1)
  l+=1

#np.set_printoptions(precision=10, suppress=True, linewidth=10000)

np.set_printoptions(formatter={'float': lambda x: ' ' + str(x)},linewidth=10000 )


print ('CONTA TROCAS PARA MAIOR NUMERO')
print (t_maior)
print ('CONTA TROCAS PARA MENOR NUMERO')
print (t_menor)

print ('CONTA TROCAS PARA SEGUNDO MAIOR NUMERO')
print (t_maior_segundo)
print ('CONTA TROCAS PARA SEGUNDO MENOR NUMERO')
print (t_menor_segundo)


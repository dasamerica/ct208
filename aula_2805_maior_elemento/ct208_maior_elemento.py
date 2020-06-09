
# Programa phyton para dado um numero gera uma lista de suas permutações 
# Verifica quantas iterações necessárias para achar o maior elemento da lista
# Daniela América da Silva
# Disciplina: ct208

# Importa library de permutações 
from itertools import permutations 
  
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


#processa lista de permutações do número 1 ao 10
x = 1
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
    #trocas.append(number)
    conta_trocas[number]+=1
  

  #print (trocas)    
  print ('numero:', x, conta_trocas)
  x+=1
  

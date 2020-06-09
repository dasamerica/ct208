#Diversos exemplos de implemntação de Fibonacci
#Daniela América da Silva

import numpy as np 

#Cálculo de Fibonacci com a técnica loop:

def fib(n):
 a = 1
 b = 1
 for i in range(n-1):
  a, b = b, a+b
#  print (a)
 return a


print ('Fibonacci Loop')
print (fib(8))

#Cálculo de Fibonacci recursivo:

def fibR(n):
 if (n==1 or n==2):
  #print (1)
  return 1
 b = fibR(n-1)+fibR(n-2)
 #print (b)
 return b

print ('Fibonacci Recursivo')
print (fibR(8))

## Usando memoization
def memoize(fn, arg):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg)
 b= memo[arg]
 #print (b)
 return b

## fib() as written in example 1.
print ('Fibonacci Memoization')
fibm = memoize(fib,8)
print (fibm)




#Fibonacci Prof. Alonso
def fib2(m,n):
  if (m[n] < 0):
      m[n] = fib2(m,n-1) + fib2(m,n-2);
  l = m[n]
  #print (l)
  return l

def Fibonacci(n):
  m = []
  j = 0
  while j < n:
     m.append(0)
     j+=1
  m[0],m[1] = 1,1
  for i in range(2,n,1):
     #print ('passou', i)
     m[i] = -1 #indicação de que não foi resolvido
  #print (m)
  k = fib2(m,n-1)
  #print (k)
  return k

print ('Fibonacci Memoization Prof. Alonso')
print (Fibonacci(8))

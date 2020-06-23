# Daniela America da Silva
# Exemplos de implementação heap minimo utilizando exemplo Prof. Alonso CT234


def Sift(i, n):
  show_tree(v)
  esq = (2*i)
  dir = (2*i)+1
  menor = i
  if (esq <= n and v[esq] < v[i]):
    menor = esq
  if (dir <= n and v[dir] < v[menor]):
    menor = dir
  if (menor != i):
    aux = v[i];
    v[i] = v[menor]
    v[menor] = aux
    Sift(menor, n)

def Build(v):
  n = len(v)-1
  x = int(n/2)
  for i in range (x,0,-1):
   Sift(i, n)
   

def Max():
   return v[len(v)-1]

def Min():
   return v[1]

def ExtractMin():
  size = len(v)-1
  if (size < 1):
     print ("heap underflow")
  else:
     min = v[1]
     v[1]= v[size]
     del v[size]
     size=len(v)-1
     #print (1,size)
     Sift(1,size)
     return min

def ExtractMax():
  size = len(v)-1
  if (size < 1):
     print ("heap underflow")
  else:
     max = v[size]
     del v[size]
     size=len(v)-1
     #print (1,size)
     Sift(1,size)
     return max


# Imprime a arvore
# exemplo do link https://www.w3resource.com/python-exercises/heap-queue-algorithm/python-heapq-exercise-19.php
import math
from io import StringIO
def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    y=[] + tree
    del y[0]
    for i, n in enumerate(y):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return


v = ["",2,6,3,4,1,1,3,3,-1,3,3]
v[0] = "Lista"
print (v)   
Build(v)

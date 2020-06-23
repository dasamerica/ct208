# Daniela America da Silva
# Exemplos de implementação heap maximo utilizando exemplo Prof. Alonso CT234


def Sift(i, n):
  esq = 2*i
  dir = (2*i)+1
  maior = i
  if (esq <= n and v[esq] > v[i]):
    maior = esq
  if (dir <= n and v[dir] > v[maior]):
    maior = dir
  if (maior != i):
    aux = v[i]
    v[i] = v[maior]
    v[maior] = aux
    Sift(maior, n)

def Build(v):
  n = len(v)-1
  x = int(n/2)
  for i in range (x,0,-1):
   Sift(i, n)

def Max():
   return v[1]

def Min():
   return v[len(v)-1]

def ExtractMax():
  size = len(v)-1
  if (size < 1):
     print ("heap underflow")
  else:
     max = v[1]
     v[1]= v[size]
     del v[size]
     size=len(v)-1
     #print (1,size)
     Sift(1,size)
     return max

def ExtractMin():
  size = len(v)-1
  if (size < 1):
     print ("heap underflow")
  else:
     min = v[size]
     del v[size]
     size=len(v)-1
     #print (1,size)
     Sift(1,size)
     return min

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


v = ["",4,1,3,2,16,9,10,14,8,7]
v[0] = "Lista"
print (v)   
Build(v)
v[0]= "Heap"

print(v) 
print("Max:",Max(), "Min:",Min())

show_tree(v)

print("Extract Max", ExtractMax())
print("Extract Min", ExtractMin())

v[0]= "Heap sem max e sem min"
print(v) 
print("2o Max:",Max(), "2o Min:",Min())

show_tree(v)


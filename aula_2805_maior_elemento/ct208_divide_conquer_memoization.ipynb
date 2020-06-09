# Daniela America da Silva
# Exemplos de implementação divide and conquer para BinarySearch e Maior/menor elemento
# Exemplo de implementação para fatorial utilizando memoization


#Exemplo Prof Alonso Binary Search

import math

def BinarySearch(v, l, r, x):
  if (r < l):
    return 'false'
  q = math.trunc((l+r)/2)
  if (v[q] == x):
    return 'true'
  if (v[q] > x):
    return BinarySearch(v, l, q-1, x);
  return BinarySearch(v, q+1, r, x);


v = [2,3,5,4,1,6]
print(BinarySearch(v, 0, 3, 8))


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

v = [8,7,6,5,4,3,2,1]
print(two_min(v,-1))
print(two_max(v,-1))


factorial_memo = {}
def factorial(k):
    if k < 2: return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]

print (factorial(11))           

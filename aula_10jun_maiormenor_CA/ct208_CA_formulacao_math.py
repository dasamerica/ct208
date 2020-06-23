# #@title
# Daniela America da Silva
# Exemplos de implementação para formulacao matematica proposta na CT208

#start = '{0:05b}'.format(6)
start= [0,0,1,1,0]
v = [] + start
print ("t",0,start)
next=[0,0,0,0,0]
for i in range(10):
  for n in range(5):
    if (n==0):
      next[n] = ((int(v[n]) + int(v[n+1]))%2)
    else:
      if (n==4):
        next[n] = ((int(v[n-1]) + int(v[n]))%2)
      else:
        next[n] = ((int(v[n-1]) + int(v[n]) + int(v[n+1]))%2)
  
  print("t",i+1, next)
  v=[] + next

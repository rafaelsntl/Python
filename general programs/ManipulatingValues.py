def Read (x):
  x = float (input())
  return x
def Write(y):
  print ('{:.1f}'.format(y))
  return
def Average (a,b,c,d):
  weightedAverage = (a+(3*b)+(2*c)+d)/7
  return weightedAverage
def Smaller (a,b,c,d):
  smaller = 0
  if a < b and a<c and a<d:
    smaller = a
  elif b < a and b < c and b < d:
    smaller = b
  elif c < a and c < b and c < c:
    smaller = c
  elif d < a and d < b and d < c:
    smaller = d
  return smaller
def Bigger (a,b,c,d):
  bigger = 0
  if a > b and a>c and a>d:
    bigger = a
  elif b >a and b > c and b>d:
    bigger = b
  elif c >a and c > b and c>c:
    bigger = c
  elif d >a and d > b and d>c:
    bigger = d
  return bigger 
def Variation(x,y):
  return x - y

a = Read('') 
b = Read('')
c = Read('')
d = Read('')

Write(Average(a,b,c,d))
Write(Smaller(a,b,c,d))
Write(Bigger(a,b,c,d))
Write(Variation((Bigger(a,b,c,d)),(Smaller(a,b,c,d))))
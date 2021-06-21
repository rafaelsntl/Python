def GDC(a,b):
    if (a < 0 or b < 0):
        print ('Is the value less than zero?')
        return True
    if a > b:
        max = a
    else:
        max = b
    for i in range (max,0,-1):
        if (a % i == 0 and b % i == 0):
            return i
        
a = int(input())
b = int(input())

print(GDC(a,b))
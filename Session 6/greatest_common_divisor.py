def gcd(a,b):

    if a > b:
        a,b=b,a 

    for x in range(a,0,-1):
        if a % x == 0 and b % x == 0:
            return x
  
a = 9 
b = 12 
print (str(gcd(a,b)))
       

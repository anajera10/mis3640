from math import sqrt
def quad():
    print("This will solve the quadratic equation")
    print()
a= int(input("input the first coefficient:"))
b= int(input("input the second coefficient:"))
c= int(input("input the third coefficient:"))
print()
disc = b**2 - 4*a*c #this is the discriminant 
disc1= sqrt(disc)
positive= (-b + disc1)/ (2*a)
negative= (-b - disc1)/ (2*a) 

print("The positive value of the quadratic is {0}, and the negative value is {1}".format(positive,negative))
 

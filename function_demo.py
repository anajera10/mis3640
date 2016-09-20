def print_lyrics():
    print("Hey, Jude. Don't make it bad.")
    print("Take a sad song and make it better.")

print(type(print_lyrics))
print_lyrics()

def repeat_lyrics():
    print_lyrics()
print('Na - na - na - na - na')
print_lyrics()

repeat_lyrics()

def print_twice(a):
    print(a)
    print(a)

print_twice('Babson')

my_name= 'Jerry'
print_twice(my_name)

def cat_twice(part1,part2):
    cat = part1+part2
    print_twice(cat)

line1 = 'Bing tiddle'
line2 = 'tiddle bang'
#cat_twice(line1,line2)

#print(cat)
#print(line1)



def give_me_a_break():
    str1= 'break'
    print('another break')
     return str1
   
new_str = give_me_a_break()
print(new_str)
#give_me_a_break()

#print(give_me_a_break())

def a_new_function_demo():
    s=0
    for x in 'Chris':
        print(x)
        print(ord(x))
        s = s + ord(x)



def quadratic(a, b, c)
A = b **2-4*a*c 

if A >= 0 
    x1=((-b+math.sqrt(A))/2*a)
    x2=((-b-math.sqrt(A)/)2*a)
    return x1,x2

else:
    #print('No real number solution')
    return "Anything" 

a = int(input('please enter a number:'))
b = int(input('please enter a number:'))
c = int(input('please enter a number:'))
print('results are:')
msg = quadratic(a,b,c)
print(msg)








input()
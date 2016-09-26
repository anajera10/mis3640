'''
result = 0 
for i in range(11):
    if i% 2 == 0: 
        print ('current i:',i)
        result += i #result += i means the same as result = result + i 
print(result)
'''
'''
#while loop
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print ('Blastoff')

countdown(5)
'''
'''
iteration = 0
while iteration < 5:
    count = 0
    #the variable letter in th eloop stands for every character, including spaces and commas! 
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break #means you jump out of the current loop
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
'''

'''
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)

print('Done!')
'''
'''
result = 0 
i = 1 
while i < 11:
    result = result + i 
    i = i + 1 
print(result) 
'''
'''
#even number
result = 0 
i = 1 
while i < 11:
    if i % 2 ==0:
        result = result + i 

    i = i + 1 
print(result)
'''
# same as the while loop above
result = 0 # this is to show that the result starts with zero
i = 1 
while i <= 10:
    if i % 2 ==0:
        result = result + i 

    i = i + 1 
print(result)
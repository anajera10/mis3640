x = int(input('Enter an integer: '))
ans = 0
if x<0:
    return abs(x)
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))

#cubic number 
 
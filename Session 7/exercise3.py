def mysqrt
x = 3 
a = 9
y = (x + a/x) / 2
print(y)

while True:
    print(x)
    y = (x + a/x) / 2
    if abs(y-x) < epsilon:
        break
    x = y


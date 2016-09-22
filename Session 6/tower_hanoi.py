def move(n, source, bridge, destination):
    if (n>1):
        move(n - 1, source, bridge, destination)
        move (1, source, destination,bridge)
        move(n-1, bridge, destination,source)
    else:
        print (source, "->", destination)

def hanoi(h):
    move(h, "A", "B", "C")

hanoi(3)
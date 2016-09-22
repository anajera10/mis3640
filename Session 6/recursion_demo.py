def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print (n)
        countdown (n-1)

    countdown(3)

    def print_n(s,n):
        if n <= 0;
            return #once it hits less than zero stop 
        print(s)
        print('n =',n)
        print_n(s, n-1)

    print_n('Hello',3) #underscore n print s (n amt of times)
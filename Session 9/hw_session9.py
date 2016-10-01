#Excercise 2 
#Recursion\
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    
    return is_abecedarian(word[1:])

#whileloop
def is_abcedarian(word):
    i = 0 
    while i < len(word)-1:
        if word[i + 1] <word[i]:
            return False
        i = i +1 
    return True 

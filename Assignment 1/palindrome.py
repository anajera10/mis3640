def isPalindrome(s):
    if len(my_string) <= 1:
        return True
    elif my_string[0] == my_string[len(my_string)-1]:
        return is_palindrome(my_string[1:len(my_string)-1])
    else:
        return False

inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")
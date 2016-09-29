# #Question 1:
# import math
# def crazy_about_9(a, b):
    
 
#     return a == 9 or b == 9 or a+b == 9 or a-b == 9
       
    
# # When you've completed your function, uncomment the
# # following lines and run this file to test!

# print(crazy_about_9(2, 9))
# print(crazy_about_9(4, 5))
# print(crazy_about_9(3, 8))

#Question 2 
# def leap_year(year):

#     if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
#         print("%d is a Leap Year" %year)
#     else:
#         print("%d is Not the Leap Year" %year)

# print(leap_year(1900))
# print(leap_year(2016))
# print(leap_year(2017))
# print(leap_year(2000))

#Question3

def sum_squares(n):
    return sum(i**2 for i in range(1, n+1))

print(sum_squares(1))
print(sum_squares(100))

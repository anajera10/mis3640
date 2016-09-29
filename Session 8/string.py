# team = "New England Patriots"
# print(team[0])
# print(len(team))

# print(team[len(team)-1])

# last = team[-1]
# print(last)

#index = 0 
#while index < len(team):
 #   letter = team[index]
  #  print(letter)
   # index += 1 

# for means one by one 

# for letter in team:
#     print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         suffix = 'uack'
#     else:
#         suffix='ack'
#     print(letter + suffix)

# team = 'New England Patriots'
# print(team[0:11])
# print(team[12:20])
# print(team[:11])
# print(team[12:])
# print(team[4:3])

# print(team[::2]) #every other letter

# team = 'New England Patriots'
# team[12:20] = 'Seahawks'

# new_team = team[:12]+ 'Seahawks'

# print(team)

#Exercise 2 
# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

# word = input('Which word?\n')
# letter = input('Which letter?\n')
 
# def count(word, letter):
#    i = 0
#    for x in word:
#        if x == letter:
#            i += 1
#        print (i)
 
# count(word, letter)

#Exercise 3 
# team = 'New England Patriots'
# new_team = team.upper()
# print(new_team)

# team = 'New England Patriots'
# index = team.find('a')
# print(index)
# print(team.find('En'))

# print(team.find('a', 10)) 

# name = 'bob'
# print(name.find('b', 1, 2))

# hw = 'python is great'
# index = hw.replace('python is great', 'python is hard')
# print(index)

# index = 'Hello World'
# print(index.split(' '))

website = 'www.learnpython.com'
print(website.strip('w.com'))





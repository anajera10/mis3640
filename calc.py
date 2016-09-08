print((42*60)+42)

print(10/1.61)

print((((42*60)+42)/(10/1.61)/60))
print((((42*60)+42)/(10/1.61)))

print((10/1.61)/(((42/60)+42)/60))






print('Q1: Volume of a sphere')
x=5
pi=3.1415926
print('4/3πr3=',((4/3)*pi*(x**3)))
 

n=60
cover_price = 24.95
discount = (1-.4)
shipping_costs = (3 + .75*(n-1))
print('Q2: Total Wholesale Cost =', ((cover_price*(discount)*n)+(shipping_costs)))

print('Q3: Time Home for breakfast')
time_of_departure = ((60*60*6)+(52*60)) # 6:52am this is the time in seconds
easy_pace = ((8*60)+15) # this is the time in seconds
tempo = ((7*60)+12) #this is the time in seconds
five_mile_run = ((2*easy_pace)+(3*tempo))
time_home_in_sec= time_of_departure+five_mile_run
time_home_in_hrs = time_home_in_sec/60/60
min = (time_home_in_hrs-7)*60
print('%s hr %.0f min' % (7, min))


print('Q4: The percentage of increase')
print('%.2f' % ((89-82)/82))













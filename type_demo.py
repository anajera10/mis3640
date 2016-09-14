import time
print(time.time()) 
current=time.time()
seconds=current//60 
minutes = (current//60) % 60
hours = (current//60)//60 %24
days = current//60//60//24
print('Current time: %d days, %d hours, %d minutes and %d seconds from Epoch.' % (days,hours,minutes,seconds))











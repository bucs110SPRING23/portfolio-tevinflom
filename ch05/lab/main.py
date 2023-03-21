#import pygame 
# import random as r
#pygame.init()



def threenp1(n):
    count = 0 
    while n > 1:
       if n % 2 == 0:
        n = int(n / 2)
        count += 1
       else:
        n = int(3 * n + 1)
        count += 1
    return count

mypair = set()
def counter(): 
    upper_limit = int(input("Define an Upper Limit: "))
    for num in range(2, upper_limit):
        count = threenp1(num)
        print("Number of Iterations: ", counter)
        mypair.add((num, count))
    return(num, count) 

while True: 
   counter()
   print(mypair)
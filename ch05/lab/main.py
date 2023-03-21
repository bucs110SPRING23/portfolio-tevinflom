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

num = int (input("Enter a number: "))
mypair = set() #creates a dictionary 

def numchecker(num):
    if num < 2 is True: 
        newnum = num + 1
    else:
        newnum == num
    return(newnum)

def counter():
    #num = int (input("Enter a number: "))
    #for num in mypair: 
       #if num < 2: 
          #newnum = num - 1
       #else:
          #newnum = num
    newnum = numchecker(num)
    iterations = threenp1(newnum) 
    print("Number of Iterations: ", iterations)
    mypair.add((newnum, iterations))
    return (newnum, iterations)

while True: 
   counter()
   print(mypair)




 
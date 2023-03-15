
def multiplier (x,y): 
    accumulator = 0 
    for i in range(y): 
        accumulator = accumulator + x
    return accumulator 

def exponent (x,y): 
    accumulator = 1
    for i in range(y): 
        accumulator = accumulator * x
    return accumulator
    
def square(x):
    return multiplier(x, x) # x = x, y = x

def main():
    x = int(input("enter a number: "))
    y = int(input("enter a number: "))
    result = multiplier (x, y) 
    print(result) 
    result = exponent (x, y) 
    print(result) 
    result = square (x, y) 
    print(result) 

main()

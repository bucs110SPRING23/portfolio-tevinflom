class Rectangle:
    def __init__ (self, x, y, h, w): 
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(h)
        self.width = abs(w)
        return None
    def __str__(self): 
        myoutput = print("(x: {self.x}, y: {self.y}), width: {self.width}, height: {self.height}")
        return myoutput 
class Circle:
    def __init__(self,radius,pi = 3.14):
        self.r = radius
        self.pi = 3.14
    
    def getArea(self):
        if self.r>=0:
            return(((self.r)**2)*self.pi)
        else:
            return(0.0)
            
    def getCircumference(self):
        if self.r>=0:
            return(2*self.r*self.pi)
        else:
            return(0.0)

if __name__ == "__main__":
    one_circle = Circle(float(input()))
    print(float(one_circle.getArea()))
    print(float(one_circle.getCircumference()))
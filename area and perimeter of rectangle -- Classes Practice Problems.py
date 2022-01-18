class Rectangle:
    
    def __init__(self,length,width):
        self.l = length
        self.w = width
    
    def rectangle_area(self):
        if self.l>0 and self.w>0:
            return (int(self.l*self.w))
        else:
            return 0
    
    def rectangle_perimeter(self):
        if self.l>0 and self.w>0:
            return(int(2*(self.l+self.w)))
        else:
            return 0

if __name__ == "__main__":
    newRectangle = Rectangle(int(input()), int(input()))
    print(newRectangle.rectangle_area())
    print(newRectangle.rectangle_perimeter())class Rectangle:
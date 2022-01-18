class Rectangle:
    def __init__(self,length,width):
        self.l=length
        self.w=width
    
    def calculatePerimeter(self):
        return(2*(self.l + self.w))

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    l, w = map(int, input().split())
    r1 = Rectangle(l, w)
    print(r1.calculatePerimeter())
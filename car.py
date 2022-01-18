class Car:
    def __init__(self,name='Audi',model='A4'):
        self.name = name
        self.model = model
    def name(self):
        return self.name
    def model(self):
        return self.model

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    flag = int(input())
    if flag == 1:
        input_string = input().split()
        p1 = Car(input_string[0], input_string[1])
    else:
        p1 = Car()

    print(p1.name)
    print(p1.model)
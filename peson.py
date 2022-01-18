### Define the required class here...
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def name(self):
        return self.name
    def age(self):
        return self.age

### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    input_string = input().split()

    p1 = Person(input_string[0], int(input_string[1]))

    print(p1.name)
    print(p1.age)
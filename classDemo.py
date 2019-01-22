class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog =Dog()
dog.run()
print (isinstance(dog,Dog))
print (isinstance(dog,object))
print(type(dog))
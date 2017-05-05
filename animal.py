class Animal(object):

    def run(self):
        print('Animal is running...')

    def eat(self):
        print('Animal is eating...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def __init__(self):
        self.name = 'Tom'

    def __str__(self):
        return self.name

    def __len__(self):
        return 100


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
print(cat)

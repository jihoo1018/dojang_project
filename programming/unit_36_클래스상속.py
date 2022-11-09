from abc import abstractmethod


class Animal:
    @abstractmethod
    def eat(self):
        print('먹다')

class Wing:
    @abstractmethod
    def flap(self):
        print('파닥거리다')

class Bird(Animal,Wing):
    def fly(self):
        print('날다')

b= Bird()
b.eat()
b.flap()
b.fly()

if __name__ == '__main__':
    print(issubclass(Bird, Animal))
    print(issubclass(Bird, Wing))

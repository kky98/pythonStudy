# 상속
# 클래스의 기능을 물려받을 수 있음.
# 다중상속이 가능함.

class Animal:
    def __init__(self, nm):
        self.name = nm
    def move(self):
        print('move')
    def speak(self):
        pass

class Dog(Animal): #Animal 상속받음
    def speak(self):
        print("bark")
class Duck(Animal):
    def speak(self):
        print("quack")
dog = Dog("doggy")
print(dog.name)  #부모 변수
dog.move()       #부모 기능
dog.speak()      #오버라이딩
duck = Duck("donald")
print(duck.name)
duck.move()
duck.speak()
#상속
#클래스의 기능을 물려받을 수 있음
# 다중상속 가능


class Animal:
    def __init__(self,nm):
        self.name =nm
    def move(selfs):
        print('move')
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("b")
class Duck(Animal):
    def speak(self):
        print('q')

dog= Dog('doggy')
print(dog.name) #부모 변수
dog.move() #부모 기능
dog.speak() #오버라이딩
duck=Duck('dona')
duck.move()
duck.speak()

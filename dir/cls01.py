# py 도 객체지향 프로그래밍
# 클래스 명은 단어의 첫문자로 하는 capWord방식

class Rectangle:
    count =0
    def __init__(self,w,h): #초기자(객체 생성할때마다 실행)
        self.width = w
        self.height = h
    # 인스턴스 메서드
    def calcArea(self):
        return  self.width*self.height
    @staticmethod
    def isSquare(w,h):
        print('정적')
        # 클래스 메서드는 객체 인스턴스의미하는 self 대신cls가짐
        #cls통해 클래스 변수에 접근
    @classmethod
    def printCount(cls):
            print('클래스 메서드')
            cls.count +=1
            return cls.count
#인스턴스
a= Rectangle(2,2)
b=Rectangle(10,10)
print(a.calcArea() )# 인스턴스 메서드 사용가능
print(b.calcArea() )
#Rectangle.calcArea() # 인스턴스 메서드는 인스턴스만 사용가능
print(Rectangle.printCount())
print(Rectangle.isSquare(3,10))
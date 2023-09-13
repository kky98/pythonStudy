# python도 객체지향 프로그래밍
# 클래스명은 단어의 첫문자를 대문자로 하는 CapWords 방식으로 명명
class Rectangle:
    count = 0 #클래스 변수
    def __init__(self, w, h): #초기자 (객체를 생성할 때마다 실행되는 메서드)
        self.width = w
        self.height = h  #인스턴스 변수
    # 인스턴스 메서드
    def calcArea(self):
        return self.width * self.height
    # static : 인스턴스 변수에 접근할 수 없음. 독립적 함수의 기능
    @staticmethod
    def isSquare(w, h):
        print('정적 메서드')
    # 클래스 메서드는 객체 인스턴스를 의미하는 self 대신 cls를 가짐
    # cls를 통해 클래스 변수에 전근 할 수 있음.
    @classmethod
    def printCount(cls):
        print('클래스 메서드')
        cls.count +=1
        return cls.count
# 인스턴스
a = Rectangle(2, 2)
b = Rectangle(10, 10)
print(a.calcArea()) #인스턴스 메서드를 사용할 수 있음.
print(b.calcArea())
# Rectangle.calcArea()  #인스턴스 메서드는 인스턴스만 사용가능함
print(Rectangle.printCount()) # 클래스 메서드는 클래스.메서드 로 바로 사용가능
print(Rectangle.isSquare(3, 10)) #바로 사용가능(인턴스변수, 클래스변수에는 접근못함)
class Point:
    count_of_instance = 0  #self 없이 클래스 영역에 선언
    #모든 인스턴스들이 공유하는 객체

    #생성자 -> 여러가지 생성자에 대응하는 '단 한개'의 생성자의 만들어야 함.
    #생성자는 주로 객체의 초기화 담당
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        Point.count_of_instance += 1

    #소멸자
    #소멸자는 주로 객체가 소멸될 때
    def __del__(self):
        Point.count_of_instance -= 1

    #문자열 연결/출력시 호출되는 내부 메서드    -----for EndUser
    def __str__(self):
        #출력포맷 리턴
        return "Point x = {}, y = {}".format(self.x, self.y)

    #repr, eval
    #repr함수를 호출하면 반환되는 문자열 포맷   -----for Developers
    #eval함수를 이용해 해당 객체를 복원할 수 있는 용도의 문자열
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    # enter, exit
    # with~as구문이 시작될 때 호출되는 메서드
    # def __enter__(self):
    #     return self
    # with~as구문이 종료될 때 호출되는 메서드
    # def __exit__(self, exc_type, exc_val, exc_tb):




    #<<<<<<<<<<<<<<<<   연산자 오버로딩   >>>>>>>>>>>>>>>>>>>>
    #새로운 클래스를 만들었다는 것은 새로운 자료형을 만들었다는 의미이므로
    #새 자료형에 대한 연산자의 작동방식을 코드올 작성해줄 필요가 있다.
    #if not, TypeError

    #수치연산자 오버로딩
    def __add__(self, other):     #Point(x, y) + other
        #other의 타입 체크한 후 메서드 실행
        if isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        elif isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return self + other

    def __sub__(self, other):    #Point(x, y) - other
        if isinstance(other, (int, float)):
            return Point(self.x - other, self.y - other)
        elif isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return self - other

    def __eq__(self, other):     #Point(x, y) == other
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return self == other

    #역이행 연산자
    def __radd__(self, other):     #other + Point(x, y)
        #other의 타입 체크한 후 메서드 실행
        if isinstance(other, (int, float)):
            return Point(other + self.x, other + self.y)
        return other + self




    def set_x(self, x):      #인스턴스 메서드의 첫번째 인자는 항상 'self'
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self):
        print("점 ({}, {})를 그렸습니다.".format(self.x, self.y))

    @classmethod
    def get_count_of_instance(cls):     #cls -> 클래스 객체의 참조 주소
        return cls.count_of_instance

    #class namespace 안쪽에 있을 뿐
    #class 멤버와는 전혀 연관 없는
    @staticmethod
    def static_method():
        print("static method 호출")




#<<<<<<<<<<<<<<<<   상속   >>>>>>>>>>>>>>>>>>>>>>
#부모로부터 멤버를 물려받은 이후, 필요한 부부만 추가 구현
#부모가 가진 메서드를 재정의

class ColorPoint(Point):     #부모가 Point인 서브클래스 ColorPoint
    def __init__(self, x = 0, y = 0, color = "black"):
        #부모(super)의 생성자 호출:
        super().__init__(x, y)
        self.color = color

    def draw(self):
        print("{}색 점({}, {})을 그렸습니다.".format(self.color, self.x, self.y))

    def __str__(self):     #출력포맷 변경
        return "ColorPoint({}, {}, {})".format(self.x, self.y, self.color)
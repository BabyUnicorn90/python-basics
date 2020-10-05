from oop.point import Point, ColorPoint


def test_bound_instance_method():
    #객체 인스턴스를 직접 호출하여 접근하는 방법
    #인수로 self는 전달하지 않음
    p = Point()
    p.set_x(10)
    p.set_y(20)
    p.draw()

def test_unbound_class_method():
    #클래스 객체를 통해 우회접근하는 방법
    #self인수에 객체의 참조 주소 전달
    p = Point()
    Point.set_x(p, 10)
    Point.set_y(p, 20)
    Point.draw(p)

def test_other_method():
    #static, class멤버에 접근하기
    print("참조 카운트: ", Point.get_count_of_instance())    #get_count_of_instance에는 cls인자가 있고, Point클래스를 받기 때문에 따로 적어주지 않아도 된다.
    Point.static_method()



#[생성자와 소멸자] 테스트
def test_constructor():
    p1 = Point(10, 20)    #__init__ 수행
    print("x = {}, y = {}, count_of_instance = {}".format(p1.x, p1.y, Point.get_count_of_instance()))

    p2 = Point(100, 200)
    print("x = {}, y = {}, count_of_instance = {}".format(p2.x, p2.y, Point.get_count_of_instance()))

    del p1   #__del__ 수행
    print("count_of_instance = {}".format(Point.get_count_of_instance()))


def test_to_string():
    p = Point(10, 20)
    print("p = ", p)     #출력값: 주소  --> 문자열화 필요 (point.py에 __str__ 지정하기)

    #repr함수 -> __repr__메서드 수행
    print("repr(p): ", repr(p))

    #eval함수 -> 객체 복원
    p2 = eval(repr(p))
    print(p2, type(p2))


def test_operator():
    p = Point(10, 20)

    print("p + int: ", p + 10)
    print("Point + Point: ", p + Point(10, 20))

    print("p - int: ", p - 5)
    print("Point - Point: ", p - Point(10, 10))

    print("Point == Point: ", p == Point(10, 20))

    print("int + Point: ", 10 + p)   #역이행 연산자



#[상속] 테스트
def test_inheritance():
    cp = ColorPoint(10, 20, "빨간")

    print("CP: ", cp)
    cp.draw()
    print(dir(cp))     #내부멤버 확인



if __name__ == "__main__":
    #test_bound_instance_method()
    #test_unbound_class_method()
    #test_other_method()
    #test_constructor()
    #test_to_string()
    #test_operator()
    test_inheritance()
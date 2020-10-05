#클래스 정의테스트:

class MyString:
    pass

print(" ===My String Class")
s = MyString
print(type(s))

print("s의 클래스 확인: ", s.__class__)
print("MyString의 부모 확인: ", MyString.__bases__)    #여러 부모로부터 상속 可

print("s의 구성요소: ", dir(s))
print("object의 구성요소: ", dir(object))


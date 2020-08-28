
# 변수 이름은 문자, 숫자, _로 구성
# 각 코드를 구분하기 위한 식별자

friend = 1
a = 2
my_name = '파란초'
your_name = '둘리'
가격1 = 2000
print(가격1)


# 에러를 일으키는 변수 형식

# friend$ = 1      #특수기호는 _ 만 可
# def = 1          #키워드로 등록된 단어들 不
# 1a = 2           #숫자로 시작 不



# 모듈: 키워드나 함수를 모아놓은 것. 외부에 모듈을 만들어놓고 끌어와서 사용 可
import keyword
print(keyword.kwlist)

# swqp 1
x = 10
y = 20
print('======before swap 1=======')
print(x, y)
x = y                                  # x = 20
y = x                                  # y = 20
print('======after swqp 1========')
print(x, y)



# swqp 2
x = 10
y = 20
print('======before swap 2========')
print(x, y)
temp = x                                 # temp = 10
x = y                                    # x = 20
y = temp                                 # y = 10
print('======after swqp 2========')
print(x, y)




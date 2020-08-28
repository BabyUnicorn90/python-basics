# helloworld.py


# 블록시작_전역범위
print('hello world')


# 함수정의
def my_func(i):
    print('블록시작_함수정의 시작')
    if i > 10:
        print('블록시작_조건문')
    else:
        print('small')
    print('블록끝_함수정의 끝')


# 함수호출
my_func(20)

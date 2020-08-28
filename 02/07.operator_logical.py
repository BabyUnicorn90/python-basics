# 논리연산자
# 피연산자(operand): 일반적으로 True 또는 False 값을 가지는 연산.
a = 20
print(not a < 20)
print(a < 30 and a != 30)
print(a == 30 or a > 30)

# 논리식의 계산순서
print(True or bool('logical'))
print(True or 'logical')        # or 연산자를 사용했을 때 앞의 값이 이미 true이기 떄문에 뒤를 보지 않음
print(False or 'logical')       # or 연산자, 앞의 값 false이기 때문에 뒤를 꼭 봐야함.
print([], 'logical')
print([2, 10], and 'logical')

def f():
    print('hello workld')

a = 20
if a > 10:
    f()
a > 10 or f()



s = 'Hello World'
s and print(s)
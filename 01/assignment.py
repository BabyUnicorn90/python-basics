
# 치환문

a = 1             # 1이라는 값이 할당, a라는 이름으로 명명, a라는 이름으로 접근 可
b = a + 1
print(a, b)


# 할당 값 오류

# 1 + c = a         # 연산자는 방향이 있다!


e = 3.5; f = 5.3      # 치환문을 ;으로 구분할 수 있지만 not recommended
print(e, f)

e, f = 3.8, 8.3       # 여러 개를 한번에 치환 可
print(e, f)


x = 30
y = 30
z = 30
x = y = z = 30        # 같은 값을 여러 변수에 할당 可
print(x, y, z)



# swap

x = 10
y = 20
print('====swap====')
print(x, y)




# 동적 타이핑(실행 중에 변수의 타입을 결정)

a = 1
print(type(a))

a = 'hello'
print(type(a))

a = 3.14
print(type(a))

a = True
print(type(a))


# 확장 치환문
a = 10
a= a+10

print(a)

a+= 10

print(a)
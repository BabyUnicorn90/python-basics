# 생성
t = ()      # 공튜플
t = (1, )   # 항목이 하나인 튜플을 표현할 때: 반드시 ,를 사용하여 일반연산()과 구분될 수 있도록 한다.
t = (1, 2, 3)

print(t, type(t))


print('\n')
print('------------sequence 타입의 특징--------------')
print('\n')


#인덱싱
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

#slicing
print(t[1:3])
print(t[:])

#반복
t2 = t * 2
print(t2)

#연결
t3 = t + (4, 5, 6)
print(t3)

#길이
print(len(t3))

#in, not in
print(4 in t3)
print(10 not in t3)

#tuple은 변경 불가!! (immutable)
try:
    t4 = ('apple', 'banana', 10, 20)
    t4[2] = 90        #에러
except TypeError as e:
    print('튜플은 변경불가 - immutable')

#tuple을 이용한 여러값의 대입
x, y, z = 10, 20, 30
print(x, y, z)

#tuple을 이용한 여러 값의 치환
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)


print('\n')
print('------------객체함수--------------')
print('\n')

t5 = (20, 30, 40, 50, 20)
print(t5.index(50))
print(t5.count(20))


#tuple을 set으로 변환하기
s = set(t5)
print(t5)

#tuple을 list로 변환하기, list를 다시 tuple로 변환하기
l = list(t5)
l.insert(0,10)
print(l, type(l))

t5 = tuple(l)
print(t5)

t5 = tuple(set(t5))     #중복제거하기
print(t5)





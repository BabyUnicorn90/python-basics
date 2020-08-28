# 생성
s = {1, 2, 3}
print(s, type(s))

# 기본연산
print(len(s))
print(2 in s)
print(10 not in s)

# list의 중복성을 제거할 수 있다.
l = [1, 2, 3, 4, 2, 2, 5, 6, 5, 6]

s2 = set(l)
print(s2)

print('\n')
print('--------객체함수------------')
print('\n')

s3 = set()     # 빈 set 표현: set()   <--- {}라고 하지말것. dictionary와 혼동 可
s3.add(7)
print(s3)

s3.add(2)
print(s3)

s3.add(6)
print(s3)

s3.discard(2)
print(s3)

s3.remove(7)
print(s3)

try:
    s3.remove(10)
except KeyError as e:
    print('remove는 discard와 다르게 존재하지 않는 요소 제거시 예외 발생')

s3.update({2, 4, 6})
print(s3)

s3.clear()
print(s3)

print('\n')
print('--------수학의 집합과 관련된 함수------------')
print('\n')

s4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s5 = {10, 20, 30}

s6 = s4.union(s5)    # 합집합 구하기
print(s6)

s7 = s4.intersection(s5)    # 교집합 구하기
print(s7)

s8 = s4.difference(s5)    # 차집합
print(s8)

s9 = s4.symmetric_difference(s5)   # 대칭차집합
print(s9)


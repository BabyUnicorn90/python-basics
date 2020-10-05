# 생성
l1 = []
l2 = [1, True, 'python', 3.14]

print('===sequence 타입의 특징===')
# 인덱싱(sequence 타입의 특징)
print(l2[0], l2[1], l2[2], l2[3])
print(l2[-4], l2[-3], l2[-2], l2[-1])

# slicing
print(l2[1:4])
l3 = l2
l4 = l2[:]              # 새 리스트 복사
print(l3)

print(l2[1:4])
print(l2[:])
print(l2[2:])
print(l2[3::-1])
print(l2[len(l2)::-1])


# 반복(sequence 타입의 특징)
l3 = l2 * 2
print('리스트 반복: ', l3)

#연결(sequence 타입의 특징)
l4 = l2 + [1, 2, 3]
print('리스트 연결: ', l4)

# 길이 (sequence 타입의 특징)
print('리스트 길이확인: ', len(l4))

# in, not in (sequence 타입의 특징)
print('요소 포함여부 확인: ', 5 not in l4)
print('요소 포함여부 확인2: ', 'python' in l4)

# 삭제 (변경 가능한 객체)
del l4[2]
print('삭제 후 확인: ', l4)

# 변경가능한 객체
l5 = ['apple', 'banana', 10, 20]
print('l5 원본: ', l5)
l5[2] = l5[2] + 90
print('l5 변경 후: ', l5)


print('<<<<<<<<<<<<<<slicing 기법>>>>>>>>>>>>>>>>>>>')
# slicing을 이용한 삭제
l6 = [1, 12, 123, 1234]
print(l6)

l6[0:] = []
print(l6)

# slicing을 이용한 삽입
l7 = [1, 12, 123,1234]

# 중간삽입
l7[1:1] = [123]
print(l7)

# 마지막삽입
l7[5:] = [123456]
print(l7)

# 처음삽입
l7[:0] = [0]
print(l7)

# slicing을 이용한 치환
l8 = [1, 12, 123, 1234, 12345]
print(l8)

l8[0:2] = [10, 20]
print(l8)



# 객체함수를 이용한 중간삽입: .insert(,)
l9 = [1, 3, 4]

l9.insert(1,2)     # 1자리에 2를 넣겠다
print(l9)

# 객체함수를 이용한 마지막삽입: .append()
l10 = [1, 3, 4]
l10.append([5, 6])
print(l10)

# 객체의 함수는 자기자신을 변형하는 메소드.

# .reverse()

# .remove()  --자리가 아니라 값을 삭제함. 동질성 비교.
# 작동원리: () "is" .앞의 리스트 안에 있는 객체 ? -y: 삭제

# .extend() --.append()는 하나만

# stack: insert X, append 可    <- "push"
# stack 가져오기: 인덱스([])로 가져오기 X, (스텍이름)[len(스텍이름)-1]. 가져오면서 빠짐  <- "pop"
# 다시말해, stack은 뒤로만 추가, 제일 뒷 값만 가져올 수 있는 자료형 (FILO)
# stack 활용 용도: 계산기,

# queue: 먼저 들어간 값이 먼저 출력됨 (FIF0)

# .sort() --오름차순 정리
# .sort(key=str)  --기준을 지정할 수 있다.
# cf. sorted --전역함수. 알고리즘을 넣을 수 있다.
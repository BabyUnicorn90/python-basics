

# for ~ in (시퀀스 객체: 스트링, 리스트, 튜플)
for number in [10, 20, 30, 40]:
    result = number ** 2
    print(result, end = '\t')


print('\n')


a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end = '\t')


print('\n')



j = [('둘리', 10), ('마이콜', 30), ('또치', 11)]
for t in j:
    print('이름: %s, 나이: %d'% t, end = '\t')


print('\n')


# 10번 반복하는 loop 만들기
for i in range(0, 10):
    print (i, end='\t')


print('\n')


# 1 ~ 10 합 구하기

for x in range(1, 11):
    y = x + 1
    z = x + y
    print(z)


print('\n')


s = 0
for n in range(1, 11):
    s += n
print(s)


print('\n')



# break
for n in range(10):
    if n > 5:
        break                        # 비정상적으로 종료하는 것. 뒤에 else 구문이 있다면 활성화 X
    print(n, end='\t')


print('\n')


# continue
for n in range(10):
    if n <= 5:
        continue
    print(n, end='\t')


print('\n')


# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print("%d x %d = %d" % (i, j, i*j))
    print('-----------')


print('\n')


# 구구단2
for i in range(1, 10):
    for j in range(1, 10):
        print("{0} X {1} = {2}".format(j, i, i*j), end="\t")
    else:
        print(' ')


print('\n')


# 삼각형 만들기
for i in range(1,10):
    print('*' * i)


print('\n')


# 역삼각형 만들기
for i in range(10, 0, -1):
    print('*' * i)



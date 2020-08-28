# 생성
d = {'basketball':5, 'baseball':9}
print(d, type(d))

d2 = {}
print(d2, type(d2))

d3 = dict()
print(d3, type(d3))

d4 = dict(one=1, two=2, three=3, five=5)
print(d4, type(d4))

d5 = dict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
print(d5, type(d5))

# index 대신에 key로 값에 접근한다.
print(d['basketball'])

# 크기확인: len
print(len(d))

# key 값의 존재여부 확인: in, not in
print('soccer' not in d)
print('baseball' in d)

# 다양한 타입의 key를 사용할 수 있다. --but key는 변경불가능한 값을 사용해야함
d6 = {}
print(d6)

d6['twenty'] = 20       #key 값으로 str
d6[True] = 'true'       #key 값으로 bool
d6[10] = 10             #key 값으로 int
print(d6)

# 리스트를 key값으로 한다면?
# d6[[1, 2, 3]] = 6           -unhashable type 에러
# hashing: 모드 값을 하나의 int의 값으로 바꾸는 것.
# key 값을 찾을때 int로 찾는 것이 유리 -간단, 빠름.


print('\n')
print('-----------객체함수---------------')
print('\n')

k = d6.keys()
print(k, type(k))
for key in k:
    print(key, d6[key])


v = d6.values()
print(v, type(v))
for value in v:
    print(value)


items = d6.items()
print(items, type(items))
for item in items:
    print(item)


phones = {'마이콜':'000-0000-0000', '둘리':'111-1111-1111', '또치':'222-2222-2222'}
print(phones['둘리'])
print(phones.get('둘리'))


# .get() 객체함수를 사용하는 이유: 값 객체가 없는 경우 none을 반환받을 수 있기 떄문.
#print(phones['도우너'])
v = phones.get('도우너')
if v is None:
    print('도우너 키를 가진 값은 없습니다.')


# set_default
v. phones.set_default('둘리', '555-5555-5555')
print(v)


print(phones)
v = phones.pop('둘리')
print(v)
print(phones)



# popitem(): 삭제와 동시에 (키, 값) 출력
item = phones.popitem()
print(item)
print(phones)

# clear()

# 조회
d7 = {'c': 3, 'a': 1, 'b': 2}

for key in d7:
    print(key, end=' ')
print('\n')


for key, value in d.items():
    print(key, value)

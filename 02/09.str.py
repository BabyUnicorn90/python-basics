

s = ''
str1 = 'Hello World'
str2 = "Hello World"
print(type(s), type(str1), type(str2))
print(isinstance(str1, str))

# 여러 줄 문자열
str3 = 'ABC\nDEF\n가나다라마바사\n아자차카타파하'
print(str3)

str4 = '''ABC
DEF
가나다라마바사
아자차카타파하'''
print(str4)



# escape
print('hello\nworld\n')




# print('======== 문자열 연산 ==========)



# 반복




# +: 연결. concatenate   <<<<<<<<<<<<<<<<<<<<<





# slicing
# 문자열 객체와 정수 객체는 연결(+)로 연산 不 -예외 有



# 시퀀스 타입이 가지는 특징: len(), in, not in


print('==========포맷팅============')
# tuple로 포맷팅
print("name: %s, age: %d" % ('둘리', 10))


# dict으로 포맷팅
print("name: %(name)s, age:%(age)d" % {'name': '둘리', 'age': 10})


# format() 함수1 --전역함수
name = '마이콜'
age = 30
print("name: " + format(name, 's') + ", age: " + format(age, 'd'))


# format() 함수2 --객체함수
print("name: {0}, age:{1}".format(name, age))    # {}안을 공란으로 둬도 괜찮다.
print('name: {n}, age: {a}'.format_map({'n': name, 'a': age}))



print('==========객체함수============')
# 대소문자
s8 = 'i like python'
print(s8.upper())
print(s8.lower())
print(s8.swapcase())
print(s8.capitalize())

#
s9 = '1234567'
print(s9.isdigit())

# 검색
s10 = 'I Like Python, I Like Java Also'
print(s10.count('Like'))
print(s10.find('Like'))
print(s10.find('Like', 5))
print(s10.find('JavaScript'))          # 찾는 문자열이 없을때: -1 리턴
print(s10.rfind('Like'))
print(s10.startswith('I Like'))          # T, F로 리턴
print(s10.startswith('I LIKE',2))
print(s10.endswith('also'))
print(s10.endswith('also', 2, 26))


# index()는 발견하지 못하면 예외 발생 = 정지
index = s9.find('JavaScript')
if index == -1:
    print('not found')



# 예외처리  --로직에 예외처리를 사용하는 것을 권장하진 않음. 예외처리는 DB처리 과정에서 네트워크가 끊어졌을 경우 대비하여 사용하는 것. (예외는 복구할 수 없음)
# 예외 발생시: 1. 로그를 남긴다(파일로 저장할 수 있도록)   2. 사용자에게 사과문구     3. 정상종료

try:
    print(s10.startswith('I Like'))        # T, F로 리턴
    s9.index('JavaScript')
except ValueError:
    print('예외처리')


# 편집과 치환

# 공백제거: strip()  (원래 전산용어로는 'trip'이라 함)
# 양쪽 끝 공백만 제거. 문자열 가운데의 공백은 제거 X. replace X.
# strip()에 특정 문자열을 주면 공백 대신 ()안의 문자열 제거.
# strip() 활용 케이스: 사용자 pw에 임의로 쳐지는 공백이 있을 경우를 대비해 제거하는 코드를 넣어둬야 할 때
s11 = '   spam and ham    '
print('-----' + s11.strip() + '-----')
print('-----' + s11.rstrip() + '-----')
print('-----' + s11.lstrip() + '-----')

s12 = '<><abc><><defg><>'
print('------'+s12.strip('<>')+'-------')      # s12 끝에 있는 <와 >를 제거

s13 = 'Hello Java Java Java'
print('-----'+s13.strip('Java')+'-----')
print('-----'+s13.replace('Java', 'Python')+'-----')


# 정렬
s14 = 'King and Queen'
print('-----' + s14.center(30) + '------')
print('-----' + s14.ljust(30) + '------')
print('-----' + s14.rjust(30) + '------')

# 분리
s15 = 'spam and ham'
r = s15.split(' and ')      # 분리자
print(r, type(r))           # 함수의 리턴값이 다수일 때는 자동적으로 리스트를 만듦

s16 = 'one:two:three:four'
r = s16.split(':')
print(r)

r = s16.split(':', 2)
print(r)

r = s16.rsplit(':', 2)
print(r)

lines = '''1st line
2nd line
3rd line
4th line
'''

r = lines.split('\n')
print(r)

r = lines.splitlines()       # 빈 스트링은 없애버린다.
print(r)


# 결합
s = '&'.join(r)
print(s16)


# 판별
print("1234".isdigit())
print('abcd'.isdigit())
print("abcd".isalpha())
print("1234".isalpha())
print('abcd'.islower())
print('1234'.islower())
print("Abcd".isupper())
print("".isspace())
print(" ".isspace())
print('\n'.isspace())
print('\t'.isspace())


# '0' 채우기
number = 234
print(str(number).zfill(5))

# str 객체는 변경 不 (불변성. immutable)
s14 = 'hello'
s14[0] = 'f'
print(s14)

#cf. 리스트는 변경 可 (가변성. mutable)
ㅣ1 = ['hello', 'world']
l1[0] = 'H'
print(l1)
l1.append('Python')
print(l1)


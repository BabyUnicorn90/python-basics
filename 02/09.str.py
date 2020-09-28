# 한 줄 문자열
s = ''
str1 = 'Hello World'
str2 = "Hello World"
print(type(s), type(str1), type(str2))
print(isinstance(str1, str))

# 여러 줄 문자열
str3 = 'ABC\nDEF\n가나다라마바사\n아자차카타파하'
print(str3)

# 여러 줄 주석 --여러 줄 문자열
str4 = '''ABC
DEF
가나다라마바사
아자차카타파하'''
print(str4)

# escape
print('hello\nworld\n')

# print('======== 문자열 연산 ==========)
s1 = 'First String'
s2 = 'Second String'

#str 역시 순차 자료형의 특징을 가지고 있다.
#불변객체 -인덱스접근 가능 but 인덱스치환 不
# 반복
s3 = s1 * 3
print('s3:', s3)



# +: 연결. concatenate
s4 = s1 + ' ' + s2
print('s4: ', s4)

s5 = 'Hello' + '-' + 'World'
s6 = 'Hello' '-' 'World'    #기호 생략 가능
print('s5(+기호 사용): ', s5, '\n'
      's6(+기호 생략): ', s6)

# 문자열 객체와 정수 객체는 연결(+)로 연산 不 -예외 有
# print("hello" + 2)   #-----error!
print('문자열 객체와 정수객체 + 연결 不: ', "hello" + str(2))

#<시퀀스 타입이 가지는 특징 1> slicing
# F   i   r   s   t    S  t  r  i n  g
# 0   1   2   3  4  5  6  7  8  9 10 11
#-12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 `

#정방향 슬라이싱
print('정방향 슬라이싱: ', s1[0], s1[1], s1[2])
#역방향 슬라이싱
print('역방향 슬라이싱: ', s1[-12], s1[-11], s1[-10])       # <<<<<<< 확인해보기

#<시퀀스 타입이 가지는 특징 2> indexing



#<시퀀스 타입이 가지는 특징 3> len()
print('s1의 길이: ', len(s1))

#<시퀀스 타입이 가지는 특징 4> in
#<시퀀스 타입이 가지는 특징 5> not inn
#<시퀀스 타입이 가지는 특징 6> not in




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
#익명 플레이스홀더
print("name: {}, age: {}".format(name, age))
#numbered placeholder
print("name: {0}, age:{1}".format(name, age))
print("name: {1}, age:{0}".format(age, name))
#named placeholder --사전을 포맷할 때는 format_map메서드 이용    <<<<<<사전포맷???
print('name: {n}, age: {a}'.format_map({'n': name, 'a': age}))

print('==========객체함수============')
#대소문자
s8 = 'i like Python'
print('모두 대문자로: ', s8.upper())
print('모두 소문자로: ', s8.lower())
print('대문자는 소문자로, 소문자는 대문자로: ', s8.swapcase())
print('문장 첫 글자만 대문자: ', s8.capitalize())
print('각 단어의 첫글자만 대문자: ', s8.title())

#
s9 = '1234567'
print(s9.isdigit())

# 검색    <<<<<<< 추가복습 필요
s10 = 'I Like Python, I Like Java Also'
print(s10.count('Like'))
print('처음부터 검색하기: ', s10.find('Like'))
print('처음부터 검색, 검색범위 제한: ', s10.find('Like', 5))
print(s10.find('Like', 21)) # 찾는 문자열이 없을때: -1 리턴
print(s10.find('JavaScript'))
print('역방향 검색: ', s10.rfind('Like'))  #역방향 검색을 했다고 해서 역방향 인덱스가 출력되지는 않는다.
print('문장의 시작 검색: ', s10.startswith('I Like'))          # T, F로 리턴
print(s10.startswith('I LIKE', 2))
print('문장의 끝 검색: ', s10.endswith('also'))
print('2~26구간의 문자열 끝 검색: ', s10.endswith('also', 2, 26))

#find와 index의 차이점:
#find: 예외발생 없음
#index: 예외발생 있음

# index()는 발견하지 못하면 예외 발생 = 정지
index = s10.find('JavaScript')
if index == -1:
    print('not found')

# 예외처리  --로직에 예외처리를 사용하는 것을 권장하진 않음.
# 예외처리는 DB처리 과정에서 네트워크가 끊어졌을 경우 대비하여 사용하는 것. (예외는 복구할 수 없음)
# 예외 발생시: 1. 로그를 남긴다(파일로 저장할 수 있도록)   2. 사용자에게 사과문구     3. 정상종료

try:
    print(s10.rindex('Like'))        # T, F로 리턴
    s10.index('JavaScript')
except ValueError as ex:
    print('index()는 발견하지 못하면 예외가 발생한다.')


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
print('-----'+s13.strip('Java')+'-----')   #제일 오른쪽 끝의 Java만 제거
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
s16 = '&'.join(r)
print('splitlines결과값에 기호(문자열) join하기: ', s16)


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
print('0으로 채우기: zfill(): ', str(number).zfill(5))   #높은 자리수부터 0으로 채움

# str 객체는 변경 不 (불변성. immutable)
s14 = 'hello'
# s14[0] = 'f'    -----error!
print('s14: ', s14)

#cf. 리스트는 변경 可 (가변성. mutable)
l1 = ['hello', 'world']
print('l1 원본: ', l1)
#1번째 요소 변경
l1[0] = 'H'
print('l1[0] 변경: ', l1)
#요소 추가
l1.append('Python')
print('l1 추가: ', l1)


#docstring:
def docstr():
    """
    파이썬은
    모듈의 상단, 클래스, 함수의 선언부 바로 아래에
    간단한 설명을 적으면 docstring이 된다."""

#docstring의 확인: 객체.__doc__
print(docstr.__doc__)

#docstring의 확인2: .help()
help(docstr)


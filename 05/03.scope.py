def func1(a):              #func1를 사용할 때 실행, a가 로컬영역의 심볼테이블에 생성 (func1이 사용될 때의 참조주소값)
    x = 10                 #x값이 할당과 동시에 로컬영역의 심볼테이블에 생성됨
    return a + x           #x값이 로컬영역에 있으므로 로컬영역 사용


def func2(a):               #func2를 사용할 때 실행, a가 로컬영역의 심볼테이블에 생성
    return a + x            #func2 의 local 영역에서 x의 할당이 일어나지 않았으므로 x값은 global 영역에서 찾음


def func3(a):
    global g                #글로벌영역의 g
    g = 3                   #글로벌영역의 g를 바꿈 --if/ global g 없이 g = 3이었다면 로컬영역에서 g를 생성, 이 g는 글로벌g와 다름
    return a + g


x = 1
g = 10

# (L)GB
r = func1(10)
print(r)
print(x)

# L(G)B
r = func2(10)
print(r)

# LG(B)
print(dir('__builtins__'))

# global 키워드
r = func3(10)
print(r)
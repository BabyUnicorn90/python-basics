

# 문제8. 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

# 문제해결

s1 = str(input('입력하세요: '))
def reverse(s):
    return ''.join(reversed(s))

print(reverse(s1))
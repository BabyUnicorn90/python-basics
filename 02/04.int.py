a = 23
a = 20 + 3

print(a, type(a))
print(isinstance(a, int))



# 2진수, 10진수, 8진수, 16진수
b = 0b1101     # 2진수 표현: 0b~
c = 0o23       # 8진수 표현: 0o~
d = 0x23       # 16진수 표현: 0x~

print(b)
print(c)
print(d)

e = 2 ** 1024
print(e, type(e))
print(e.bit_length())



# 변환함수
print(bin(38))    # 10진수를 2진수로 변환
print(oct(38))    # 10진수를 8진수로 변환
print(hex(38))    # 10진수를 16진수로 변환





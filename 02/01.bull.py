# Bool: 참(true)이나 거짓(false)을 나타내는 값. T, F 두 값(리터럴)만 가짐

a = 1
print(a > 1)
print(a < 10)

b = a > 1
print(b, type(b))

print(b + 1)
# b가 bool타입이긴 하지만 연산식에서는 int값으로 평가 (True는 1, False는 0)
print(True * False)



# 조건식에서 쓰임



# 다른 타입의 객체도 bool 타입으로 형반환이 가능
print(bool(10), bool(0))
print(bool(3.14), bool(0))
print(bool("hello"), bool(' '))
print(bool([0, 1]), bool([]))
print(bool((0, 1)), bool(()))
print(bool({'k1':'v1', 'k2':'v2'}). bool({}))
print(bool(none))


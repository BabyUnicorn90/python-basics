# 문제6. 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.
# 입력값: 67879원


m = 67879
a = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
b = []

x = m // 50000
y = m % 50000
b.append(x)

x = y // 10000
y = y % 10000
b.append(x)

x = y // 5000
y = y % 5000
b.append(x)

x = y // 1000
y = y % 1000
b.append(x)

x = y // 500
y = y % 500
b.append(x)

x = y // 100
y = y % 100
b.append(x)

x = y // 50
y = y % 50
b.append(x)

x = y // 10
y = y % 10
b.append(x)

x = y // 5
y = y % 5
b.append(x)

x = y // 1
y = y % 1
b.append(x)


print(b)



# 문제6. 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.
# 입력값: 67879원

# still working on

money = int(input('수를 입력하세요: '))
unit = ([50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
result = []

for i in unit:
    money = money // int(unit)
    result.append(money)
    print(result)


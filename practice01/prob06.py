
# 문제6. 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.
# 입력값: 67879원

# 문제해결

import sys

try:
    money = int(input('금액을 입력하세요: '))
except ValueError:
    print("숫자를 입력하지 않았습니다.")
    sys.exit()


unit = ([50000, 10000, 5000, 1000, 500, 100, 50, 10, 1])
result = []

for i in unit:
    count = money // int(i)
    money = money % int(i)
    result.append(count)
print("오만원권: {0}장, "
      "만원권: {1}장, "
      "오천원권: {2}장, "
      "천원권: {3}장, "
      "500원: {4}개, "
      "100원: {5}개, "
      "50원: {6}개, "
      "10원: {7}개, "
      "1원: {8}개".format(*result))


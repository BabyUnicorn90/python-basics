# 문제10 숫자를 입력받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

# a.입력 받은 숫자가 홀수인 경우에는, 0부터 입력값까지 홀수의 합을 출력합니다.
# 예제: 입력이 7이면 16을 출력(1 + 3 + 5 + 7 = 16 )

# b.입력받은 숫자가 짝수인 경우에는, 0부터 입력값까지 짝수의 합을 출력합니다.
# 예제: 입력이 10이면 30을 출력(2 + 4 + 6 + 8 + 10 = 30 )


#문제해결

import sys

input_num = 0
try:
    input_num = int(input('숫자를 입력하세요: '))
except ValueError:
    print('Error: 숫자를 입력하지 않았습니다.')
    sys.exit()

if input_num % 2 == 0:
    even_list = []
    for i in range(0, input_num+2, 2):
        even_list.append(i)
    print(sum(even_list))
else:
    odd_list = []
    for j in range(1, input_num+2, 2):
        odd_list.append(j)
    print(sum(odd_list))

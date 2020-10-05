# 문제 7. 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

#문제 해결

count = 1
user_list = []
while count < 6:
    user_input = int(input('5개의 정수를 입력하세요:'))
    user_list.append(user_input)
    count += 1

print('입력받은 5개 정수:', user_list)

average_of_user_list = sum(user_list) / 5
print('입력받은 5개 정수의 평균: ', average_of_user_list)


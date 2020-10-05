# 문제9. 주어진 if 문을 dict를 사용해서 수정하세요.

# menu = input('메뉴: ')

# if menu == '오뎅':
#     price = 300
# elif menu == '순대':
#     price = 400
# elif menu == '만두':
#     price = 500
# else:
#     price = 0

# print('가격: {0}'.format(price))


#dict를 사용해서 수정하라???

import sys

input_menu = str(input('메뉴를 입력하세요(오뎅, 순대, 만두): '))

menu_dic = {'오뎅':300, '순대':400, '만두':500}

price = 0
for menu in menu_dic:
    if menu == input_menu:
        price = menu_dic[menu]

if price == 0:
    print('메뉴없음')
else:
    print('{}의 가격: {}'.format(input_menu, price))
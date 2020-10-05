index = 0                                                       #외부에 변수 두기!
for color in ['red', 'yellow', 'blue', 'black', 'grey']:
    #내부값은 알 수 있지만 실제 인덱스는 알 수 없음.
    print(index, color)
    index = index + 1

# enumerate함수로 묶으면 (인덱스, 값)의 튜플로 전달됨
for item in enumerate(['red', 'yellow', 'blue', 'black', 'grey']):
    print(item)

# 외부변수없이: enumerate
for index, color in enumerate(['red', 'yellow', 'blue', 'black', 'grey']):
    # 전달받은 튜플을 언패킹
    print(index, color)

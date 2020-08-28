index = 0                                                       #외부에 변수 두기!
for color in ['red', 'yellow', 'blue', 'black', 'grey']:
    print(index, color)
    index = index + 1

# 외부변수없이: enumerate
for index, color in enumerate(['red', 'yellow', 'blue', 'black', 'grey']):
    print(index, color)



# 문제4. 다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)

# 풀이완료

for i in range(1, 10):
    for j in range(1, 10):
        print("%d X %d = %d" % (j, i, i*j), end='\t')
    print('')
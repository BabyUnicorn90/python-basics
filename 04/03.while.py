# 1~10 합 구하기

s = 0
for n in range(1, 11):
    s += n
print(s)


count = 0
while count < 10:
    count += 1
    print(count)

count = 0
while count < 10:
    print(count)
    count += 1



s = 0
count = 0
while count < 10:
    s += (count)
    count += 1
print(s)



# Break 문
for n in range(10):
    if n > 5:
        break
    print(n, end=' ')

i = 0
while i < 10:
    if i > 5:
        break
    print(i, end=' ')
    i += 1

print('\n')




# Continue 문   --무한루프에 빠질 수 있으므로 조심할것!
for n in range(10):
    if n <= 5:
        continue
    print(n, end=' ')

# 무한루프에 빠짐
# i = 0
# while i < 10:
#     if i <= 5:
#         continue
#     print(i, end='')
#     i += 1

i = 0
while i < 10:
    if i <= 5:
        i += 1
        continue
    print(i, end=' ')
    i += 1

print('\n')

# 무한루프

# while True:
#     print('infinite loop')

i = 0
while True:
    print(i, end=' ')
    if i > 5:
        break
    i += 1

# while True:
#     print('infinite loop')

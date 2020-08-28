numbers = [1, 2, 3, 4, 5, 6, 7, 8]
results = []
# 1
for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    result = n * n
    results.append(result)

print(results)


# 2
results = [num * num for num in numbers]
print(results)




# 문자열 리스트에서 길이가 2이하인 문자열만 새로운 리스트에 넣기
#1
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
results = []
for s in strings:
    if len(s) <= 2:
        results.append(s)
print(results)

#2
reslts = [s for s in strings if len(s) <= 2]
print(results)




# 1~100사이의 수 중 짝수 리스트 만들기
results = [n for n in range(1, 101) if n % 2]
print(results)



# 문자열 리스트에서 각각의 문자열의 길이를 담은 리스트 만들기.
results = [len(s) for s in strings]
print(results)




# 3, 6, 9게임: 1~100사이의 수 중 3. 6. 9가 있는 수 리스트 만들기.
[n for n in rage(1, 101)]

results = [number for number in range(D, 101)] if str(number).count()in range((1' 10'))





# set comprehension


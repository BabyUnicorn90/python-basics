# zip() 사용 예:

seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)
print(z, type(z))


for t in z:               #튜플로 만들어준다.
    print(t)



# for index, t in enumerate(z):
#     print(index, t)
#
# for a, b in z:
#     print(a, b)

# for문 순회를 한번 하고나면 앞으로 되돌릴 수 없다.


z = zip(seq1, seq2)
for index, t in enumerate(z):
    print(index, t)


z = zip(seq1, seq2)
for a, b in z:
    print(a, b)


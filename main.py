n = int(input())
a = []
count = 0
s = 0

for i in range(n):
    a.append(int(input()))
    if a[i] == 0:
        a.pop()
        n = len(a)
        break
print(a)

for i in range(n):
    if a[i] % 8 == 0:
        count += 1
        s += a[i]

if count == 0:
    print('NO')
else:
    print(s / count)

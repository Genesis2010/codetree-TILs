a = list(map(int, input().split()))

for i in range(2, 10):
    temp = (a[i-2] + a[i-1])%10
    a.append(temp)

for i in a:
    print(i, end=" ")
number = int(input())
lis = list(map(int, input().split()))

answer = False
for i in range(1, number):
    if lis[i] < 0 and lis[i - 1] < 0:
        answer = True
    elif lis[i] >= 0 and lis[i - 1] >= 0:
        answer = True

if answer:
    print("YES")
else:
    print("NO")

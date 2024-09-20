number = int(input())
lis = list(map(int, input().split()))

result = []
for element in lis:
    if element % 2 == 0:
        result.append(element)
print(*result)

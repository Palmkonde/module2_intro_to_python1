number = int(input())
lis = list(map(int, input().split()))

result = []
for i, element in enumerate(lis):
    if i % 2 == 0:
        result.append(element)
print(*result)

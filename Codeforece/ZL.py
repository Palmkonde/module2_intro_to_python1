number = int(input())
lis = list(map(int, input().split()))
already = []

count = 0
for element in lis:
    if not element in already:
        count += 1
        already.append(element)
print(count)

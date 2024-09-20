number = int(input())
lis = list(map(int, input().split()))
number_to_plus = int(input())

result = []
for i in range(number):
    result.append(lis[i] + number_to_plus)

print(*result)

# print(*list(map(lamba x: x + number_to_plus, lis)))

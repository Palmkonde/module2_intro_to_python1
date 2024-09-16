number = int(input())

result = (number * (number + 1)) // 2

for i in range(number - 1):
    user_number = int(input())
    result -= user_number

print(result)

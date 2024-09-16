number = int(input())

zeros = 0

for i in range(number):
    user_number = int(input())
    zeros += (user_number == 0)

print(zeros)

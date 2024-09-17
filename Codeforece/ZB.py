s1 = input()

block = len(s1)
middle_of_block = block // 2
result = s1[middle_of_block - 1: middle_of_block + 2]

print(result)

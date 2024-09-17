s1 = input()

mid = len(s1)//2
part_1 = s1[:mid]
part_2 = s1[mid:]

result = part_2 + part_1
print(result)

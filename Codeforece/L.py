chest_a = int(input())
chest_b = int(input())
chest_c = int(input())

result = (chest_a + chest_b + chest_c) - min(chest_a, chest_b, chest_c)

print(result)

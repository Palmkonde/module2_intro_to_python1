string1 = input()
little_string1 = input()

position = len(string1) // 2

result = string1[:position] + little_string1 + string1[position:]

print(result)

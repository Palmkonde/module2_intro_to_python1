user_input = input()
character = ""

for i in user_input:
    character += i + "_"
    print(character)


print(character[:-1])

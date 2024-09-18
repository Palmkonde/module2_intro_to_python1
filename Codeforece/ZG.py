string = input()

for i, character in enumerate(string):
    if i == len(string) - 1:
        print(character)
    else:
        print(character, end="_")

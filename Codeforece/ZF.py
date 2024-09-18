string = input()

reverse_string = ""

for i in range(len(string) - 1, -1, -1):
    reverse_string += string[i]

if string == reverse_string:
    print("YES")
else:
    print("NO")

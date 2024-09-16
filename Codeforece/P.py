score = int(input())

if 0 <= score <= 40:
    print("Emerging")
elif 41 <= score <= 80:
    print("Developing")
else:
    print("Achieved")

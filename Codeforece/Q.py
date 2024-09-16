apple = int(input())
orange = int(input())
first_bag = int(input())
second_bag = int(input())

if max(first_bag, second_bag) >= max(apple, orange) and min(first_bag, second_bag) >= min(apple, orange):
    print("YES")
else:
    print("NO")

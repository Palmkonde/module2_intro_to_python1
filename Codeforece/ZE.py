string = input()

alice = string.count("A")
bob = string.count("B")

if alice > bob:
    print("ALICE")
elif bob > alice:
    print("BOB")
else:
    print("DRAW")

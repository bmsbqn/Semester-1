print(" " * 7 + "*")
for i in range(1, 7 + 1):
    print(" " * (7 - i), end="")
    for j in range(i):
        print("*", end=".")
    print("*")
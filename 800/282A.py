if __name__ == "__main__":
    x = int(input())

    z = 0
    for i in range(x):
        y = input()
        if y == "X++":
            z += 1
        elif y == "X--":
            z -= 1
        elif y == "++X":
            z += 1
        elif y == "--X":
            z -= 1
    print(z)
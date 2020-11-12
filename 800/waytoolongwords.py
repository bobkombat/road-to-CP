def solve(x):
    if len(x) > 10:
        print("{}{}{}".format(x[0], str(len(x[2:])), x[-1]))
    else:
        print(x)

if __name__ == "__main__":
    x = int(input())

    z = []
    for i in range(x):
        y = input()
        solve(y)
    
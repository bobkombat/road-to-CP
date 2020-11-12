def solve(x):
    if sum(x) > 1:
        return 1
    return 0

if __name__ == "__main__":
    x = int(input())

    z = 0
    for i in range(x):
        y = input().split(' ')
        print(y)
        z += solve([int(i) for i in y])
    
    print(z)
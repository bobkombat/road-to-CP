def solve(z, y):
    x = 0
    _ = 1

    if z[y - 1] > 0:
        x = y
        _ = z[y - 1]
        for i in z[y:]:
            if i == _:
                x += 1
    else:
        for i in z:
            if i >= _:
                x += 1

    
    return x

if __name__ == "__main__":
    _ = input().split(' ')
    x = _[0]
    y = int(_[1])

    z = [int(i) for i in input().split(' ')]
    print(solve(z, y))
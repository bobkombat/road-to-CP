if __name__ == "__main__":
    x = input()
    y = input()

    x1 = 0
    y1 = 0
    for i in range(len(x)):
        if ord(x[i]) >= 97:
            x1 = ord(x[i]) - 97
        else:
            x1 = ord(x[i]) - 65

        if ord(y[i]) >= 97:
            y1 = ord(y[i]) - 97
        else:
            y1 = ord(y[i]) - 65
        
        if x1 > y1 or x1 < y1: 
            break
            
    print(1 if x1 > y1 else 0 if x1 == y1 else -1)
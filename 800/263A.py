def solve(z):
	x = []
	for i in range(5):
		for j in range(5):
			if z[i][j] == '1':
				x = [i, j]
	return abs(2 - x[1]) + abs(2 - x[0])

if __name__ == "__main__":
	z = []
	for i in range(5):
		x = z.append(input().split(' '))

	print(solve(z))

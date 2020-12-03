with open('day3.txt') as f:
    lines = f.read().splitlines()

width = len(lines[0])


def getTrees(right, down):
	trees = 0
	x = 1
	y = 0

	while y in range(0, len(lines)):
		if lines[y][x - 1] == "#":
			trees += 1
		x = (x + right) % width
		y += down

	return trees


print("Trees (right 3, down 1): {}".format(getTrees(3, 1)))

multiplied = getTrees(1, 1) * getTrees(3, 1) * getTrees(5, 1) * getTrees(7, 1) * getTrees(1, 2)
print("Trees multiplied: {}".format(multiplied))
from adventofcode import utils


class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def is_possible(self):
        biggest_side = max(self.sides)
        smaller_sides = self.sides[:]
        smaller_sides.remove(biggest_side)

        return sum(smaller_sides) > biggest_side


def part_one():
    possible = 0
    for triangle in utils.load('3').split('\n'):
        if Triangle([int(side) for side in triangle.split(',')]).is_possible():
            possible += 1

    print("Your puzzle answer is", possible)


def part_two():
    possible = 0
    table = [row.split(',') for row in utils.load('3').split('\n')]
    for x in range(3):
        sides = []
        for y in range(len(table)):
            sides.append(int(table[y][x]))
            if len(sides) == 3:
                if Triangle(sides).is_possible():
                    possible += 1
                sides = []

    print("Your puzzle answer is:", possible)


if __name__ == '__main__':
    part_two()

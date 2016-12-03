from adventofcode import utils


class BlockRouter:

    DIRECTIONS = {"L": -90, "R": 90}
    ANGLE_DIRECTIONS = {0: [0, 1], 90: [1, 0], 180: [0, -1], 270: [-1, 0]}

    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.visited = []
        self.first_intersect = None

    def turn(self, direction):
        self.angle += self.DIRECTIONS[direction]
        if self.angle < 0:
            self.angle += 360
        elif self.angle >= 360:
            self.angle -= 360

    def step(self):
        change = self.ANGLE_DIRECTIONS[self.angle]
        self.x += change[0]
        self.y += change[1]
        coords = (self.x, self.y)
        if coords in self.visited:
            if self.first_intersect is None:
                self.first_intersect = coords
        else:
            self.visited.append(coords)


def part_one():
    block_router = BlockRouter()
    for instruction in utils.load('1').split(", "):
        direction = instruction[0]
        steps = int(instruction[1:])
        block_router.turn(direction)
        for i in range(steps):
            block_router.step()
    print("Your puzzle answer is", abs(block_router.x) + abs(block_router.y))


def part_two():
    block_router = BlockRouter()
    for instruction in utils.load('1').split(", "):
        direction = instruction[0]
        steps = int(instruction[1:])
        block_router.turn(direction)
        for i in range(steps):
            block_router.step()

    first_intersect = block_router.first_intersect
    print("Your puzzle answer is", abs(first_intersect[0]) + abs(first_intersect[1]))


if __name__ == '__main__':
    part_two()

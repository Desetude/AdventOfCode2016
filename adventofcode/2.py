from adventofcode import utils


class KeyPad:
    directions = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}

    def __init__(self, pad, start_x, start_y):
        self.pad = pad
        self.x = start_x
        self.y = start_y

    def process(self, instruction):
        test_y = self.y
        test_x = self.x
        direction = self.directions[instruction]
        test_y += direction[1]
        if test_y < 0:
            test_y = 0
        elif test_y >= len(self.pad):
            test_y = len(self.pad) - 1

        test_x += direction[0]
        if test_x < 0:
            test_x = 0
        elif test_x >= len(self.pad[test_y]):
            test_x = len(self.pad[test_y]) - 1

        if self.pad[test_y][test_x] is not None:
            self.y = test_y
            self.x = test_x


def part_one():
    pad = KeyPad([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 1, 1)

    instruction_set = utils.load('2')
    code = []
    for key_set in instruction_set.split('\n'):
        for instruction in key_set:
            pad.process(instruction)
        code.append(pad.pad[pad.y][pad.x])

    print("Your puzzle answer is", code)


def part_two():
    pad = KeyPad([[None, None, '1', None, None],
                  [None, '2', '3', '4', None],
                  ['5', '6', '7', '8', '9'],
                  [None, 'A', 'B', 'C', None],
                  [None, None, 'D', None, None]],
                 0, 2)

    instructionSet = utils.load('2')
    code = []
    for keySet in instructionSet.split('\n'):
        for instruction in keySet:
            pad.process(instruction)
        code.append(pad.pad[pad.y][pad.x])

    print("Your puzzle answer is", code)


if __name__ == '__main__':
    part_two()

from random import randint
from chess import check_position

def generate_position() -> list[tuple]:
    result = []
    for i in range(8):
        x = randint(1, 8)
        y = randint(1, 8)
        result.append((x, y))
    return result


def print_four_positions():
    i = 0
    while i < 4:
        pos = generate_position()
        if check_position(pos):
            print(pos)
            i += 1


if __name__ == '__main__':
    print_four_positions()
"""
Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""

def check_position(positions: list[tuple]) -> bool:
    for pos in positions:
        x, y = pos[0], pos[1]
        for i in range(1, 9):
            attacked = False
            # generate cells ander attac for queen in current position
            # i don't check bounds but this is ok here
            up_left = True if (x - i, y + i) in positions else False
            attacked = attacked or up_left
            up_right = True if (x + i, y + i) in positions else False
            attacked = attacked or up_right
            down_left = True if (x - i, y - i) in positions else False
            attacked = attacked or down_left
            down_right = True if (x + i, y - i) in positions else False
            attacked = attacked or down_right
            hor_left = True if (x - i, y) in positions else False
            attacked = attacked or hor_left
            hor_right = True if (x + i, y) in positions else False
            attacked = attacked or hor_right
            ver_up = True if (x, y + i) in positions else False
            attacked = attacked or ver_up
            ver_down = True if (x, y - i) in positions else False
            attacked = attacked or ver_down
            if attacked:
                return False
    return True


if __name__ == '__main__':
    good_positions = [(1, 1), (5, 2), (8, 3), (6, 4), (3, 5), (7, 6), (2, 7), (4, 8)]
    print(check_position(good_positions))
    bad_position = [(1, 1), (5, 2), (8, 3), (6, 4), (3, 5), (7, 6), (7, 7), (4, 8)]
    print(check_position(bad_position))


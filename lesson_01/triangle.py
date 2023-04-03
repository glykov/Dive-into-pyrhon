side_a = float(input('Введите длину стороны А: '))
side_b = float(input('Введите длину стороны B: '))
side_c = float(input('Введите длину стороны C: '))

if side_a + side_b <= side_c or side_b + side_c <= side_a or side_c + side_a <= side_b:
    print('Вообще не похоже на треугольник')
    exit()

if side_a != side_b and side_b != side_c and side_c != side_a:
    print('Треугольник разносторонний')
elif side_a == side_b and side_b == side_c and side_c == side_a:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')

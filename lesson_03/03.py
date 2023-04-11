"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант. 
*Верните все возможные варианты комплектации рюкзака
"""
import itertools

things = {
    "spam": 1,
    "eggs": 2,
    "ham": 3,
    "sombrero": 5,
    "maracas": 4,
    "guitar": 6,
    "cornflales": 3
}

max_load = 6

permutations = list(itertools.permutations(things))

solutions = []

for variant in permutations:
    weight = 0
    current_solution = {}
    for item in variant:
        if weight + things.get(item) <= max_load:
            current_solution[item] = things.get(item)
            weight += things.get(item)
    if current_solution not in solutions:
        solutions.append(current_solution)

for solution in solutions:
    print(solution)

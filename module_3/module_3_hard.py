def calculate_structure_sum(data_structure):
    rez = 0
    if isinstance(data_structure, int):
        rez += data_structure
    elif isinstance(data_structure, str):
        rez += len(data_structure)
    elif isinstance(data_structure, list):
        for i in data_structure:
            rez += calculate_structure_sum(i)
    elif isinstance(data_structure, tuple):
        for i in data_structure:
            rez += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            rez += calculate_structure_sum(key) + calculate_structure_sum(value)
    elif isinstance(data_structure, set):
        for i in data_structure:
            rez += calculate_structure_sum(i)

    return rez


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))

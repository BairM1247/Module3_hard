def calculate_structure_sum(data_structure):
    sum_value = 0
    def recursive_sum(structure):
        nonlocal sum_value
        if isinstance(structure, (list, tuple, set)):
            for item in structure:
                recursive_sum(item)
        elif isinstance(structure, dict):
            for key, value in structure.items():
                recursive_sum(key)
                recursive_sum(value)
        elif isinstance(structure, str):
            sum_value += len(structure)
        elif isinstance(structure, int):
            sum_value += structure
        else:
            pass
    recursive_sum(data_structure)
    return sum_value


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)

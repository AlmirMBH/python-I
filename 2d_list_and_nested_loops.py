number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])

new_list = []

for row in number_grid:
    for column in row:
        new_list.append(column)

print(new_list)
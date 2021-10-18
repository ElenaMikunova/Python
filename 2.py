start_list = [1, 2, 3, 555, 75, 4, 2, 2, 4, 6, 100, 1]

new_list = [start_list[i] for i in range(1, len(start_list)) if start_list[i] > start_list[i - 1]]

print(new_list)

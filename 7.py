import json
from functools import reduce
with open("text_7.txt", "r", encoding="utf-8") as start_f:
    my_dict = {}
    income_list = []

    while True:
        content = start_f.readline()
        if not content:
            break
        else:
            my_list = content.split()
            key_list = [''.join(my_list[0])]
            my_num = list(map(int, filter(lambda x: x.isdigit(), my_list)))
            value_list = [reduce(lambda x, y: x - y, my_num)]
            income_list.extend(value_list)
            for_dict = dict(zip(key_list, value_list))
            my_dict.update(for_dict)
    fin_prof = reduce(lambda x, y: x + y,
                      [el for el in income_list if el > 0]) / len([el for el in income_list if el > 0])
    av_income = dict(average_profit=fin_prof)
    main_data = [my_dict, av_income]
    print(main_data)
with open("task_7.json", "x", encoding="utf-8") as new_j:
    json.dump(main_data, new_j)

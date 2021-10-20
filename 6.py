from functools import reduce
with open("text_6.txt", "r", encoding="utf-8") as my_l:
    my_dict = {}
    while True:
        my_list = my_l.readline()
        if not my_list:
            break
        else:
            my_fl = my_list.split()
            key_list = [''.join(my_fl[0].replace(":", ""))]
            split_list = sum(list(x.split('(') for x in my_fl), [])
            my_num = list(map(int, list(filter(lambda x: x.isdigit(), split_list))))
            value_list = [reduce(lambda x, y: x + y, my_num)]
            for_dict = dict(zip(key_list, value_list))
            my_dict.update(for_dict)
    print(my_dict)

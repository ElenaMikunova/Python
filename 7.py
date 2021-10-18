from itertools import count


def fact():
    n = int(input("Введите целое число: "))
    for el in count(1):
        if el <= n:
            yield el
        else:
            break


fact_n = list(fact())
for x in [fact_n]:
    print(x)

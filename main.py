from random import randint

print("Императивный стиль, поскольку используется свои алгоритмы сортировки")


def fast_sort(lst: list) -> list:
    """

    :param lst:
    :return:
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left: list = [x for x in lst if x < pivot]
    middle: list = [x for x in lst if x == pivot]
    right: list = [x for x in lst if x > pivot]
    return fast_sort(left) + middle + fast_sort(right)


rnd_list_1: list[int] = [randint(1, 100) for _ in range(randint(15, 20))]
print(rnd_list_1, end="\n\n")

sorted_arr: list = fast_sort(rnd_list_1)
print(sorted_arr, end="\n\n")

print("Декларативный стиль, поскольку используется готовый алгоритм с \"неизвестной\" реализацией")

rnd_list_2: list[int] = [randint(1, 100) for _ in range(randint(15, 20))]
print(rnd_list_2, end="\n\n")

new_rnd_list: list[int] = sorted(rnd_list_2)
print(rnd_list_2, new_rnd_list, sep="\n", end="\n\n")

rnd_list_2.sort()

print(rnd_list_2, new_rnd_list, sep="\n")

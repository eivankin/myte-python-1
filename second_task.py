from itertools import islice
from random import randint


def weighted_choices(items: list, weights: list, k: int) -> list:
    """
    Сложность: O(N*log(N))
    Память: O(N)

    :param items: список элементов для выбора
    :param weights: список весов элементов
    :param k: число элементов для выбора
    :return: выбранные элементы
    """
    if len(items) != len(weights):
        raise ValueError('количество элементов должно совпадать с количеством весов')
    if len(items) < k:
        raise ValueError('k не должно превышать количество всех элементов')

    # Взвешенное тасование: чем больше вес, тем больше шанс оказаться в начале списка
    # random.random нельзя использовать по условию, поэтому тут 'random.randint(1, 10)'
    order = sorted(range(len(items)),
                   key=lambda i: randint(1, 10) ** (1.0 / weights[i]) if 0 < i < 1 else i)
    return [items[i] for i in islice(order, k)]  # выбор первых k элементов


if __name__ == '__main__':
    print(weighted_choices([1, 3, 4, 3, 9], [.7, .4, .5, .9, .1], 3))

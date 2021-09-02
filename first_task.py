from random import randint


def choices(items: list, k: int) -> list:
    """
    Сложность: O(N)
    Память: O(N)

    :param items: список элементов для выбора
    :param k: число элементов для выбора
    :return: выбранные элементы
    """
    n = len(items)
    if k > n:
        raise ValueError('k не должно превышать количество всех элементов')

    p_copy = items.copy()
    # Тасование Фишера — Йетса
    for i in range(n):
        j = randint(0, i)
        p_copy[i], p_copy[j] = p_copy[j], p_copy[i]
    start = randint(0, n - k - 1)
    return p_copy[start:start + k]


if __name__ == '__main__':
    print(choices([1, 3, 4, 3, 3, 9], 3))

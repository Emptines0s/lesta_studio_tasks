# Исходя из условия задания, нас в первую очередь интересует скорость выполнения алгоритма сортировки.
# Ну, на сколько я помню, из допов по инофрматике, нормальными (оптимизированными) алгоритмами можно назвать quicksort
# и mergesort. Выберу quicksort. Дело в том, что видов сортировок великое множество и, не с проста, ведь их эффективнось
# сильно зависит от входящих данных. Поэтому для сортировки конкретного набора данных, обладающего своей спецификой,
# часто выбирают спецеффический алгоритм. Т.к. в задании ничего не сказанно про массив данных, точнее сказанно, что
# он может быть любым, то я и выбрал универсальный алгоритм, который в среднем показывает хорошие результаты.
from random import choice
from random import sample


# Описание (если надо вообще?): Рекурсивно делим входящий массив на две половинки, относительно случайно выбранного
# элемента. В первой половине элементы < взятого случ. числа, во второй >. Cпускаясь в низ по рекурсии мы доходим до
# списков размером в 1 элемент, они же в свою очередь и отсортированны относительно друг друга.
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        point = choice(nums)
    left = [num for num in nums if num < point]
    print(left)
    right = [num for num in nums if num > point]
    print(right)
    return quicksort(left) + [point] + quicksort(right)


# проверка алгоритма
arr = sample(range(1, 100), 20)
result = quicksort(arr)
print(result)

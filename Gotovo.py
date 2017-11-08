# -*- coding: utf-8 -*-         #сортування вибіркою
import random
import time

def Selection_sort_algorithm(a):
    tm = time.time()
    for i in range(0, len(a) - 1):
        min = a[i]
        min_ind = i
        for j in range(i + 1, len(a)):
            if a[j] < min:
                min = a[j]
                min_ind = j

        a[i], a[min_ind] = a[min_ind], a[i]
    print('сортування вибіркою: {:.3f} сек'.format(time.time() - tm),"список відсортовано =",(a==sorted(a)))
    return a
x = [random.randint(0, 99) for i in range(0, 100000)]
y = [random.uniform(0, 99) for i in range(0, 100000)]



Selection_sort_algorithm(x)
Selection_sort_algorithm(y)


# -*- coding: utf-8 -*- # сотування вставкою
def Iinsertion_sort_algoritm (a):
    tm = time.time()
    for i in range(1, len(a)):
        j = i
        while (j > 0 and a[j] < a[j - 1]):
            a[j], a[j - 1] = a[j - 1], a[j]
            j = j - 1
    print('сортування вставкою: {:.3f} сек'.format(time.time() - tm), "список відсортовано =",(a == sorted(a)))
    return a

Iinsertion_sort_algoritm(x)
Iinsertion_sort_algoritm(y)



# -*- coding: utf-8 -*- #сортування бульбашкою
def Bubble_Sort_algoritm(a):
    tm = time.time()
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print('сортування бульбашкою: {:.3f} сек'.format(time.time() - tm), "список відсортовано =",(a == sorted(a)))
    return a

Bubble_Sort_algoritm(x)
Bubble_Sort_algoritm(y)


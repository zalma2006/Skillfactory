l = [2, 3, 1, 4, 6, 5, 9, 8, 7]


# быстрая сортировка

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)


# сортировка слиянием
def merge_sort(l):
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) // 2
        left = merge_sort(l[:middle])
        right = merge_sort(l[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


left = len(l) // 2
right = len(l) - left
print(qsort(l, left=left, right=right))

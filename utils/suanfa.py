def quick_sort(lists, i, j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= pivot:
            i += 1
        lists[j] = lists[i]
    lists[j] = pivot
    quick_sort(lists, low, i - 1)
    quick_sort(lists, i + 1, high)
    return lists


lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]

quick_sort(lists, 0, len(lists) - 1)

print(lists)

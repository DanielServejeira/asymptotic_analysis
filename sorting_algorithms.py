def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]  # Fix index here
    return array

def improved_bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return array

def quick_sort(array):
    stack = [(0, len(array) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = array[start]
        low = start + 1
        high = end

        while True:
            while low <= high and array[high] >= pivot:
                high -= 1
            while low <= high and array[low] <= pivot:
                low += 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break

        array[start], array[high] = array[high], array[start]

        stack.append((start, high - 1))
        stack.append((high + 1, end))

    return array

def quick_sort_mid_pivot(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        pivot = array[mid]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quick_sort_mid_pivot(left) + middle + quick_sort_mid_pivot(right)

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n):
        minimum_index = i
        for j in range(i+1, n):
            if array[j] < array[minimum_index]:
                minimum_index = j
        array[i], array[minimum_index] = array[minimum_index], array[i]
    return array

def heap_sort(array):
    n = len(array)

    def heapify(array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[left] > array[largest]:
            largest = left

        if right < n and array[right] > array[largest]:
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array

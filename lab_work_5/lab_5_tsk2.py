"""
Упорядочить по возрастанию элементы массивов А размером 9 и В размером 11, расположенные после максимального элемента.
Упорядочение части массива, начинающейся элементом с заданным индексом, осуществить в методе.
"""
def max_ind(arr):
    mxin = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[mxin]:
            mxin = i
    return mxin

def sort_max(arr, max_index):
    part_to_sort = arr[max_index + 1:]
    n = len(part_to_sort)
    for i in range(n):
        for j in range(0, n-i-1):
            if part_to_sort[j] >= part_to_sort[j+1]:
                part_to_sort[j], part_to_sort[j+1] = part_to_sort[j+1], part_to_sort[j]
    return arr[:max_index + 1] + part_to_sort

a = [3, 1, 9, 1, 5, 5, 2, 6, 5]
b = [5, 3, 5, 15, 1, 2, 4, 6, 8, 7, 9]
print(a)
print(b)

maxind_A= max_ind(a)
maxind_B = max_ind(b)

sorte_A = sort_max(a, maxind_A)
sorte_B = sort_max(b, maxind_B)

print("Отсортированный массив A >>", sorte_A)
print("Отсортированный массив B >>", sorte_B)


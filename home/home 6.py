def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:  # Если элемент больше следующего, меняем их
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(target, arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Находим середину
        if arr[mid] == target:  # Элемент найден
            print(f"Элемент {target} найден на позиции {mid}")
            return
        elif arr[mid] < target:  # Ищем в правой половине
            left = mid + 1
        else:  
            right = mid - 1

    print(f"Элемент {target} не найден")


nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubble_sort(nums)
print("Отсортированный список:", sorted_nums)

binary_search(34, sorted_nums)
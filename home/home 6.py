def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binary_search(value, arr):
    num1 = 0
    num2 = len(arr)-1
    num = False
    pos = -1
    while num1 <= num2:
        center = (num1+num2)//2
        if arr[center] == value:
            num = True
            pos = center
            break
        elif arr[center] < value:
            num1 = center + 1
        else:
            num2 = center - 1
    if num:
        print(f"Элемент найден: {pos}")
    else:
        print("Элемент не найден")


list1 = [5, 7, 2, 6, 3, 4, 1]
print(f"Неотсортированный спс: {list1}")

sorted_list = bubble_sort(list1)
print(f"Отсортированный спс: {sorted_list}")

list2 = [2, 11, 19, 22, 30, 31, 46, 52, 55, 69, 76, 79, 81, 87, 95]

value1 = 79
binary_search(value1, list2)

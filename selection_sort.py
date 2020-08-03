def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                temp = arr[i]
                arr[i] = arr[min_idx]
                arr[min_idx] = temp
    return arr
nums = [66, 22, 41, 12, 11, 10]
sorted_nums = selection_sort(nums)
print(sorted_nums)

# Create a function bubble sort
def bubble_sort(n):
    n = len(n)
    for i in range(n):
        for j in range(n-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n
my_list = [10, 40, 11, 22, 44]
sorted_list = bubble_sort(my_list)
print(sorted_list)
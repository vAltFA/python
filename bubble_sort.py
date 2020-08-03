# Create a function bubble sort
def bubble_sort(x):
    n = len(x)
    for i in range(n):
        for j in range(n-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x
my_list = [10, 40, 11, 22, 44]
sorted_list = bubble_sort(my_list)
print(sorted_list)
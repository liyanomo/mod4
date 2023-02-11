
a = [ 5, 6, 10, 1, 3]

def insertion_sort(a):
    for i in range(1, len(a)):
        t = a[i]
        j = i - 1
        while j >= 0 and a[j] > t:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = t
insertion_sort(a)
print(a)

elem = 10
def binary_search(a, elem):
    low = 0
    high = len (a)

    while low <= high:
        middle = (low + high) // 2
        if a[middle] == elem:
            return middle

        elif a[middle] > elem:
            high = middle - 1 
        else:
            low = middle + 1
    return index
print (binary_search(a, elem))

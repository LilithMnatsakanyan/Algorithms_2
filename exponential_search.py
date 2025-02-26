# Exponential Search
def binary_search(arr, l, r, x):
    while l <=r:
        mid = l +(r -l) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid +1
        else:
            r = mid -1
    return -1

def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    n = len(arr)
    i = 1
    while i <n and arr[i] <= x:
        i *= 2
    start = i //2  
    end = min(i, n -1)  
    return binary_search(arr, start, end,x)  

arr = [2, 3, 4, 7, 12, 17, 20, 54, 100, 101]
x =54
index = exponential_search(arr, x)
print(f"Element found at index {index}" if index != -1 else "Element not found")

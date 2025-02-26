# Binary Search
def binary_search(arr,x):
    l = 0
    r =len(arr) - 1
    while l <= r:
        mid = (l + r) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid +1
        else:
            r = mid -1

print("\nBinary Search Example:")
arr = [0, 1, 5, 9, 10]
print(f"Index of 10: {binary_search(arr,10)}")

# Linear Search
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

print("\nLinear search example:")
arr = [66, 12, 77, 99, 20]
print("Index is:", linear_search(arr,99))

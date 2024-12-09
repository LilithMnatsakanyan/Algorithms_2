# Interpolation Search
def interpolation_search(arr, x):
    l = 0
    r = len(arr) -1
    while l <=r and x >=arr[l] and x<= arr[r]:
        pos = l +((x -arr[l]) *(r -l)) //(arr[r] -arr[l])
        if pos <l or pos > r:
            break
        if arr[pos] == x:
            return pos
        elif arr[pos] <x:
            l = pos +1
        else:
            r = pos -1
    return -1

arr = [12, 25, 26, 25, 24, 27, 50, 52, 54]
x = 52
index = interpolation_search(arr, x)
print(f"Element found at index {index}" if index != -1 else "Element not found")


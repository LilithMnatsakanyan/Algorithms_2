# Ternary Search
def ternary_search(arr, left, right):
    while right -left >2:
        mid1 = left +(right - left) //3
        mid2 = right -(right - left) //3
        
        if arr[mid1] < arr[mid2]:
            left = mid1
        else:
            right = mid2
    
    return max(arr[left], arr[left+1], arr[left+2])

arr = [5, 6, 7, 8, 10, 10, 45, 88, 4]
left = 0
right = len(arr) -1
lll = ternary_search(arr, left, right)
print("Maximum value is:", lll )

# Jump Search
def jump_search(arr, x):
    n = len(arr)
    step = int(n**0.5)
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    return prev if arr[prev] == x else -1

print("\nJump Search Example:")
arr = [10, 20, 30, 40, 50]
print(f"Index of 50: {jump_search(arr, 50)}")

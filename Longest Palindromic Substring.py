# Longest Palindromic Substring
def longest(txt):
    n = len(txt)
    start = 0
    max_len = 1
    for i in range(1, n):
        l =i - 1
        r =i
        while l >=0 and r <n and txt[l]== txt[r]:
            if r -l +1 > max_len:
                start = l
                max_len = r -l +1
            l -= 1
            r += 1
        l=i -1
        r =i +1
        while l >=0 and r <n and txt[l] == txt[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r -l +1
            l -= 1
            r += 1
    return txt[start:start +max_len]

print("\nLongest Palindromic Substring Example:")
text = "babad"
print(f"The longest palindromic substring in '{text}' is '{longest(text)}'")

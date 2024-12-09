# Naive String Matching done
def naive_string_match(pat, text):
  m = len(pat)
  n = len(text)
  for i in range(n - m + 1):
    j = 0
    while j < m :
      if text[i+j] != pat[j]:
        break
      j+=1
      if j ==m:
          print(f"Pattern found at index {i}")

text = "gogollalalala go lalal"
pat = "lala"
print("\nNaive String Matching Example:")
naive_string_match(pat, text)

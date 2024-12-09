# Knuth-Morris-Pratt Algorithm
def compute_table(pattern):
    m = len(pattern)
    table = [0] *m 
    j = 0  
    for i in range(1,m):
        if pattern[i] ==pattern[j]:
            j += 1
            table[i]= j 
        else:
            if j != 0:
                j = table[j-1] 
                i -= 1  
            else:
                table[i]=0  
    return table

def kmp_match(text, pattern):
    m, n = len(pattern),len(text)
    table = compute_table(pattern)  
    i = 0
    j = 0
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:  
            print(f"Pattern found at index {i - j}")
            j = table[j - 1]  
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = table[j -1]  
            else:
                i += 1 

print("\nKnuth-Morris-Pratt Algorithm Example:")
kmp_match("eeeeeaaaaty", "aaty")

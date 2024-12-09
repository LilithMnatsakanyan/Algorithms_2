# Boyer-Moore Algorithm
def boyer_moore(text, pattern):
    def miakner(pattern):
        last = {}
        unique=set(pattern)  
        
        for i in range(len(pattern)):
            last[pattern[i]] = i  
        
        return last, unique

    last,unique = miakner(pattern)  
    
    m =len(pattern)
    n =len(text)
    i = 0  
    
    while i <= n-m: 
        j = m -1  
        while j >= 0 and text[i +j] ==pattern[j]:
            j -= 1
        if j < 0:
            print(f"Pattern found at index {i}")
            i += 1  
        else:
            if text[i + j] not in unique:
                i +=m
            else:
                i += max(1, j -last.get(text[i + j],-1))  

print("\nBoyer-Moore Algorithm Example:")
boyer_moore("blaaaablllllbaaa", "bll")

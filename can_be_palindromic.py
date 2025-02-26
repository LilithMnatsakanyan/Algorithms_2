# Can Be Palindromic
def can_be_palindromic(s):
    unique_chars =set(s)
    odd_count = 0
    for i in unique_chars:
        count = s.count(i)  
        if count %2 !=0:
            odd_count += 1
    if odd_count >1:
        return False
    else:
        return True

print(can_be_palindromic("aaarrr"))  
print(can_be_palindromic("asssa")) 
print(can_be_palindromic("kkkaall"))    

# Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

print("\nPalindrome Check example:")
word = "sus"
print(is_palindrome(word))

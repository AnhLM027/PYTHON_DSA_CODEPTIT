def is_palindrome(s):
    return s == s[::-1]

def generate_binary_palindromes(n, current="", a=[]):
    if len(current) == n:
        if is_palindrome(current):
            a.append(" ".join(current))
        return
    
    generate_binary_palindromes(n, current + "0", a)
    generate_binary_palindromes(n, current + "1", a)

n = int(input())
a = []
generate_binary_palindromes(n, "", a)
print("\n".join(a))
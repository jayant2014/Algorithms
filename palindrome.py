# Time O(n^2) | Space O(n)
def is_palindrome(str):
    revstr = ''
    for i in reversed(range(len(str))):
        revstr += str[i]
    return str == revstr

# Time O(n) | Space O(n)
def is_palindrome1(str):
    revchars = []
    for i in reversed(range(len(str))):
        revchars.append(str[i])
    return str == "".join(revchars)

# Time O(n) | Space O(1)
def is_palindrome2(str):
    left_index = 0
    right_index = len(str) - 1
    while left_index < right_index:
        if str[left_index] != str[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True

str = 'abcba'
if is_palindrome2(str):
    print(str + ' is palindrome')
else:
    print(str + ' is not palindrome')

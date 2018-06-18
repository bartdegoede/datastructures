def to_str(n, base):
    chars = '0123456789ABCDEF'
    if n < base:
        return chars[n]
    else:
        return to_str(n // base, base) + chars[n % base]


def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


def palindrome(s):
    s = s.lower()
    if reverse(s) == s:
        return True
    return False


if __name__ == '__main__':
    assert(to_str(769, 10) == '769')
    assert(to_str(1234567890, 16) == '499602D2')
    assert(to_str(12345, 2) == '11000000111001')

    assert(reverse('hello') == 'olleh')
    assert(reverse('l') == 'l')
    assert(reverse('') == '')

    assert(palindrome('kayak') == True)
    assert(palindrome('palindrome') == False)

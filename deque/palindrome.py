from deque import Deque


def is_palindrome(s):
    d = Deque()
    for c in s:
        d.add_rear(c)

    while d.size > 1:
        l = d.remove_front()
        r = d.remove_rear()
        if l != r:
            return False
    return True


if __name__ == '__main__':
    assert(is_palindrome('lsdkjfskf') == False)
    assert(is_palindrome('racecar') == True)

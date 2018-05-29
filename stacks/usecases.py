from stack import Stack

def reverse_string(s):
    stack = Stack()
    for c in s:
        stack.push(c)
    rs = ''
    while not stack.is_empty():
        rs += stack.pop()

    return rs


def parentheses(s):
    parens = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    stack = Stack()
    for c in s:
        if c in parens:
            stack.push(c)
        else:
            if stack.is_empty() or stack.pop() not in parens:
                return False

    if not stack.is_empty():
        return False
    return True


def to_binary(number):
    stack = Stack()

    while number > 0:
        stack.push(number % 2)
        number //= 2

    binary_string = ''
    while not stack.is_empty():
        binary_string += str(stack.pop())

    return binary_string


def base_converter(number, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > len(digits):
        raise Exception('Invalid base {}; must be between 2 and '
                        '{}'.format(base, len(digits)))
    stack = Stack()

    while number > 0:
        stack.push(number % base)
        number //= base

    ret_string = ''
    while not stack.is_empty():
        ret_string += str(digits[stack.pop()])

    return ret_string

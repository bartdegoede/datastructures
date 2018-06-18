def binary_search(l, v):
    first = 0
    last = len(l) - 1
    found = False
    c = 1
    while first <= last and not found:
        midpoint = (first + last) // 2
        if l[midpoint] == v:
            found = True
        else:
            if v < l[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
        c += 1
    print('Took {} steps'.format(c))
    return found


def binary_recursive(l, v):
    if len(l) == 0:
        return False
    else:
        midpoint = len(l) // 2
        if l[midpoint] == v:
            return True
        else:
            if v < l[midpoint]:
                # slicing is O(k); keeping track of indices
                # would be more efficient
                return binary_recursive(l[:midpoint], v)
            else:
                return binary_recursive(l[midpoint + 1:], v)


if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    assert(binary_search(test_list, 3) == False)
    assert(binary_search(test_list, 13) == True)

    assert(binary_recursive(test_list, 3) == False)
    assert(binary_recursive(test_list, 13) == True)

def list_sum(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + list_sum(l[1:])

if __name__ == '__main__':
    assert(list_sum([1, 3, 5, 7, 9]) == 25)
    assert(list_sum([1]) == 1)

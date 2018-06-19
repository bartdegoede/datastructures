def sort(l):
    for pass_num in range(len(l) - 1, 0, -1):
        for i in range(pass_num):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]


def short_circuit_sort(l):
    exch = True
    pass_num = len(l) - 1
    while pass_num > 0 and exch:
        exch = False
        for i in range(pass_num):
            if l[i] > l[i+1]:
                exch = True
                l[i], l[i+1] = l[i+1], l[i]
        pass_num -= 1


if __name__ == '__main__':
    l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sort(l)
    assert(l == [17, 20, 26, 31, 44, 54, 55, 77, 93])
    short_circuit_sort(l)
    assert(l == [17, 20, 26, 31, 44, 54, 55, 77, 93])

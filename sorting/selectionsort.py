def sort(l):
    for i in range(len(l) - 1, 0, -1):
        pos_max = 0
        for j in range(1, i + 1):
            if l[j] > l[pos_max]:
                pos_max = j
        l[i], l[pos_max] = l[pos_max], l[i]


if __name__ == '__main__':
    l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sort(l)
    assert(l == [17, 20, 26, 31, 44, 54, 55, 77, 93])

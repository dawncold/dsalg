# -*- coding: UTF-8 -*-


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, s, e):
    if s < e:
        p = partition(alist, s, e)
        quick_sort_helper(alist, s, p - 1)
        quick_sort_helper(alist, p + 1, e)


def partition(alist, s, e):
    p_inx = adjust_mid(alist, s, e)
    # print alist
    p = alist[p_inx]
    left = s
    right = e
    while True:
        while left < p_inx and alist[left] <= p:
            left = left + 1
        # print 'l: {}'.format(left)
        while right > left and alist[right] >= p:
            right = right - 1
        # print 'r: {}'.format(right)
        if right <= left:
            break
        else:
            alist[left], alist[right] = alist[right], alist[left]
            # print alist
    if p_inx != right:
        alist[p_inx], alist[right] = alist[right], alist[p_inx]
    # print alist
    return right


def adjust_mid(alist, s, e):
    m = s + (e - s) / 2
    # print 's: {}, m: {}, e: {}'.format(alist[s], alist[m], alist[e])
    if alist[s] > alist[m]:
        alist[s], alist[m] = alist[m], alist[s]
    if alist[s] > alist[e]:
        alist[s], alist[e] = alist[e], alist[s]
    if alist[m] > alist[e]:
        alist[m], alist[e] = alist[e], alist[m]
    if m != e - 1:
        alist[m], alist[e - 1] = alist[e - 1], alist[m]
    return e - 1


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print alist
    quick_sort(alist)
    print alist

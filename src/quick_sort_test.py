# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
from unittest import TestCase
from quick_sort import adjust_mid, quick_sort


class QuickSortTest(TestCase):

    def test_adjust_mid(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        adjust_mid(alist, 0, len(alist) - 1)
        self.assertEqual(alist[0], 20)
        self.assertEqual(alist[-1], 77)
        self.assertEqual(alist[-2], 54)

    def test_sort(self):
        alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        quick_sort(alist)
        self.assertEqual(alist, [17, 20, 26, 31, 44, 54, 55, 77, 93])

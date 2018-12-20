# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import unittest
from linked_list import LinkedList, DoublyLinkedList


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        data = [1, 2, 3, 4, 5]
        l = LinkedList(*data)
        self.assertEqual(1, l.head.data)
        self.assertEqual(5, l.tail.data)

    def test_empty_list(self):
        l = LinkedList()
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)

    def test_append(self):
        l = LinkedList()
        l.append(1)
        self.assertEqual(1, l.head.data)
        self.assertEqual(1, l.tail.data)

    def test_delete(self):
        l = LinkedList(1, 2, 3)
        self.assertEqual(1, l.head.data)
        l.delete(1)
        self.assertEqual(2, l.head.data)
        l.delete(3)
        self.assertEqual(2, l.head.data)
        self.assertEqual(2, l.tail.data)

    def test_insert(self):
        l = LinkedList()
        l.insert(1, 0)
        self.assertEqual(1, l.head.data)
        self.assertEqual(1, l.tail.data)

    def test_insert_out_of_list(self):
        l = LinkedList()
        self.assertRaises(ValueError, lambda: l.insert(1, 1))

    def test_insert_with_negative_inx(self):
        l = LinkedList()
        self.assertRaises(ValueError, lambda: l.insert(1, -1))

    def test_index(self):
        l = LinkedList()
        self.assertIsNone(l.index(1))
        l.append(1)
        l.append(1)
        self.assertEqual(0, l.index(1))
        l.append(2)
        self.assertEqual(2, l.index(2))

    def test_get(self):
        l = LinkedList()
        self.assertIsNone(l.get(1))
        l.append(1)
        self.assertEqual(1, l.get(0))
        l.append(2)
        self.assertEqual(2, l.get(1))

    def test_get_with_negative_inx(self):
        l = LinkedList()
        self.assertRaises(ValueError, lambda: l.get(-1))


class TestDoublyLinkedList(unittest.TestCase):
    def test_linked_list(self):
        data = [1, 2, 3, 4, 5]
        l = DoublyLinkedList(*data)
        self.assertEqual(1, l.head.data)
        self.assertEqual(5, l.tail.data)

    def test_empty_list(self):
        l = DoublyLinkedList()
        self.assertIsNone(l.head)
        self.assertIsNone(l.tail)

    def test_append(self):
        l = DoublyLinkedList()
        l.append(1)
        self.assertEqual(1, l.head.data)
        self.assertEqual(1, l.tail.data)

    def test_delete(self):
        l = DoublyLinkedList(1, 2, 3)
        self.assertEqual(1, l.head.data)
        l.delete(1)
        self.assertEqual(2, l.head.data)
        l.delete(3)
        self.assertEqual(2, l.head.data)
        self.assertEqual(2, l.tail.data)

    def test_insert(self):
        l = DoublyLinkedList()
        l.insert(1, 0)
        self.assertEqual(1, l.head.data)
        self.assertEqual(1, l.tail.data)

    def test_insert_out_of_list(self):
        l = DoublyLinkedList()
        self.assertRaises(ValueError, lambda: l.insert(1, 1))

    def test_insert_with_negative_inx(self):
        l = DoublyLinkedList()
        self.assertRaises(ValueError, lambda: l.insert(1, -1))

    def test_index(self):
        l = DoublyLinkedList()
        self.assertIsNone(l.index(1))
        l.append(1)
        l.append(1)
        self.assertEqual(0, l.index(1))
        l.append(2)
        self.assertEqual(2, l.index(2))

    def test_get(self):
        l = DoublyLinkedList()
        self.assertIsNone(l.get(1))
        l.append(1)
        self.assertEqual(1, l.get(0))
        l.append(2)
        self.assertEqual(2, l.get(1))

    def test_get_with_negative_inx(self):
        l = DoublyLinkedList()
        self.assertRaises(ValueError, lambda: l.get(-1))

# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division


class Node(object):
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList(object):
    def __init__(self, *data):
        self.head = None
        self.tail = None
        nodes = [Node(d) for d in data]
        if nodes:
            self.head = nodes[0]
            self.tail = nodes[-1]
            for i, node in enumerate(nodes):
                if i + 1 >= len(nodes):
                    break
                node.next_node = nodes[i + 1]

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next_node = node
        self.tail = node

    def delete(self, data):
        def find_prev(node):
            if self.head is node:
                return None
            current = self.head
            while current is not None:
                if current.next_node is node:
                    return current
                current = current.next_node

        current = self.head
        while current is not None:
            if current.data == data:
                prev_node = find_prev(current)
                if prev_node is None:
                    self.head = current.next_node
                else:
                    prev_node.next_node = current.next_node

                if current.next_node is None:
                    self.tail = prev_node
            current = current.next_node

    def insert(self, data, inx):
        if inx < 0:
            raise ValueError('invalid inx')
        node = Node(data)
        if inx == 0:
            if self.head:
                node.next_node = self.head.next_node
            self.head = node
            if not self.tail:
                self.tail = node
        else:
            i = 0
            prev = None
            current = self.head
            while current is not None:
                if i == inx:
                    node.next_node = current
                    prev.next_node = node
                    break
                i += 1
                prev = current
                current = current.next_node
            if i != inx:
                raise ValueError('inx out of list')

    def index(self, data):
        data_inx = None
        i = 0
        current = self.head
        while current is not None:
            if current.data == data:
                data_inx = i
                break
            i += 1
            current = current.next_node
        return data_inx

    def get(self, inx):
        if inx < 0:
            raise ValueError('invalid inx')
        if inx == 0:
            return None if not self.head else self.head.data
        else:
            i = 0
            current = self.head
            while current is not None:
                if i == inx:
                    return current.data
                i += 1
                current = current.next_node

    def get_node(self, inx):
        if inx < 0:
            raise ValueError('invalid inx')
        if inx == 0:
            return None if not self.head else self.head
        else:
            i = 0
            current = self.head
            while current is not None:
                if i == inx:
                    return current
                i += 1
                current = current.next_node

    def display(self):
        print('h: {}({}), t:{}({})'.format(self.head.data, hex(id(self.head)), self.tail.data, hex(id(self.tail))))
        current = self.head
        while current is not None:
            print(current.data, hex(id(current)))
            current = current.next_node

    def detect_loop(self):
        p1 = p2 = self.head
        while True:
            p1 = p1.next_node
            if p1 is None:
                break
            p2 = p2.next_node
            if p2 is None:
                break
            else:
                p2 = p2.next_node
            print('p1: {}, p2: {}'.format(p1.data, p2.data))
            if p1.data == p2.data:
                print('found loop')
                return
        print('no loop')


class DoublyLinkedList(object):
    def __init__(self, *data):
        self.head = None
        self.tail = None
        nodes = [Node(d) for d in data]
        if nodes:
            self.head = nodes[0]
            self.tail = nodes[-1]
            for i, node in enumerate(nodes):
                if i + 1 >= len(nodes):
                    node.prev_node = nodes[i - 1]
                    break
                node.next_node = nodes[i + 1]
                nodes[i + 1].prev_node = node

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next_node = node
            node.prev_node = self.tail
        self.tail = node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev_node is None:
                    self.head = current.next_node
                    if current.next_node:
                        current.next_node.prev_node = None
                else:
                    current.prev_node.next_node = current.next_node
                    if current.next_node:
                        current.next_node.prev_node = current.prev_node

                if current.next_node is None:
                    self.tail = current.prev_node
                    if current.prev_node:
                        current.prev_node.next_node = None
            current = current.next_node

    def insert(self, data, inx):
        if inx < 0:
            raise ValueError('invalid inx')
        node = Node(data)
        if inx == 0:
            if self.head:
                node.next_node = self.head.next_node
                self.head.prev_node = node
            self.head = node
            if not self.tail:
                self.tail = node
        else:
            i = 0
            current = self.head
            while current is not None:
                if i == inx:
                    node.prev_node = current.prev_node
                    node.next_node = current
                    current.prev_node.next_node = node
                    current.prev_node = node
                    break
                i += 1
                current = current.next_node
            if i != inx:
                raise ValueError('inx out of list')

    def index(self, data):
        data_inx = None
        i = 0
        current = self.head
        while current is not None:
            if current.data == data:
                data_inx = i
                break
            i += 1
            current = current.next_node
        return data_inx

    def get(self, inx):
        if inx < 0:
            raise ValueError('invalid inx')
        if inx == 0:
            return None if not self.head else self.head.data
        else:
            i = 0
            current = self.head
            while current is not None:
                if i == inx:
                    return current.data
                i += 1
                current = current.next_node

    def display(self):
        print('h: {}({}), t:{}({})'.format(self.head.data, hex(id(self.head)), self.tail.data, hex(id(self.tail))))
        current = self.head
        while current is not None:
            print('id: {}, d: {}, prev: {}, next: {}'.format(hex(id(current)), current.data, hex(id(current.prev_node)) if current.prev_node else 'N/A',
                                                             hex(id(current.next_node)) if current.next_node else 'N/A'))
            current = current.next_node


if __name__ == '__main__':
    L = LinkedList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    L.detect_loop()
    print('build loop 11->4')
    L.tail.next_node = L.get_node(3)
    L.detect_loop()

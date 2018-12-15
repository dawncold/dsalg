# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self, *data):
        self.head = None
        self.tail = None
        nodes = [Node(d, None) for d in data]
        if nodes:
            self.head = nodes[0]
            self.tail = nodes[-1]
            for i, node in enumerate(nodes):
                if i + 1 >= len(nodes):
                    break
                node.next_node = nodes[i + 1]

    def append(self, data):
        node = Node(data, None)
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
        node = Node(data, None)
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

    def display(self):
        print('h: {}({}), t:{}({})'.format(self.head.data, hex(id(self.head)), self.tail.data, hex(id(self.tail))))
        current = self.head
        while current is not None:
            print(current.data, hex(id(current)))
            current = current.next_node


if __name__ == '__main__':
    L = LinkedList(1, 2, 3, 4, 5)
    L.display()
    print('append 6')
    L.append(6)
    L.display()
    print('delete 6')
    L.delete(6)
    L.display()
    print('append 1,1,1')
    L.append(1)
    L.append(1)
    L.append(1)
    L.display()
    print('delete 1')
    L.delete(1)
    L.display()
    print('insert 9 into 1')
    L.insert(9, 1)
    L.display()

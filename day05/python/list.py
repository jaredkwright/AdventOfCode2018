class Node:
    def __init__(self, value):
        self.value = value
        self.prev_node = None
        self.next_node = None

    def __next__(self):
        if self.next_node is None:
            raise StopIteration
        return self.next_node

    def __str__(self):
        return str(self.value)


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        return self.length

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        if self.tail:
            old_tail = self.tail
            old_tail.next_node = new_node
            new_node.prev_node = old_tail
            self.tail = new_node
        self.length += 1

    def peek(self):
        return self.tail

    def pop(self):
        if not self.tail:
            return None
        old_tail = self.tail
        new_tail = old_tail.prev_node
        if new_tail:
            new_tail.next_node = None
        self.tail = new_tail
        self.length -= 1
        return old_tail.value



class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item = self.current.value
            self.current = self.current.next_node
            return item

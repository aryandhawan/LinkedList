class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_begnning(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            raise 'Not possible since the head does not exist'
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_position(self, value, pos):
        new_node = Node(value)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current and count < pos - 1:
            current = current.next
            count += 1

        if not current:
            raise IndexError("Position out of bounds")

        new_node.next = current.next
        current.next = new_node

        while current and count < pos - 1:
            current = current.next
            count += 1
        if not current:
            raise IndexError("Position out of bounds")

        current.next = new_node.next
        current.next = new_node

    def deletion_at_begnning(self):
        if not self.head:
            raise 'there is nothing to delete in here!'
        else:
            self.head = self.head.next

    def deletion_at_end(self):
        if not self.head:
            raise 'not possible'
        else:
            current = self.head
            while current.next.next:  # we will reach the second last node
                current = current.next

            current.next = None

    def deletion_at_middle(self, pos):
        if pos == 0:
            self.deletion_at_begnning()
        else:
            current = self.head
            count = 0

            while current and count < pos - 1:
                current = current.next
                count += 1
            if current is None or current.next is None:
                raise IndexError("Position out of bounds")

            current.next = current.next.next

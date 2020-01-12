from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the item exists
       self.current 

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

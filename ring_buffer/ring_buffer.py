from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the item exists
        if self.current is not None:
        # store it
            self.storage.move_to_end(item)
            return


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

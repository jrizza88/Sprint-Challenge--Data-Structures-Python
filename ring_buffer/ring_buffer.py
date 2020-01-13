from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the item exists
        if  self.storage.length < self.capacity:
            # invoke the add to tail function from the dll
            self.storage.add_to_tail(item)
            # set the new current to head
            self.current = self.storage.head

        elif self.storage.length == self.capacity:
            the_values = self.storage.head
            # if not self.current:
            #     self.current = self.storage.tail

      
            self.storage.remove_from_head()
            
            self.storage.add_to_tail(item)
  
            if the_values == self.current:
                self.current = self.storage.tail
            # self.current.value = item
            # self.current = self.current.prev
            
            print("item", item)
            print('storage length: ', self.storage.length)
            print('\n')
        
            
        # else:
        #     self.storage.add_to_head(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr = self.storage.head
        while curr is not None:
            list_buffer_contents.append(curr.value)
            curr = curr.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

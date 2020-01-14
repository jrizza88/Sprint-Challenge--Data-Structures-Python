from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the item is less than capacity, add!
        if  self.storage.length < self.capacity:
        #     # invoke the add to tail function from the dll
            self.storage.add_to_tail(item)
        #     # set the new current to head
            self.current = self.storage.head
        #     print('self.current as head', self.current)
            

        elif self.storage.length == self.capacity:
            print('values', self.storage.head)
           
            if not self.current:
            #     print('self.current.value', self.current.value)
                self.current = self.storage.head
                print('self.current as tail', self.current.value)
            #     print('self.current as head', self.storage.head)

            #     print('print previous', self.current.prev)

            #     print('self.current.value', self.current.value)
            self.storage.remove_from_head()
            
            self.storage.add_to_head(item)
            the_value = self.storage.head
            self.storage.value = item
            self.current = self.current.prev
            
            if the_value == self.current:
                print('self.storage.head', self.storage.head)
                print('self.current.tail', self.storage.tail)
                self.current = self.storage.tail

            
            print("item", item)
            print('storage length: ', self.storage.length)
            print('\n')
        
            
        else:
            self.storage.add_to_head(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr = self.storage.head
        if curr is None:
            list_buffer_contents.append(curr.value)
        # if self.current.next is not None:
        #     #if current isn't the only node in the list
        #     #store the next node
        #         curr = self.current.next
        # else:
        #         curr = self.storage.head

        while curr is not None:
            print('curr value', curr.value)
            list_buffer_contents.append(curr.value)
            # print('self.storage.next', self.current.next)
            # curr = self.current.next
            curr = curr.next
            print('curr.next', curr)
            # if self.current.next is not None:
            #     curr = self.storage.head
            # else:
            #     curr = curr.next
            # if curr:
            #     curr = self.storage.head
            # else:
            #     curr = curr.next
            # print('curr.next', curr.next)
            # if curr is None:
            #     self.current = self.storage.head
            # else: 
            #     self.current = self.current.next

        # list_buffer_contents.append(curr.value)
        return list_buffer_contents

    # def get(self):
    #     # Note:  This is the only [] allowed
    #     list_buffer_contents = []

    #     if self.storage.length <= 0:
    #         return list_buffer_contents

    #     current = self.storage.head
    #     list_buffer_contents.append(current.value)
        
    #     # if current == self.capacity:
    #     #     # printing current.prev helped me to understand what is being printed here
    #     #     print('curr prev', current.prev)
    #     #     self.current = current.prev
    #     #     list_buffer_contents.append(current.value)      
    #     return list_buffer_contents
        # if self.storage.length < 1:
        #     return list_buffer_contents
        # # list_buffer_contents.append(self.current.value)
        # # print(list_buffer_contents.append(self.current.value))
        # if self.current.next is not None:
        #     current = self.storage.head
            
        # else:
        #     next_val = self.current.next
        # # list_buffer_contents.append(self.current.value)
        # # TODO: Your code here
        # current = self.storage.head
        # while current is not self.current:
        #     list_buffer_contents.append(current.value)
        #     next_val = self.current.next
        #     if next_val is not None:
        #         next_val = next_val.next
            
        #     else:
        #         self.head = self.storage.head
        #         self.tail = self.storage.tail
        # # while current is not None:
        # #     list_buffer_contents.append(current.value)
        # #     current = current.next



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

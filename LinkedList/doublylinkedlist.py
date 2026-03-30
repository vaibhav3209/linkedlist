''' This only makes a node w/o a linkage '''
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertatend(self,value):
        new_node = Node(value)

        #if empty list
        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        #to reach last node
        while temp.next:
            temp = temp.next

        temp.next = new_node

        '''I forgot to add this line, yahi to reason hai doubly linked list ka.'''
        new_node.prev = temp

    def printfwd(self):
        temp = self.head
        while temp:
            print(f'{temp.data}',end='->')
            temp=temp.next
        print(None)

    '''** since doubly LL. ==>> reverse printing is possible easy**'''
    def printbkwd(self):
        temp = self.head
        #reach to last node
        while temp.next:
            temp = temp.next

        tail = temp
        while tail:
            print(tail.data,end='->')
            tail = tail.prev
        print(None)

    def deleteatend(self):
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def deletefromstart(self):
        self.head = self.head.next
        self.head.prev = None

    def reversedll(self):
        temp = self.head
        second = temp.next

        while second :
            temp = temp.next
            second = temp.next

        #ab tail pe head le aao
        self.head = temp

        while temp :
            temp.next = temp.prev
            temp.prev = second
            second = temp
            temp = temp.next



dll = DoublyLinkedList()
dll.insertatend(1)
dll.insertatend(2)
dll.insertatend(3)
dll.printfwd()
dll.printbkwd()

# dll.deleteatend()
# dll.printfwd()
# dll.deletefromstart()
# dll.printfwd()
dll.reversedll()
dll.printfwd()
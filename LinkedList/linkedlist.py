from types import new_class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    '''
    1.head isi  function mein change hoga bas
    2. Not a recursive problem
    3. No need to check list is empty or not
    '''
    def insertatstart(self,data):
        new_node = Node(data)

        new_node.next = self.head   #move head

        self.head = new_node


    def insertatend(self,data):
        new_node = Node(data)

        ''' if list is empty then head abhi None hi hoga '''
        if self.head is None:
            self.head = new_node
            return

        ''' Note: head always points at start. To traverse in linked list we move the temp pointer'''
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node


    def insertatend_rec(self,data):
        self.head = self._helper(self.head,data)

    def _helper(self,head,data):
        # when list is empty or last node
        if not head:
            return Node(data)

        head.next = self._helper(head.next,data)
        return head

    '''insert AT nhi kar sakte insert AFTER karna padega'''
    def insertafterpos(self,data,pos):
        if pos == 0:
            self.insertatstart(data)
            return

        new_node = Node(data)
        temp = self.head

        ''' to reach that position: now temp will point '''
        for i in range(pos):

            ''' if out of range ho gya to '''
            if temp is None:
                print("position out of range")
                return

            temp = temp.next

        ''' this order is very important '''
        new_node.next = temp.next
        temp.next = new_node


    def insertafterpos_rec(self,temp,data,pos):
        if pos == 0:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            return

        if not temp:
            print('out of bounds')
            return
        self.insertafterpos_rec(temp.next,data,pos-1)

    def printlist(self):
        temp = self.head

        while temp:
            ''' end mein -> dede and last mein bhi print hoga to None dedo '''
            print(temp.data,end ='->')
            temp = temp.next

        print(None)

    '''
    1. head pass kardo calling k time pe,
    2. Actual head will not change as the arguments are passed as a copy of original refernece '''
    def revprintlist_rec(self,temp):
        if not temp:
            return
        self.printlist_rec(temp.next)
        print(temp.data,end="->")

        '''new Tweak'''
        if temp == self.head:
            print(None)

    def printlist_rec(self,temp):
        if not temp:
            print(None)
            return
        print(temp.data,end="->")
        self.printlist_rec(temp.next)

    # def deletefromstart(self):
    #     if self.head is None:
    #         return
    #     self.head = self.head.next
    #     print('List after Deletetion from start is:')
    #     self.printlist()
    #
    # def deletefromend(self):
    #     prev = None
    #     temp = self.head
    #
    #     if temp is None:
    #         return
    #
    #     # only one node
    #     if self.head.next is None:
    #         self.head = None
    #         return
    #
    #     while temp.next is not None:
    #         prev = temp
    #         temp = temp.next
    #
    #     #now we are at last node
    #     prev.next = temp.next
    #     print('List after Deletetion from end is:')
    #     self.printlist()
    #
    # def deleteatpos(self,pos):
    #     if pos == 0:
    #         self.deletefromstart()
    #         return
    #
    #     temp = self.head
    #     prev = None
    #
    #     #traverse till postion
    #     for i in range(pos):
    #         if temp is None:
    #             print("position out of range")
    #             return
    #         prev = temp
    #         temp = temp.next
    #
    #     prev.next = temp.next
    #     print(f'List after Deleteting postion {pos} is:')
    #     self.printlist()




ll = LinkedList()
ll.insertatend(1)
ll.insertatstart(22)
ll.insertatend_rec(11)
ll.insertafterpos('vaib',1)
ll.insertafterpos_rec(ll.head,'malav',2)
ll.insertafterpos_rec(ll.head,'check',0)
ll.printlist()
# we have to pass head
# ll.printlist_rec(ll.head)


# =============================================

# how to delete n nodes simultaneously

# =============================================


'''
doing everything recursively
'''
# class Node:
#     def __init__(self,data):
#         self.value = data
#         self.next = None
#
# class LinkedListRecursive:
#     def __init__(self):
#         self.head = None
#
#     def helper(self,temp):
#         if not temp.next:
#             return temp
#
#         return self.helper(temp.next)
#
#     def insertatend(self,head,value):
#         new_node = Node(value)
#         temp = head
#
#         if not temp:
#             self.head = new_node
#             return
#
#         temp = self.helper(temp)
#
#         temp.next = new_node
#         return
#
#     def printlist(self,temp):
#         if not temp :
#             print(None)
#             return
#
#         print(temp.value,end='->')
#         self.printlist(temp.next)
#
#     def insertatbeg(self,value):
#         new_node = Node(value)
#         if not self.head:
#             self.head = new_node
#             return
#
#         new_node.next = self.head
#         self.head = new_node
#         return
#
#     def deletefromend(self):
#
#
#
#
#
# ll = LinkedListRecursive()
# ll.insertatend(ll.head,2)
# ll.insertatend(ll.head,3)
# ll.insertatend(ll.head,55)
# ll.insertatbeg(1)
# ll.printlist(ll.head)

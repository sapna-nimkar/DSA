
'''
LINEkD LIST: Remove Nth Node from End of List
'''

# create a linked list for data



class Linkedlist:

    def __init__(self, data):
        self.data = data
        self.next = None


def value_print(ll: Linkedlist):
    while ll is not None:
        print(ll.data)
        ll = ll.next

def remove_n(head: Linkedlist):
    prev = None
    curr = head
    while curr.next is not None:
        prev = curr
        curr = curr.next
    prev.next = curr.next
    return head


a = [10, 20, 30]
ll = Linkedlist(10)
ll.next = Linkedlist(20)
ll.next.next = Linkedlist(30)
value_print(ll)
new_ll = remove_n(ll)
value_print(new_ll)












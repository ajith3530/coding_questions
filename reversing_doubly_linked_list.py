class DoubleListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

def reversed_double_ll(input_head):
    prev_node = None
    head = input_head
    while head is not None:
        # Store the prev and next
        prev_node = head.prev
        next_node = head.next
        # Interchange connection
        head.next = prev_node
        head.prev = next_node
        # Iterate
        head = next_node


    return prev_node.prev

node_1 = DoubleListNode(val=1, prev=None, next=None)
node_2 = DoubleListNode(val=2, prev=node_1, next=None)
node_3 = DoubleListNode(val=3, prev=node_2, next=None)
node_4 = DoubleListNode(val=4, prev=node_3, next=None)
node_5 = DoubleListNode(val=5, prev=node_4, next=None)
node_6 = DoubleListNode(val=6, prev=node_5, next=None)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6

head = node_1
reversed_node = reversed_double_ll(head)
pass

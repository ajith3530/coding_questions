# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

    def __repr__(self):
        return str(self.value)

def replace_node(head: ListNode, x, y):
    dummy = head
    prev_node = None
    x_node, y_node = None, None
    x_prev_node, y_prev_node = None, None
    x_next_node, y_next_node = None, None
    while head is not None:
        if head.value == x:
            x_node = head
            x_prev_node = prev_node
            x_next_node = head.next
        if head.value == y:
            y_node = head
            y_prev_node = prev_node
            y_next_node = head.next
        # Iterate
        prev_node = head
        head = head.next

    if x_node is not None and y_node is not None:
        x_prev_node.next = y_node
        y_prev_node.next = x_node
        x_node.next = y_next_node
        y_node.next = x_next_node
    return dummy



node_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, None))) ) )))

node_2 = replace_node(node_1, x=2, y=5)
pass
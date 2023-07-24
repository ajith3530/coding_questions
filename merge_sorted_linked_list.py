class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val)
def merge_sorted_linked_list(l1, l2):
    dummy = ListNode(-1, None)
    l3 = dummy
    while l1 is not None or l2 is not None:
        if l1 is None:
            l3.next = l2
            break
        elif l2 is None:
            l3.next = l1
            break
        elif l1.val >= l2.val:
            l3.next = ListNode(l2.val, None)
            l3 = l3.next
            # Iterate
            l2 = l2.next
        elif l2.val >= l1.val:
            l3.next = ListNode(l1.val, None)
            l3 = l3.next
            # Iterate
            l1 = l1.next
    return dummy.next

node_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
node_2 = ListNode(5, ListNode(6, ListNode(7)))

merged_list = merge_sorted_linked_list(node_1, node_2)
pass

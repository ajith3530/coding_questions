# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)
class Solution:
    def reverseList(self, head):
        prev_node = None
        while head is not None:
            # Save the next node connection
            next_node = head.next
            # Reverse the connection (head=current)
            head.next = prev_node
            # Set previous node to current node (head=current)
            prev_node = head
            # Iterate the linked list
            head = next_node

        return prev_node

node_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

reversed = Solution().reverseList(node_1)
pass





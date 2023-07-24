# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "->".join(([repr(self.val)]))
class Solution:
    def addTwoNumbers(self, l1 , l2):
        addition, carry = 0, 0
        dummy = ListNode(val=-1, next=None)
        l3 = dummy
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None and l2 is not None:
                addition = l1.val + l2.val + carry
                # Iterate
                l1 = l1.next
                l2 = l2.next
            elif l1 is None and l2 is not None:
                addition = l2.val + carry
                # Iterate
                l2 = l2.next
            elif l1 is not None and l2 is None:
                addition = l1.val + carry
                # Iterate
                l1 = l1.next
            elif l1.next is None and l2.next is None and carry != 0:
                addition = carry
            # Calculating carry and addition
            carry = addition // 10
            addition = addition % 10
            l3.next = ListNode(val=addition, next=None)
            l3 = l3.next
        return dummy.next

node_1 = ListNode(1, ListNode(2, ListNode(8, ListNode(4))))
node_2 = ListNode(3, ListNode(4, ListNode(5, ListNode(6))))

add_value = Solution().addTwoNumbers(node_1, node_2)
pass





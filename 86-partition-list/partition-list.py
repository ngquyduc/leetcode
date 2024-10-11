# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        first_smaller_x, last_smaller_x, first_larger_x, last_larger_x, curr = None, None, None, None, head
        while curr != None:
            if curr.val >= x:
                if not first_larger_x:
                    first_larger_x = curr
                if not last_larger_x:
                    last_larger_x = curr
                    curr = curr.next
                    continue
                last_larger_x.next = curr
                last_larger_x = curr
                curr = curr.next
            else:
                if not first_smaller_x:
                    first_smaller_x = curr
                if not last_smaller_x:
                    last_smaller_x = curr
                    curr = curr.next
                    continue
                last_smaller_x.next = curr
                last_smaller_x = curr
                curr = curr.next
        if not first_smaller_x:
            return first_larger_x
        if not first_larger_x:
            return first_smaller_x
        last_smaller_x.next = first_larger_x
        last_larger_x.next = None
        return first_smaller_x
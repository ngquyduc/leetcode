# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        sum_set = {0}
        curr_sum = 0
        i = 0
        while i < len(arr):
            curr_sum += arr[i]
            if (curr_sum == 0 or curr_sum in sum_set):
                temp = 0
                for j in range(i, -1, -1):
                    temp += arr[j]
                    curr_sum -= arr[j]
                    sum_set.remove(curr_sum)
                    arr.pop(j)
                    i -= 1
                    if temp == 0:
                        break
            sum_set.add(curr_sum)
            i += 1
        res = prev = ListNode(0, None)
        for i in range(len(arr)):
            curr = ListNode(arr[i], None)
            prev.next = curr
            prev = prev.next
        return res.next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     current = head
     before = None
     while current:
         after = current.next
         current.next = before
         before = current
         current = after
     return before
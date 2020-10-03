# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dedup = ListNode(0)
        cur = dedup
        prev = None
        while head:
            if head.next != None and head.val == head.next.val:
                while head.next != None and head.next.val == head.val:
                    prev = head.val
                    head = head.next
                    
            if head.val != prev:
                cur.next = head
                cur = cur.next
                head = head.next

            else:
                if not head.next:
                    cur.next = None
                head = head.next
                
        return dedup.next
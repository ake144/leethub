# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head ==None or head.next == None:
            return head
        
        middle = self.getmiddle(head)
        nextmid = middle.next
        
        middle.next = None
        
        left = self.sortList(head)
        right = self.sortList(nextmid)
        
        sortedList = self.sortedList(left,right)
        return sortedList
    def getmiddle(self,head):
        if head == None:
            return head
        slow = head
        fast = head
        
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow
    def sortedList(self,a,b):
        result = None
        if a == None:
            return b
        elif b == None:
            return a
        if a.val <= b.val:
            result = a
            result.next = self.sortedList(a.next,b)
        else:
            result = b
            result.next = self.sortedList(a,b.next)
        return result
            
            
        
                    
        
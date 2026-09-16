# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Traverse the linked list.
# Store all the nodes (or their references) in a list.
# Reorder them using two indices (left and right).
# Reconnect the next pointers accordingly.


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        #finding the middle pt 
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #rev second half
        second = slow.next
        slow.next = None
        
        prev = None

        while second:
            front = second.next
            second.next = prev
            prev = second
            second = front


        #merge both halves
        first = head
        second = prev

        while second:
            temp1=first.next
            temp2=second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            
            

        


        

    

        
            

        
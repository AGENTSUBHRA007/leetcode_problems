# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Dono lists ke digits ko strings mein badal kar store karenge
        s1 = ""
        curr1 = l1
        while curr1:
            s1 += str(curr1.val)
            curr1 = curr1.next
            
        s2 = ""
        curr2 = l2
        while curr2:
            s2 += str(curr2.val)
            curr2 = curr2.next
            
        # Step 2: Strings ko reverse karke unka actual integer sum nikala
        # [::-1] string ko ulta kar deta hai (jaise "243" se "342")
        num1 = int(s1[::-1])
        num2 = int(s2[::-1])
        
        total_sum = num1 + num2
        
        # Step 3: Total sum ko string mein badla aur wapas reverse order mein linked list banayi
        sum_str = str(total_sum)[::-1] # "807" ko ulta karke "708" kar diya
        
        dummy = ListNode(-1)
        tail = dummy
        
        for char in sum_str:
            tail.next = ListNode(int(char))
            tail = tail.next
            
        return dummy.next
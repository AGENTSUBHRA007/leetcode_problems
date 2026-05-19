# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        
        
        curr = list1
        while curr:
            arr1.append(curr.val)
            curr = curr.next
            
        curr = list2
        while curr:
            arr2.append(curr.val)
            curr = curr.next
        
        m = len(arr1)
        n = len(arr2)
        result = []
        
        
        i = 0 
        j = 0 

        # 2. Comparison Loop
        while m > 0 and n > 0:
        
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                m -= 1
                i += 1
            else:
                result.append(arr2[j])
                n -= 1
                j += 1
                
        
        while m > 0:
            result.append(arr1[i])
            m -= 1
            i += 1
            
        
        while n > 0:
            result.append(arr2[j])
            n -= 1
            j += 1
            
        
        dummy = ListNode(-1)
        tail = dummy
        for value in result:
            tail.next = ListNode(value)
            tail = tail.next
            
        return dummy.next
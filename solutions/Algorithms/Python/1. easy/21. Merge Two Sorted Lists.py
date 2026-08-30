class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    res = ListNode()
    respoint = res
    while list1 !=  None and list2 != None:
        if list1.val < list2.val:
            res.next, list1 = ListNode(list1.val), list1.next
        else:
            res.next, list2 = ListNode(list2.val), list2.next
        res = res.next      
    if list1 or list2:
        res.next = list1 if list1 else list2
    return respoint.next

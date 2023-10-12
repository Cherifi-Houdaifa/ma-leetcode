class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(list1: ListNode | None, list2: ListNode | None):
    result: ListNode = ListNode()
    
    
            
        
            
    # print(list1)


test1 = ListNode(1, ListNode(2, ListNode(4)))

def test(l: ListNode | None):
    if l == None:
        return
    print(l.val)
    test(l.next)
    print(
test2 = ListNode(1, ListNode(2, ListNode(4)))
# main(test1, test2)
test(test1)

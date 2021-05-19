class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Extract values
    l1_vals = ''
    l2_vals = ''
    while l1.next != None:
        l1_vals += str(l1.val)
        l1 = l1.next
    while l2.next != None:
        l2_vals += str(l2.val)
        l2 = l2.next
    l1_vals += str(l1.val)
    l2_vals += str(l2.val)
    
    # Get solution values
    sol_vals = str(int(l1_vals) + int(l2_vals))
    print(sol_vals)
    # Create final node
    sol = ListNode(None)
    cur = sol
    for i in range(len(sol_vals)):
        cur.next = ListNode(int(sol_vals[i]))
        cur = next
    return sol.next





l1 = ListNode(2, ListNode(4,ListNode(3,None)))
l2 = ListNode(5, ListNode(6,ListNode(4,None)))

print(addTwoNumbers(l1, l2))
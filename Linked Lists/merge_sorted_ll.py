'''
Merge Sorted Linked Lists

Input: 1 -> 2 -> 4, 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

=========================================
Simple solution with pointers manipulation (just change the pointers of the old nodes, if there is smaller node than the old one).
    Time Complexity:    O(N + M)
    Space Complexity:   O(1)        - working with the same old nodes (no extra space)
'''


############
# Solution #
############

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_two_sorted_ll(l1, l2):
    result = ListNode(-1)
    pointer = result

    while (l1 is not None) and (l2 is not None):
        if l1.val < l2.val:
            pointer.next = l1
            l1 = l1.next
        else:
            pointer.next = l2
            l2 = l2.next
        
        pointer = pointer.next
        
    if l1 is not None:
        pointer.next = l1

    if l2 is not None:
        pointer.next = l2
    
    return result.next


###########
# Testing #
###########

def build_ll(l):
    if l == None:
        return None

    ll = ListNode(l[0])
    pt = ll

    for i in range(1, len(l)):
        pt.next = ListNode(l[i])
        pt = pt.next

    return ll

def print_ll(l):
    while l != None:
        print(l.val)
        l = l.next
    print()

# Test 1
# Correct result => 1 2 3 4 5 6 7 8 9
a = build_ll([1, 2, 3, 4, 5])
b = build_ll([6, 7, 8, 9])
print_ll(merge_two_sorted_ll(a, b))

# Test 2
# Correct result => 1 2 3 4 5 6 7
a = build_ll([1, 3, 5])
b = build_ll([2, 4, 6, 7])
print_ll(merge_two_sorted_ll(a, b))

# Test 3
# Correct result => 1 1 2 3 4 4
a = build_ll([1, 2, 4])
b = build_ll([1, 3, 4])
print_ll(merge_two_sorted_ll(a, b))
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next


# dummy node
#    ↓
# compare list1 and list2
#    ↓
# attach smaller node
#    ↓
# move that list
#    ↓
# move node
#    ↓
# attach leftovers




# Example:
# list1 = 1 -> 2 -> 4
# list2 = 1 -> 3 -> 4

# Start:
# dummy
# node = dummy

# Compare:
# 1 and 1

# Since 1 < 1 is false, take from list2:
# dummy -> 1

# Then compare:
# list1 = 1
# list2 = 3

# Take 1 from list1:
# dummy -> 1 -> 1

# Continue:
# 2 < 3

# Take 2:
# 1 -> 1 -> 2

# Then:
# 4 vs 3

# Take 3.

# Eventually one list becomes empty.

# This line:
# node.next = list1 or list2


# means:
# Attach whichever list still has nodes left.

# For example, if:
# list1 = 4
# list2 = None

# then:
# list1 or list2


# returns list1.
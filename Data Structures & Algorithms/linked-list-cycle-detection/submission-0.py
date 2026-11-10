# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Example:
# 1 -> 2 -> 3 -> 4
#      ^         |
#      |_________|

# Start:
# slow = 1
# fast = 1

# Move:
# slow = 2
# fast = 3

# Move again:
# slow = 3
# fast = 2

# Eventually they meet inside the cycle.

# The important condition is:
# while fast and fast.next:


# We check both because this line:
# fast = fast.next.next


# needs two nodes available.

# If fast reaches None, there is no cycle.

# Easy rule to remember:
# slow = 1 step
# fast = 2 steps

# If slow == fast
# → cycle exists

# If fast reaches None
# → no cycle

# Time: O(n)
# Space: O(1)








# This is the classic Floyd’s Cycle Detection pattern, also called slow and fast pointers.

# The idea:
# Slow moves 1 step.
# Fast moves 2 steps.
# If there is a cycle, they will eventually meet.        
class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers together
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next




# This is a classic two-pointer linked list problem.

# The best pattern is:
# Move fast pointer n steps ahead, then move slow and fast together.
# When fast reaches the end, slow will be just before the node we need to remove.

# Using a dummy node makes removing the head easy.
# For:
# head = [1,2,3,4]
# n = 2

# Start:
# dummy -> 1 -> 2 -> 3 -> 4
# slow = dummy
# fast = dummy

# Move fast by:
# n + 1 = 3 steps

# So:
# fast = 3
# slow = dummy

# Now move both:
# slow = 1
# fast = 4

# Then:
# slow = 2
# fast = None

# Now slow is just before the node to delete:
# 1 -> 2 -> 3 -> 4
#      ↑    ↑
#    slow  remove

# Remove it:
# slow.next = slow.next.next


# So:
# 2.next = 4

# Final:
# 1 -> 2 -> 4

# Output:
# [1,2,4]

# The dummy node is important for this case:
# head = [1,2]
# n = 2

# We need to remove the head.

# With dummy:
# dummy -> 1 -> 2

# slow stays at dummy, so:
# slow.next = slow.next.next


# becomes:
# dummy -> 2

# and returning:
# return dummy.next


# gives:
# [2]

# Easy rule to remember:
# dummy
#   ↓
# fast goes n + 1 steps ahead
#   ↓
# move slow + fast together
#   ↓
# fast reaches None
#   ↓
# slow is before node to delete
#   ↓
# slow.next = slow.next.next

# Time: O(n)
# Space: O(1)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # 1. Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list
        second = slow.next
        slow.next = None

        # Reverse second half
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # prev is now the head of reversed second half
        second = prev
        first = head

        # 3. Merge the two lists
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2




#   This problem uses 3 linked-list patterns together:
# 1. Find the middle using slow/fast pointers
# 2. Reverse the second half
# 3. Merge the two halves alternately    

# For:
# 2 -> 4 -> 6 -> 8 -> 10

# 1. Find middle
# Using:
# slow = headfast = head.next


# Slow moves 1 step and fast moves 2.

# Eventually:
# slow = 6

# Split:
# First half:
# 2 -> 4 -> 6

# Second half:
# 8 -> 10

# 2. Reverse second half
# 8 -> 10

# becomes:
# 10 -> 8

# Now:
# first  = 2 -> 4 -> 6

# second = 10 -> 8

# 3. Merge alternately
# Take from first:
# 2

# Then second:
# 2 -> 10

# Then first:
# 2 -> 10 -> 4

# Then second:
# 2 -> 10 -> 4 -> 8

# Finally:
# 2 -> 10 -> 4 -> 8 -> 6

# Output:
# [2,10,4,8,6]

# The merging section is especially important:
# temp1 = first.nexttemp2 = second.nextfirst.next = secondsecond.next = temp1first = temp1second = temp2


# We save both next nodes first because we're about to change the pointers.
# Easy rule to remember
# Find middle
#     ↓
# Split
#     ↓
# Reverse second half
#     ↓
# Merge alternately

# So Reorder List is basically:
# Middle + Reverse + Merge

# Time: O(n)
# Space: O(1)
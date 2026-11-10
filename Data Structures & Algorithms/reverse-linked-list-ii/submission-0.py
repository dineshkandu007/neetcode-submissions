class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node before 'left'
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # First node in the section to reverse
        current = prev.next

        # Move nodes one by one to the front of the section
        for _ in range(right - left):
            next_node = current.next

            # Remove next_node
            current.next = next_node.next

            # Put next_node after prev
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
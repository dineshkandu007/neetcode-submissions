from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()   # stores indices
        left = 0

        for right in range(len(nums)):

            # Remove smaller values from the back
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add current index
            q.append(right)

            # Remove index if it is outside the window
            if q[0] < left:
                q.popleft()

            # Once window size reaches k, record max
            if right - left + 1 == k:
                result.append(nums[q[0]])
                left += 1

        return result
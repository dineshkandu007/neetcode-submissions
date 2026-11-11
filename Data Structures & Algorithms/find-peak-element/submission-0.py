class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Uphill: peak is on the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            # Downhill: peak is at mid or on the left
            else:
                right = mid

        return left
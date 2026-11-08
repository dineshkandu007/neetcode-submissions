class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # If k <= 1, no positive-product subarray can be < k
        if k <= 1:
            return 0

        # Left side of the window
        left = 0

        # Product of current window
        product = 1

        # Number of valid subarrays
        count = 0

        # Move right pointer through the array
        for right in range(len(nums)):

            # Include current number in product
            product *= nums[right]

            # If product is too large, shrink from left
            while product >= k:
                product //= nums[left]
                left += 1

            # Count all valid subarrays ending at right
            count += right - left + 1

        return count
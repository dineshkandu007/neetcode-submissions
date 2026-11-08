class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # If k <= 1, no positive-product subarray can be < k
        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):
            # Add current number into the window product
            product *= nums[right]

            # Shrink window until product becomes < k
            while product >= k:
                product //= nums[left]
                left += 1

            # Number of valid subarrays ending at right
            count += right - left + 1

        return count
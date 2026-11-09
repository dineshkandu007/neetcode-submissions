class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Best sum ending at current position
        current_sum = nums[0]

        # Best sum found overall
        max_sum = nums[0]

        # Start from second element
        for i in range(1, len(nums)):
            # Either start new subarray
            # or continue previous one
            current_sum = max(
                nums[i],
                current_sum + nums[i]
            )

            # Update overall maximum
            max_sum = max(max_sum, current_sum)

        return max_sum
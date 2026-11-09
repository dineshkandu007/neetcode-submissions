class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            # Add current number to the window
            current_sum += nums[right]

            # While current window satisfies the target
            while current_sum >= target:
                # Calculate current window length
                window_length = right - left + 1

                # Keep the smallest length
                min_length = min(min_length, window_length)

                # Remove left element and shrink window
                current_sum -= nums[left]
                left += 1

        # If no valid window was found
        return 0 if min_length == float("inf") else min_length
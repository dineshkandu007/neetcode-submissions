class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Sum of all numbers
        total_sum = sum(nums)

        # Sum of numbers to the left of current index
        left_sum = 0

        # Check each index
        for i in range(len(nums)):

            # Sum of numbers to the right
            right_sum = total_sum - left_sum - nums[i]

            # If left and right sums are equal
            if left_sum == right_sum:
                return i

            # Add current number to left sum
            left_sum += nums[i]

        # No pivot index found
        return -1
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0

        # prefix sum 0 has appeared once
        prefix_count = {0: 1}

        for num in nums:
            # Update running sum
            prefix_sum += num

            # We need a previous prefix sum equal to:
            needed = prefix_sum - goal

            # Add how many times that prefix sum appeared
            count += prefix_count.get(needed, 0)

            # Store current prefix sum
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count
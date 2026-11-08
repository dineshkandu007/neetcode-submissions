class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize result and current prefix sum
        res = 0
        cur_sum = 0

        # Prefix sum frequency map
        # 0 has appeared once before we start
        prefix_sums = {0: 1}

        # Loop through each number
        for num in nums:
            # Add current number to running sum
            cur_sum += num

            # We need a previous prefix sum equal to cur_sum - k
            diff = cur_sum - k

            # Add how many times that prefix sum has appeared
            res += prefix_sums.get(diff, 0)

            # Store/update current prefix sum frequency
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

        return res
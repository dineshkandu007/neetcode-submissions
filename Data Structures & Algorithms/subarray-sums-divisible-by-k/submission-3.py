class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0

        # remainder 0 has appeared once before starting
        remainder_count = {0: 1}

        for num in nums:
            # Add current number to prefix sum
            prefix_sum += num

            # Find remainder
            remainder = prefix_sum % k

            # If same remainder appeared before,
            # those positions form valid subarrays
            count += remainder_count.get(remainder, 0)

            # Store/update remainder frequency
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0

        # remainder -> first index where it appeared
        remainder_index = {0: -1}

        for i, num in enumerate(nums):
            # Add current number to prefix sum
            prefix_sum += num

            # Get remainder
            remainder = prefix_sum % k

            # If this remainder appeared before
            if remainder in remainder_index:

                # Check subarray length is at least 2
                if i - remainder_index[remainder] >= 2:
                    return True

            else:
                # Store only the first occurrence
                remainder_index[remainder] = i

        return False
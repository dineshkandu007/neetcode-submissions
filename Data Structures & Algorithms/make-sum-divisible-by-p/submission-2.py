class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)

        # Remainder we need to remove
        need = total_sum % p

        # Already divisible
        if need == 0:
            return 0

        prefix_sum = 0

        # remainder -> latest index
        remainder_index = {0: -1}

        result = len(nums)

        for i, num in enumerate(nums):

            # Running prefix sum
            prefix_sum += num

            # Current remainder
            current_rem = prefix_sum % p

            # We want:
            # current_rem - previous_rem = need
            target_rem = (current_rem - need) % p

            # If such previous remainder exists
            if target_rem in remainder_index:

                # Length of subarray we can remove
                length = i - remainder_index[target_rem]

                # Keep smallest length
                result = min(result, length)

            # Store latest index for this remainder
            remainder_index[current_rem] = i

        # Cannot remove the entire array
        if result == len(nums):
            return -1

        return result
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        prefix_sum = 0
        even_count = 1  # empty prefix
        odd_count = 0

        result = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                # Current prefix is even.
                # Need a previous odd prefix to make odd subarray sum.
                result += odd_count
                even_count += 1
            else:
                # Current prefix is odd.
                # Need a previous even prefix to make odd subarray sum.
                result += even_count
                odd_count += 1

            result %= MOD

        return result
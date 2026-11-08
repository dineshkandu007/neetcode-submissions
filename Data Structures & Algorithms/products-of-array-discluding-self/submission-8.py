class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Result array
        res = [1] * n

        # Product of everything to the left
        prefix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Product of everything to the right
        suffix = 1

        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
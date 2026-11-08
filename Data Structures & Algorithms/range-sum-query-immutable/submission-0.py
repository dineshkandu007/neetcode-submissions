class NumArray:

    def __init__(self, nums: List[int]):
        # prefix[i] stores sum of first i elements
        self.prefix = [0]

        # Build prefix sum array
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        # Sum from left to right inclusive
        return self.prefix[right + 1] - self.prefix[left]
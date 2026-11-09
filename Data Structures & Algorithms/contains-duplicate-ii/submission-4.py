class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, x in enumerate(nums):
            if i > k:
                window.discard(nums[i - k - 1])   # drop element that fell out of range
            if x in window:
                return True
            window.add(x)
        return False
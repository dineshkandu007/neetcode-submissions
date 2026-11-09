class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):

            # If current number is already in the window,
            # duplicate exists within distance k
            if nums[i] in window:
                return True

            # Add current number to the window
            window.add(nums[i])

            # Keep only the last k elements in the window
            if len(window) > k:
                window.remove(nums[i - k])
        return False

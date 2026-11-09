class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        # Keep shrinking until window size becomes k
        while right - left + 1 > k:

            # Compare distance from x
            left_distance = abs(arr[left] - x)
            right_distance = abs(arr[right] - x)

            # Remove the farther element
            if left_distance <= right_distance:
                right -= 1
            else:
                left += 1

        return arr[left:right + 1]
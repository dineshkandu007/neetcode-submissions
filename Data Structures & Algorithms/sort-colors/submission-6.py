class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for where the next 0 should be placed
        low = 0

        # Pointer for the current element we are checking
        mid = 0

        # Pointer for where the next 2 should be placed
        high = len(nums) - 1

        # Keep checking until mid passes high
        while mid <= high:

            # If current value is 0
            if nums[mid] == 0:

                # Swap current 0 with the value at low
                nums[low], nums[mid] = nums[mid], nums[low]

                # Move low forward because this position now has correct 0
                low += 1

                # Move mid forward to check next element
                mid += 1

            # If current value is 1
            elif nums[mid] == 1:

                # 1 is already in the correct middle section
                # Just move mid forward
                mid += 1

            # Otherwise current value is 2
            else:

                # Swap current 2 with the value at high
                nums[mid], nums[high] = nums[high], nums[mid]

                # Move high backward because this position now has correct 2
                high -= 1

                # Do NOT move mid here
                # because the new value swapped into mid still needs to be checked
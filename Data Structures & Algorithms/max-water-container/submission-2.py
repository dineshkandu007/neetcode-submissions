class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Start left pointer from the beginning
        left = 0

        # Start right pointer from the end
        right = len(heights) - 1

        # Store the maximum water found so far
        max_water = 0

        # Continue until both pointers meet
        while left < right:

            # Distance between the two bars
            width = right - left

            # Water height depends on the shorter bar
            height = min(heights[left], heights[right])

            # Calculate current container area
            water = width * height

            # Update maximum water if current area is bigger
            max_water = max(max_water, water)

            # If left bar is shorter
            if heights[left] < heights[right]:

                # Move left pointer to the right
                left += 1

            else:
                # Otherwise move right pointer to the left
                right -= 1

        # Return the maximum water found
        return max_water
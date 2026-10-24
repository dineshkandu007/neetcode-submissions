class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        #Initialize Two Pointers
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        #while loop to trap water between bars
        while l < r:
            #process the side with the smaller max wall
            if leftMax < rightMax:
                l += 1
                #update tallest wall seen from the left
                leftMax = max(leftMax, height[l])
                #water trapped at this bar
                res += leftMax - height[l]
            else:
                r -= 1
                #update tallest wall seen from the right
                rightMax = max(rightMax, height[r])
                #water trapped at this bar
                res += rightMax - height[r]

        return res
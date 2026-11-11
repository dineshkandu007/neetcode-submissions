class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first():
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid

                    # Found target, but search further left
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return answer

        def find_last():
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid

                    # Found target, but search further right
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return answer

        return [find_first(), find_last()]
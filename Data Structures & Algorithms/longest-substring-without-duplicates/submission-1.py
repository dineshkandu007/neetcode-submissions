class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):

            # Remove characters until duplicate is gone
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            # Add current character
            chars.add(s[right])

            # Update longest window length
            max_length = max(max_length, right - left + 1)

        return max_length
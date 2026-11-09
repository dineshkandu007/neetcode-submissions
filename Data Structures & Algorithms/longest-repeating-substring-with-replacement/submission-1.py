class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):

            # Count current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Highest frequency inside current window
            max_freq = max(max_freq, count[s[right]])

            # If replacements needed are more than k,
            # shrink window from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update longest valid window
            max_length = max(max_length, right - left + 1)

        return max_length
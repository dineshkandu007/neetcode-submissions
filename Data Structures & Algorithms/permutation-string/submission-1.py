class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        # Build count for s1
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        left = 0

        for right in range(len(s2)):
            # Add current character to window
            window_count[s2[right]] = window_count.get(s2[right], 0) + 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1

                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                left += 1

            # Compare counts
            if window_count == s1_count:
                return True

        return False
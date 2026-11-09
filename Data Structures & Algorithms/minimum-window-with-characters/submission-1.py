class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Count required characters
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        # Number of required characters currently satisfied
        have = 0

        # Number of distinct required characters
        need_count = len(need)

        left = 0

        # Store best window
        result = [-1, -1]
        min_length = float("inf")

        for right in range(len(s)):
            char = s[right]

            # Add current character to window
            window[char] = window.get(char, 0) + 1

            # If this character now satisfies its required count
            if char in need and window[char] == need[char]:
                have += 1

            # Window contains everything we need
            while have == need_count:

                # Current window length
                window_length = right - left + 1

                # Save smaller window
                if window_length < min_length:
                    min_length = window_length
                    result = [left, right]

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                # If removing it makes the window invalid
                if (
                    left_char in need
                    and window[left_char] < need[left_char]
                ):
                    have -= 1

                # Move left pointer
                left += 1

        start, end = result

        if min_length == float("inf"):
            return ""

        return s[start:end + 1]
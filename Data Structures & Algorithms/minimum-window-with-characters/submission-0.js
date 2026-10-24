class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
 minWindow(s, t) {
        if (t.length > s.length) return "";

        const need = {};
        for (let c of t) {
            need[c] = (need[c] || 0) + 1;
        }

        let left = 0;
        let required = t.length;
        let minLen = Infinity;
        let start = 0;

        for (let right = 0; right < s.length; right++) {
            const char = s[right];

            if (need[char] > 0) required--;
            need[char]--;

            // Try to shrink the window
            while (required === 0) {
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                start = left;
            }

            const leftChar = s[left];
            need[leftChar]++;
            if (need[leftChar] > 0) required++;

            left++;
            }
        }

        return minLen === Infinity ? "" : s.slice(start, start + minLen);
        }

}

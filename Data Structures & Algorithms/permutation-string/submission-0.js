class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
 checkInclusion(s1, s2) {
  if (s1.length > s2.length) return false;

  const freq = new Array(26).fill(0);

  // Count characters in s1
  for (let ch of s1) {
    freq[ch.charCodeAt(0) - 97]++;
  }

  let left = 0;
  let right = 0;
  let remaining = s1.length;

  while (right < s2.length) {
    const rIdx = s2.charCodeAt(right) - 97;

    // If char needed, reduce remaining count
    if (freq[rIdx] > 0) remaining--;
    freq[rIdx]--;

    right++;

    // If window size exceeds s1 length, shrink from left
    if (right - left > s1.length) {
      const lIdx = s2.charCodeAt(left) - 97;
      if (freq[lIdx] >= 0) remaining++;
      freq[lIdx]++;
      left++;
    }

    // If all characters matched
    if (remaining === 0) return true;
  }

  return false;
}

}

class Solution {
    /**
     * @param {number[]} nums1
     * @param {number} m
     * @param {number[]} nums2
     * @param {number} n
     * @return {void} Do not return anything, modify nums1 in-place instead.
     */
 merge(nums1, m, nums2, n) {

  // Points to the last index of nums1 (where the largest value should go)
  let last = m + n - 1;

  // Pointer for the last valid element in nums1
  let i = m - 1;

  // Pointer for the last element in nums2
  let j = n - 1;

  // Continue until all elements of nums2 are merged
  while (j >= 0) {

    // If nums1 still has elements AND
    // the current element in nums1 is greater than nums2's element
    if (i >= 0 && nums1[i] > nums2[j]) {

      // Place nums1[i] at the end position
      nums1[last] = nums1[i];

      // Move nums1 pointer left
      i--;

    } else {

      // Place nums2[j] at the end position
      nums1[last] = nums2[j];

      // Move nums2 pointer left
      j--;
    }

    // Move the last pointer left after placing a value
    last--;
  }
}

}
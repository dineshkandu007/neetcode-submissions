class Solution {
    /**
     * @param {number[]} arr
     * @param {number} k
     * @param {number} x
     * @return {number[]}
     */
 findClosestElements(arr, k, x) {
  let left = 0;
  let right = arr.length - k;

  // Binary search for the best window start
  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (x - arr[mid] > arr[mid + k] - x) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return arr.slice(left, left + k);
}

}

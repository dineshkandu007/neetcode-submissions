class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    searchInsert(nums, target) {
        let res = nums.length;
        let l = 0,
            r = nums.length - 1;
        while (l <= r) {
            const mid = Math.floor((l + r) / 2);
            if (nums[mid] === target) {
                return mid;
            }
            if (nums[mid] > target) {
                res = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return res;
    }
}
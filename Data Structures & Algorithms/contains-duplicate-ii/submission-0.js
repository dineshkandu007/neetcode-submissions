class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    // containsNearbyDuplicate(nums, k) {
    //     // const map = new Map();

    //     // for (let i = 0; i < nums.length; i++) {
    //     //     if (map.has(nums[i]) && i - map.get(nums[i]) <= k) {
    //     //         return true;
    //     //     }
    //     //     map.set(nums[i], i);
    //     // }

    //     // return false;
    // }

    containsNearbyDuplicate(nums, k) {
        let window = new Set();
        let L = 0;

        for (let R = 0; R < nums.length; R++) {
            if (R - L > k) {
                window.delete(nums[L]);
                L++;
            }
            if (window.has(nums[R])) {
                return true;
            }
            window.add(nums[R]);
        }
        return false;
    }
}

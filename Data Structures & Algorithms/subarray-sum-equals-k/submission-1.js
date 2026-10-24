class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums, k) {
         let count = 0;
        let sum = 0;
        const map = { 0: 1 };

        for (let num of nums) {
            sum += num;

            if (map[sum - k] !== undefined) {
            count += map[sum - k];
            }

            map[sum] = (map[sum] || 0) + 1;
        }

        return count;
    }
}

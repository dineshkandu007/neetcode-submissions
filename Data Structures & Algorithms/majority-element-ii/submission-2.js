class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums) {
        const count = new Map();
        for (const num of nums) {
            count.set(num, (count.get(num) || 0) + 1);
        }

        const res = [];
        for (const [key, value] of count.entries()) {
            if (value > Math.floor(nums.length / 3)) {
                res.push(key);
            }
        }

        return res;
    }
}

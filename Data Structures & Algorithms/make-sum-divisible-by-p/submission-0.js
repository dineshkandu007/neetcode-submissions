class Solution {
    /**
     * @param {number[]} nums
     * @param {number} p
     * @return {number}
     */
    minSubarray(nums, p) {
        const n = nums.length;
        let totSum = nums.reduce((a, b) => a + b, 0);

        if (totSum % p === 0) return 0;

        for (let l = 1; l < n; l++) {
            let curSum = 0;
            for (let i = 0; i < n; i++) {
                curSum += nums[i];
                if (i >= l) curSum -= nums[i - l];

                const remainSum = totSum - curSum;
                if (remainSum % p === 0) return l;
            }
        }

        return -1;
    }
}

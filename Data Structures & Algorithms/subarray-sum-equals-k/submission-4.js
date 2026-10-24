class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums, k) {
        let res=0;
        let curSum=0;
        const prefixSums = new Map();
        prefixSums.set(0, 1);

        for(let i=0;i<nums.length;i++){
            /**Add it to curSum. */
            curSum+=nums[i];
            let diff= curSum-k /**Compute diff = curSum - k. */
            res += prefixSums.get(diff) || 0; /**Add prefixSums[diff] to res (counts subarrays ending here with sum k). */
            prefixSums.set(curSum, (prefixSums.get(curSum) || 0) + 1); /**Increment prefixSums[curSum] by 1. */
        }
        return res;
    }
}

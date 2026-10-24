class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    checkSubarraySum(nums, k) {
        for(let i=0; i<nums.length-1;i++){
            let sum=nums[i];
            for(let j=i+1;j<nums.length;j++){
                sum+=nums[j];
                if(sum%k==0) return true
            }
        }
        return false
    }
}

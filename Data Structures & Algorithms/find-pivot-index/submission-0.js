class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    pivotIndex(nums) {
        const n = nums.length;
        let prefixSum=new Array(n+1).fill(0);

        for(let i=0; i<n; i++){
            prefixSum[i+1]=prefixSum[i]+nums[i]
        }

        for(let i=0; i<n;i++){
            const leftSum=prefixSum[i];
            const rightSum= prefixSum[n]-prefixSum[i+1];
            if(leftSum === rightSum){
                return i;
            }
        }
        return -1
    }
}

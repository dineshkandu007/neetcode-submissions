class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraysDivByK(nums, k) {
        const n = nums.length;
        let res=0;

        for(let i=0;i<n;i++){
            let curSum=0;
            for(let j=i;j<n;j++){
                curSum+=nums[j];
                if(curSum%k===0){
                    res++
                }
            }
        }
        return res;
    }
}

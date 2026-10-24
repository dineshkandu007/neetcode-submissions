class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    pivotIndex(nums) {
        let total=0;
        for(let num of nums){
            total+=num;
        }

        let leftSum=0
        for(let i=0; i<nums.length;i++){
            let rightSum= total-leftSum-nums[i]
            if(leftSum === rightSum){
                return i;
            }
            leftSum+=nums[i]
        }
        return -1
    }
}

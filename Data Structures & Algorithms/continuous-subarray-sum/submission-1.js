class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    checkSubarraySum(nums, k) {
        const reminder = new Map();
        reminder.set(0,-1);
        let total = 0;

        for(let i=0;i<nums.length;i++){
            total+=nums[i];
            let r=total%k;
            if(!reminder.has(r)){
                reminder.set(r,i);
            } else if(i-reminder.get(r)>1){
                return true
            }
        }
        return false
    }
}

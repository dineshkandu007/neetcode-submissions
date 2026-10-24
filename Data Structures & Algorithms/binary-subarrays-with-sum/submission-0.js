class Solution {
    /**
     * @param {number[]} nums
     * @param {number} goal
     * @return {number}
     */
    numSubarraysWithSum(nums, goal) {
        let prefixSum=0;
        let res=0;
        const count = new Map();
        count.set(0,1);

        for(const num of nums){
            prefixSum +=num;
            res+=count.get(prefixSum-goal) || 0;
            count.set(prefixSum,(count.get(prefixSum) || 0) +1)
        }
        return res;
    }
}

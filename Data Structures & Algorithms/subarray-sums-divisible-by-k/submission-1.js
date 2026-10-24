class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraysDivByK(nums, k) {
       let prefixSum = 0, res = 0;
       const prefixCnt = new Map();
       prefixCnt.set(0,1);

       for(let n of nums){
        prefixSum +=n;
        let remain = prefixSum%k;
        if(remain<0) remain+=k;

        res+=prefixCnt.get(remain) || 0;
        prefixCnt.set(remain, (prefixCnt.get(remain) || 0) + 1);
       }
       return res;
    }
}

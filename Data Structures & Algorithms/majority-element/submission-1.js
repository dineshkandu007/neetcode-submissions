class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        const freq = {};
        for (const x of nums) {
            freq[x] = (freq[x] || 0) + 1;
            console.log("freq[x]",x,freq[x])
            if (freq[x] > nums.length / 2) return x;
        }
        return null;
    }
}

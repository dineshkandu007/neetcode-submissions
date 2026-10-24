class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        //one way
        // let set = new Set(nums);
        // return nums.length!==set.size ? true : false 

        //second way
        const seen = new Set();
        for (const num of nums) {
            if (seen.has(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;

        //third way
        // nums.sort((a, b) => a - b);
        // for (let i = 1; i < nums.length; i++) {
        //     if (nums[i] === nums[i - 1]) {
        //         return true;
        //     }
        // }
        // return false;
    }
}

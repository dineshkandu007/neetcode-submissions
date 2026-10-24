class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    firstMissingPositive(nums) {
        const set = new Set(nums);
        let i = 1;

        while (true) {
            if (!set.has(i)) return i;
            i++;
        }
    }
}

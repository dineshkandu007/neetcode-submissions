class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = new Map();
        for (const x of nums) freq.set(x, (freq.get(x) ?? 0) + 1);

        return [...freq.entries()]               // [num, count]
            .sort((a, b) => b[1] - a[1])           // by count desc
            .slice(0, k)
            .map(([num]) => num);
    }
}

class Solution {
    /**
     * @param {number[]} arr
     * @return {number}
     */
    numOfSubarrays(arr) {
        const n = arr.length;
        let res = 0;
        const mod = 1e9 + 7;

        for (let i = 0; i < n; i++) {
            let curSum = 0;
            for (let j = i; j < n; j++) {
                curSum += arr[j];
                if (curSum % 2 !== 0) {
                    res = (res + 1) % mod;
                }
            }
        }

        return res;
    }
}

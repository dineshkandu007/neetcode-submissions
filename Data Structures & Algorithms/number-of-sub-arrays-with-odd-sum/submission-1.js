class Solution {
    /**
     * @param {number[]} arr
     * @return {number}
     */
    numOfSubarrays(arr) {
        let curSum = 0,
            oddCnt = 0,
            evenCnt = 0,
            res = 0;
        const MOD = 1e9 + 7;

        for (let n of arr) {
            curSum += n;
            if (curSum % 2 !== 0) {
                res = (res + 1 + evenCnt) % MOD;
                oddCnt++;
            } else {
                res = (res + oddCnt) % MOD;
                evenCnt++;
            }
        }

        return res;
    }
}

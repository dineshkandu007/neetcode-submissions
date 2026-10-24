class Solution {
    /**
     * @param {number[]} cardPoints
     * @param {number} k
     * @return {number}
     */
    maxScore(cardPoints, k) {
        let n = cardPoints.length;

        let prefix = new Array(n + 1).fill(0);
        for (let i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + cardPoints[i];
        }

        let suffix = new Array(n + 1).fill(0);
        for (let i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + cardPoints[i];
        }

        let res = 0;
        for (let left = 0; left <= k; left++) {
            let right = k - left;
            res = Math.max(res, prefix[left] + suffix[n - right]);
        }

        return res;
    }
}

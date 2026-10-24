class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {string}
     */
    mergeAlternately(word1, word2) {
        const n = word1.length,
            m = word2.length;
        const res = [];
        for (let i = 0; i < m || i < n; i++) {
            if (i < n) {
                res.push(word1.charAt(i));
            }
            if (i < m) {
                res.push(word2.charAt(i));
            }
        }
        return res.join('');
    }
}
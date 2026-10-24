class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        if (!strs || strs.length === 0) return "";

        let prefix = "";
        for (let i = 0; i < strs[0].length; i++) {
            const char = strs[0][i];

            for (let j = 1; j < strs.length; j++) {
            // if jth string is too short or char doesn't match → done
                if (i >= strs[j].length || strs[j][i] !== char) {
                    return prefix;
                }
            }

            // all strings had the same char at i
            prefix += char;
        }

        return prefix;
    }
}

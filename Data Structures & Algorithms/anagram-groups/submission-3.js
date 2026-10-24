class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const res = {};
        for (let s of strs) {
            const sortedS = s.split('').sort().join('');
            console.log("sortedS",sortedS);
            if (!res[sortedS]) {
                res[sortedS] = [];
            }
            console.log("s",s);
            res[sortedS].push(s);
            console.log("res",res);
        }
        return Object.values(res);
    }
}

class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();             // key: sorted string -> value: list of anagrams
        for (const s of strs) {
            const key = s.split('').sort().join(''); // canonical form
            if (!map.has(key)) map.set(key, []);
            map.get(key).push(s);
        }
        return Array.from(map.values());
    }
}

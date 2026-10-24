class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();             // key: sorted string -> value: list of anagrams
        console.log("map",map)
        for (const s of strs) {
            console.log("s",s)
            const key = s.split('').sort().join(''); // canonical form
            console.log("key",key, map.has(key))
            if (!map.has(key)) { 
                map.set(key, []);
            }
            map.get(key).push(s);
        }
        return Array.from(map.values());
    }
}

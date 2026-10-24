class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
         let res = 0;
        const store = new Set(nums);
        console.log("store",store)
        for (let num of nums) {
            let streak = 0,
                curr = num;
                 console.log("curr",curr)
            while (store.has(curr)) {
                streak++;
                curr++;
            }
            console.log("curr1",curr)
             console.log("res",res)
              console.log("streak",streak)
            res = Math.max(res, streak);
        }
        return res;
    }
}

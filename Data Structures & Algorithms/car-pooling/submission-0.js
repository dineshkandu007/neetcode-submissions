class Solution {
    /**
     * @param {number[][]} trips
     * @param {number} capacity
     * @return {boolean}
     */
    carPooling(trips, capacity) {
        trips.sort((a,b)=> a[1]-b[1]);

        for(let i=0; i<trips.length;i++){
            let curPass=trips[i][0];
            for(let j=0;j<i;j++){
                if(trips[j][2]>trips[i][1]){
                    curPass+=trips[j][0];
                }
            }
            if(curPass>capacity){
                return false
            }
        }
        return true
    }
}

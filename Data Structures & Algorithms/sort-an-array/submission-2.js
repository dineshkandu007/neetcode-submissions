class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    //Selection sort
    sortArray(arr) {
         for (let i = 0; i < arr.length; i++) {
            let lowest = i;
            for (let j = i + 1; j < arr.length; j++) {
                if (arr[lowest] > arr[j]) {
                    lowest = j;
                }
            }
            if (i !== lowest) {
            // swap the elements
            [arr[i],arr[lowest]] = [arr[lowest], arr[i]];
            }
        }

        return arr;
    }
}

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    sortArray(nums) {
        this.quickSort(nums, 0, nums.length - 1);
        return nums;
    }

    quickSort(arr, left, right) {
        if (left >= right) return;

        const pivotIndex = this.partition(arr, left, right);
        this.quickSort(arr, left, pivotIndex - 1);
        this.quickSort(arr, pivotIndex + 1, right);
    }

    partition(arr, left, right) {
        const pivot = arr[right];
        let i = left;

        for (let j = left; j < right; j++) {
            if (arr[j] < pivot) {
            [arr[i], arr[j]] = [arr[j], arr[i]];
            i++;
            }
        }

        [arr[i], arr[right]] = [arr[right], arr[i]];
        return i;
    }
}

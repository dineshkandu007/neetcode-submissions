class Solution {
    /**
     * @param {number[][]} trips
     * @param {number} capacity
     * @return {boolean}
     */
    carPooling(trips, capacity) {
        const diff = new Array(1001).fill(0);

        for (const [passengers, start, end] of trips) {
            diff[start] += passengers;
            diff[end] -= passengers;
        }

        let currentPassengers = 0;

        for (let i = 0; i < diff.length; i++) {
            currentPassengers += diff[i];

            if (currentPassengers > capacity) {
            return false;
            }
        }

        return true;
    }
    /*pickup  → +passengers
    dropoff → -passengers
    prefix sum → passengers currently inside car*/
}

class Solution {
    /**
     * @param {number[]} people
     * @param {number} limit
     * @return {number}
     */
    numRescueBoats(people, limit) {

        // Step 1: Sort people by weight (ascending order)
        // This allows us to pair the lightest and heaviest people efficiently
        people.sort((a, b) => a - b);

        // Pointer to the lightest person
        let left = 0;

        // Pointer to the heaviest person
        let right = people.length - 1;

        // Counter to track how many boats are used
        let boats = 0;

        // Continue until all people are assigned to boats
        // left <= right handles the case where one person remains
        while (left <= right) {

            // Check if the lightest and heaviest person can share a boat
            if (people[left] + people[right] <= limit) {
                // If they fit together, pair them
                // Move left pointer since the lightest person is used
                left++;
            }

            // The heaviest person always boards a boat
            // Either alone or with the lightest person
            right--;

            // One boat is used in every iteration
            boats++;
        }

        // Return the total number of boats needed
        return boats;
    }
}

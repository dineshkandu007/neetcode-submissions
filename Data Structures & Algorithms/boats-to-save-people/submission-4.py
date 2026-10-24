class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort so lightest and heaviest can be paired with two pointers
        people.sort()
        #Initialize Two Pointers
        l = 0
        r = len(people) - 1
        boats = 0

        #while loop to seat every person
        while l <= r:
            #lightest + heaviest fit together — send both
            if people[l] + people[r] <= limit:
                l += 1
            #heaviest always takes this boat (alone or with lightest)
            r -= 1
            boats += 1

        return boats
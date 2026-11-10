class Solution:
    def intervalIntersection(
        self,
        firstList: List[List[int]],
        secondList: List[List[int]]
    ) -> List[List[int]]:

        i = 0
        j = 0
        result = []

        while i < len(firstList) and j < len(secondList):

            # Current intervals
            first = firstList[i]
            second = secondList[j]

            # Start of overlap
            start = max(first[0], second[0])

            # End of overlap
            end = min(first[1], second[1])

            # If valid overlap exists
            if start <= end:
                result.append([start, end])

            # Move the interval that ends first
            if first[1] < second[1]:
                i += 1
            else:
                j += 1

        return result
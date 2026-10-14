class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        occurrences = set(count.values())
        return len(occurrences) == len(count)
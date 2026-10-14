class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lista = set()
        for num in nums:
            if num not in lista:
                lista.add(num)
            else:
                return True
        return False
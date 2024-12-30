class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        # add l and r, if too large decrease r, if too small increase l
        # time: O(n)
        # space: O(1)
        l = 0
        r = len(numbers) - 1
        while l < r:
            if (numbers[l] + numbers[r] == target):
                return [l+1,r+1]
            elif (numbers[l] + numbers[r] < target):
                l+=1
            elif (numbers[l] + numbers[r] > target):
                r-=1


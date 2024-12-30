class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashset
        # time: O(N)
        # space: O(N)
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort in place
        # time: O(nlogn)
        # space: O(1)
        nums.sort()
        for i in range(1,len(nums)):
            if (nums[i-1] == nums[i]):
                return True

        return False

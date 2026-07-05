class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(k):
            if k<0: return 0
            l = 0
            total = 0
            count = 0

            for r in range(len(nums)):
                total += nums[r]

                while total > k:
                    total -= nums[l]
                    l += 1

                count += r-l+1

            return count

        return helper(goal) - helper(goal-1)
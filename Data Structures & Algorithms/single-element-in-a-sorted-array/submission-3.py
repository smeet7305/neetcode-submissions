class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            # Case 1: mid matches the previous element
            if m > 0 and nums[m] == nums[m - 1]:

                # If mid is odd, the pair is correctly aligned
                if m % 2 == 1:
                    l = m + 1

                # If mid is even, the pairing pattern has shifted
                else:
                    r = m - 2

            # Case 2: mid matches the next element
            elif m < len(nums) - 1 and nums[m] == nums[m + 1]:

                # If mid is even, the pair is correctly aligned
                if m % 2 == 0:
                    l = m + 2

                # If mid is odd, the pairing pattern has shifted
                else:
                    r = m - 1

            # Case 3: mid matches neither neighbour
            else:
                return nums[m]

        return -1
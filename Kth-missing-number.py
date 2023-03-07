# https://leetcode.com/problems/kth-missing-positive-number/
class Solution(object):
    def missing(self, arr, k):
        n = 1
        ans = 0
        while 0 < k:
            if n in arr:
                pass
            else:
                ans = n
                k -= 1
            n += 1
        return ans


"""TEST CASES
a = [2, 3, 4, 7, 11]
b = 5

a = [1, 2, 3, 4]
b = 2

Returns should be 9, and 6
"""

a = [1, 2, 3, 4]
b = 2
Solution = Solution()
print(Solution.missing(a, b))

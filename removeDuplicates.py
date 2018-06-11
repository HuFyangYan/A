#coding:utf8
# class Solution(object):
    # def removeDuplicates(self, A):
    #     if not A:
    #         return 0
    #     newTail = 0

    #     for i in range(1, len(A)):
    #         if (A[i] != A[newTail]):
    #             newTail += 1
    #             A[newTail] = A[i]
    #     return newTail + 1

from collections import OrderedDict
class Solution(object):
    def removeDuplicates(self, nums):

        nums[:] =  OrderedDict.fromkeys(nums).keys()
        return len(nums)

nums = [1, 2, 3, 1]
result = Solution()
print(result.removeDuplicates([1, 2, 3, 1]))
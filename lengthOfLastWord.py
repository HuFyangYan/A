#coding:utf8
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.rstrip(' ').split(' ')[-1])

s = 'hello world'
result = Solution()
print(result.lengthOfLastWord(s))
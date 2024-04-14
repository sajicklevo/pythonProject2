
from collections import defaultdict
class Solution:
    def Anagrams(self,strs):
        anagrams = defaultdict(list)
        for i in strs:
            sorted_word= ''.join(sorted(i))
            anagrams[sorted_word].append(i)
        return list(anagrams.values())
solution=Solution()
strs = ['eat','tea','tan','ate','nat','bat']
print(solution.Anagrams(strs))
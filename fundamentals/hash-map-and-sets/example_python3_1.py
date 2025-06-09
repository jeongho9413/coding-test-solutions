"""
https://www.youtube.com/watch?v=RcZsTI5h0kg

LeetCode - 49. Group Anagrams
"""
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
            
        return list(anagram_map.values())

"""
input:
  eat tea tan ate nat bat
"""
def main() -> None:
    strs = list(map(str, input().split()))
    # print(strs)
    result = Solution().groupAnagrams(strs)
    print(result)

if __name__ == "__main__":
    main()

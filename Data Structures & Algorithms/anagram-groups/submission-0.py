from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for curr_str in strs:
            str_map["".join(sorted(curr_str))].append(curr_str)
        
        return list(str_map.values())

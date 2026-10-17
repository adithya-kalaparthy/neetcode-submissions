class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for char_s, char_t in zip(s, t):
            s_map[char_s] = s_map.get(char_s, 0) + 1
            t_map[char_t] = t_map.get(char_t, 0) + 1

        return s_map == t_map
        
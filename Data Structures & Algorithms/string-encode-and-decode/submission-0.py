import base64

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for curr_str in strs:
            encoded_str += f"{len(curr_str)}:{curr_str}"
        return encoded_str


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i
            # Loop through next letters to find the ":" character
            while j < len(s):
                if s[j] == ":":
                    # Length is stored as prefix for the string.
                    length = int(s[i:j])
                    break
                j += 1
            # The correct string is stored after the "{len}:" prefix.
            output.append(s[j+1:j+1+length])
            # Update the index to the advance character after this string.
            i = j+1+length
        
        return output
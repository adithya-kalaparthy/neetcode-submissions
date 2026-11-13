class Solution:
    def isValid(self, s: str) -> bool:
        # Define close to open braces map.
        close_open_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        open_braces = []
        available_open_braces = close_open_map.values()
        for i in s:
            if i in available_open_braces:
                # Append the open brace to the open_braces list.
                open_braces.append(i)
            elif i in close_open_map:
                # If there are no already open braces, then
                # Having new closed brace is wrong.
                if not open_braces:
                    return False
                # Check the already open brace.
                already_open_brace = open_braces.pop()
                # If the latest open brace does not correspond to this
                # closed brace..then the order is wrong and it is invalid.
                if already_open_brace != close_open_map[i]:
                    return False
        
        return not open_braces

        
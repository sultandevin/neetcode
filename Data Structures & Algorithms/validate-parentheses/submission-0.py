class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        matching = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        for i in range(n):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    last_opening = stack.pop()
                    if last_opening != matching[s[i]]:
                        return False
                else:
                    return False
        
        return len(stack) == 0


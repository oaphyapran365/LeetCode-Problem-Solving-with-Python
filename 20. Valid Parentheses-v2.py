class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')' : '(',  "}" : "{", "]":"["}
        for i in s:
            if i not in d:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop(-1)
                if x == d[i]:
                    pass
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                
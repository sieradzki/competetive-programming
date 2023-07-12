class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                if p == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif p == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                elif p == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
            else: 
                stack.append(p)

        if len(stack) > 0:
            return False

        return True
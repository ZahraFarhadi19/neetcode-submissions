class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"}":"{", ")":"(", "]":"["}
        # if i see an opening bracket, push it to the stack
        # when i see a closing bracket, i have to check if the top of the stack is its matching opener
        stack = []
        if len(s)%2 != 0:
            return False
        for i in s:
            if i in valid.values():
                stack.append(i)
            else:
                if not stack or stack[-1] != valid[i]:
                    return False
                stack.pop()
        return len(stack) == 0
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # Truncates toward zero per RPN spec
        }
        stack = []

        for token in tokens:
            if token in ops:
                b = stack.pop()  # Right operand (popped first!)
                a = stack.pop()  # Left operand (popped second!)
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]
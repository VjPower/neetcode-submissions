class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x == "*":
                b = stack.pop()
                a = stack.pop()

                result = a*b
                stack.append(result)

            elif x == "-":
                b = stack.pop()
                a = stack.pop()

                result = a-b
                stack.append(result)

            elif x == "+":
                b = stack.pop()
                a = stack.pop()

                result = a+b
                stack.append(result)
            elif x == "/":
                b = stack.pop()
                a = stack.pop()

                result = int(a/b)
                stack.append(result)
            else:
                stack.append(int(x))

        return stack[0]
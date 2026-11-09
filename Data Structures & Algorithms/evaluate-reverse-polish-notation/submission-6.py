class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if token == "+":
                b = nums.pop()
                a = nums.pop()
                c = a + b
                nums.append(c)
            elif token == "-":
                b = nums.pop()
                a = nums.pop()
                c = a - b
                nums.append(c)
            elif token == "*":
                b = nums.pop()
                a = nums.pop()
                c = a * b
                nums.append(c)
            elif token == "/":
                b = nums.pop()
                a = nums.pop()
                c = int(a / b)
                nums.append(c)
            else:
                nums.append(int(token))
        return nums.pop()
        
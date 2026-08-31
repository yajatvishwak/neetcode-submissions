class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        import operator
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        
        for i in tokens:
            if i in '+/*-':
                second_operand = stack.pop()
                first_operand = stack.pop() 
                stack.append(int(ops[i](first_operand, second_operand)))
            else:
                stack.append(int(i))
        print(stack)
        return stack.pop()
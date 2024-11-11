# Check if the the given Paranthesis are valid (properly closing).
# Approach
# Check for opening tags (append them) and in case of closing tags, pop them and return True if valid


# BTC -> O(N)
# WTC -> O(N)
# STC -> O(N)
def validParentheses(string):
    stack = (
        []
    )  # Creating a dummy stack (it will work reverse -> FILO like normal arrays)

    for char in string:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        else:
            if not stack:
                return False
            poppedEl = stack.pop()
            if char == ")" and poppedEl != "(":
                return False
            if char == "}" and poppedEl != "{":
                return False
            if char == "]" and poppedEl != "[":
                return False
        # print(stack)

    return True


# Remove Adjacent Duplicates (remove both elements which are duplicates -> aabbac -> ac)
# Approach
# Append into Stack and if they appear again in the next, remove them.


def removeAdjacentDuplicates(string):
    stack = []

    for char in string:
        # if stack and stack[len(stack) - 1] == char:
        #             OR
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ",".join(stack)  # For String Formatting


# Return number of days until a warmer day comes
#                    1, 1, 3, 2, 1, 0, 0
# Example input -> [73,74,76,71,69,79,73]
def nextWarmDay(days):
    stack = []
    res = [0] * len(days)

    for i in range(len(days) - 1, -1, -1):
        while stack and days[stack[-1]] <= days[i]:
            stack.pop()

        res[i] = stack[-1] - i if stack else 0
        stack.append(i)

    return res


# Evaluate the expression and return its evaluated value
# Example input -> "*+-1234"
# Example output -> "8"
def evaluatePrefix(string):

    def isOperator(op):
        return op == "*" or op == "/" or op == "+" or op == "-"

    def processString(char1, op, char2):
        res = None
        if op == "*":
            res = char1 * char2
        if op == "/":
            res = char1 / char2
        if op == "+":
            res = char1 + char2
        if op == "-":
            res = char1 - char2

        return res

    stack = []

    for char in string[::-1]:
        if isOperator(char):
            char1 = stack.pop()
            char2 = stack.pop()
            res = processString(int(char1), char, int(char2))
            stack.append(res)
        else:
            stack.append(char)

    return stack[-1]


# Convert infix to postfix (Watch for Operator Precedence)
# Example input -> "A+B*C+D/E"
# Example output -> "ABC*+DE/+"
def infixToPostfix(string):
    def isOperator(op):
        return op == "*" or op == "/" or op == "+" or op == "-"

    def hasHigherPrecedence(char, stackTop):
        operatorPriority = {
            "+": 1,
            "-": 1,
            "/": 2,
            "*": 2,
            "^": 3,
        }

        return operatorPriority[char] <= operatorPriority[stackTop]

    res = []
    stack = []

    for char in string:
        if isOperator(char):
            while stack and hasHigherPrecedence(char, stack[-1]):
                res.append(stack.pop())
            stack.append(char)
        else:
            res.append(char)

    while stack:
        res.append(stack.pop())

    return "".join(res)

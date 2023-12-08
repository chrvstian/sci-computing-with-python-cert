"""
@name: .py
@date: 07/11/2023 (dd/mm/yy)
@author: github.com/chrvstian
"""

def arithmetic_arranger(problems: list, show_answers: bool=False):
    # Check if the number of problems is within the limit
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}

    for problem in problems:
        # Split the problem into operands and operator
        operand1, operator, operand2 = problem.split()

        # Check if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if operands have a max of four digits in width
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width of the arranged problem
        width = max(len(operand1), len(operand2)) + 2

        # Create the formatted strings for the problem
        arranged_problems["top"].append(f"{operand1:>{width}}")
        arranged_problems["bottom"].append(f"{operator} {operand2:>{width-2}}")
        arranged_problems["line"].append("-" * width)

        # If show_answers is True, calculate and add the answer
        if show_answers:
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
            arranged_problems["result"].append(f"{result:>{width}}")

    # Combine the formatted strings and add four spaces between each problem
    arranged_output = (
        "    ".join(arranged_problems["top"]) + "\n" +
        "    ".join(arranged_problems["bottom"]) + "\n" +
        "    ".join(arranged_problems["line"])
    )

    # If show_answers is True, add the line with answers
    if show_answers:
        arranged_output += "\n" + "    ".join(arranged_problems["result"])

    return arranged_output


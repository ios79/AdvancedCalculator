import math

def evaluate_expression(expression, last_result):
    """
    Evaluates the given arithmetic expression with support for advanced math functions.
    Allows the use of 'ans' to refer to the last calculated result.
    """
    try:
        # Ensure expression is not empty
        if not expression.strip():
            return "Error: Empty expression. Please enter a valid expression.", last_result
        
        # Replace 'ans' with the last result
        if "ans" in expression:
            expression = expression.replace("ans", str(last_result))

        # Replace '^' with '**' for exponentiation
        expression = expression.replace("^", "**")

        # Allow mathematical functions from the math module
        result = eval(expression, {"__builtins__": None}, {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e
        })
        return result, result  # Return new result as last_result

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed.", last_result
    except (SyntaxError, NameError, TypeError):
        return "Error: Invalid expression. Please enter a valid arithmetic expression.", last_result
    except Exception as e:
        return f"Unexpected error: {e}", last_result

def calculate():
    print("Advanced Calculator with Memory. Type 'quit' or 'exit' to stop.")
    print("Supported functions: sqrt(x), sin(x), cos(x), tan(x), log(x), exp(x)")
    print("Constants: pi, e")
    print("Use ^ for exponentiation (e.g., 2^3 for 2³)")
    print("Use 'ans' to reuse the last result.")

    last_result = 0  # Initialize memory storage

    while True:
        expression = input("Enter an arithmetic expression: ")

        if expression.lower() in ['quit', 'exit']:
            print("Exiting calculator. Goodbye!")
            break
        
        result, last_result = evaluate_expression(expression, last_result)
        print("Result:", result)

if __name__ == "__main__":
    calculate()

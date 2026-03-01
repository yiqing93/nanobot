#!/usr/bin/env python3
"""
Calculate - Mathematical calculation utility
"""

import math
import sys

def calculate(expression):
    """
    Safely evaluate a mathematical expression
    
    Args:
        expression: String containing a mathematical expression
        
    Returns:
        Result of the calculation
    """
    # Create a safe namespace with only math functions
    safe_dict = {
        '__builtins__': {},
        'math': math,
        'pi': math.pi,
        'e': math.e,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'sqrt': math.sqrt,
        'log': math.log,
        'log2': math.log2,
        'log10': math.log10,
        'exp': math.exp,
        'pow': pow,
        'abs': abs,
        'round': round,
        'ceil': math.ceil,
        'floor': math.floor,
        'radians': math.radians,
        'degrees': math.degrees,
    }
    
    try:
        result = eval(expression, safe_dict, {})
        return result
    except Exception as ex:
        return f"Error: {str(ex)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        result = calculate(expr)
        print(f"Result: {result}")
    else:
        print("Usage: python calculate.py <expression>")
        print("Examples:")
        print("  python calculate.py \"2 + 3 * 4\"")
        print("  python calculate.py \"sqrt(16)\"")
        print("  python calculate.py \"sin(pi/2)\"")

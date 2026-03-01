---
name: calculate
description: Perform mathematical calculations including basic arithmetic (+, -, *, /), advanced functions (trigonometry, logarithms, exponents), mathematical constants (π, e), square roots, powers, rounding, and absolute value. Use when the user needs to compute numerical results, solve equations, or perform any mathematical operations.
---

# Calculate

Perform mathematical calculations using Python's math library.

## Quick Usage

### Basic Arithmetic
```python
# Addition, subtraction, multiplication, division
result = 2 + 3        # 5
result = 10 - 4       # 6
result = 6 * 7        # 42
result = 15 / 3       # 5.0
```

### Advanced Functions
```python
import math

# Trigonometry (radians)
math.sin(math.pi / 2)   # 1.0
math.cos(0)             # 1.0
math.tan(math.pi / 4)   # 1.0

# Logarithms
math.log(100, 10)       # 2.0 (log base 10)
math.log(math.e)        # 1.0 (natural log)
math.log2(8)            # 3.0

# Exponents and roots
math.sqrt(16)           # 4.0
math.pow(2, 10)         # 1024.0
2 ** 3                  # 8

# Constants
math.pi                 # 3.14159...
math.e                  # 2.71828...

# Rounding
round(3.14159, 2)       # 3.14
math.ceil(3.2)          # 4
math.floor(3.8)         # 3

# Absolute value
abs(-5)                 # 5
```

## How to Use

1. **For simple calculations**: Use Python's built-in operators
2. **For advanced math**: Import and use the `math` module
3. **For complex expressions**: Write a Python script and execute it

## Example Workflow

When a user asks for a calculation:

1. Parse the mathematical expression
2. Execute using Python
3. Return the result with appropriate formatting

### Example: Calculate distance
```python
import math
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
```

### Example: Compound interest
```python
principal = 1000
rate = 0.05
years = 10
amount = principal * (1 + rate) ** years
```

## Supported Operations

| Category | Operations |
|----------|-----------|
| **Basic** | +, -, *, /, //, %, ** |
| **Trigonometry** | sin, cos, tan, asin, acos, atan, radians, degrees |
| **Logarithms** | log, log2, log10 |
| **Exponents** | sqrt, pow, exp |
| **Constants** | π (pi), e |
| **Rounding** | round, ceil, floor |
| **Absolute** | abs |

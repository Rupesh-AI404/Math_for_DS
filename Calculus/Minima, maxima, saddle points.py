# python
from sympy import symbols, diff, solve

x = symbols('x')

# Find minimum of f(x) = x³ - 6x² + 9x + 1
f  = x**3 - 6*x**2 + 9*x + 1
df = diff(f, x)              # first derivative
d2f = diff(df, x)            # second derivative (curvature test)

critical = solve(df, x)      # where slope = 0
print("Critical points:", critical)  # [1, 3]

for pt in critical:
    curvature = float(d2f.subs(x, pt))   # use the expression's .subs method
    kind = "minimum" if curvature > 0 else "maximum"
    print(f"x={pt}: second derivative={curvature} → {kind}")

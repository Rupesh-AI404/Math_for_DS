from sympy import symbols, diff, solve, subs

x = symbols('x')

# Find minimum of f(x) = x³ - 6x² + 9x + 1
f  = x**3 - 6*x**2 + 9*x + 1
df = diff(f, x)              # first derivative
d2f = diff(df, x)            # second derivative (curvature test)

critical = solve(df, x)      # where slope = 0
print("Critical points:", critical)  # [1, 3]

for pt in critical:
    curvature = d2f.subs(x, pt)
    kind = "minimum" if curvature > 0 else "maximum"
    print(f"x={pt}: second derivative={curvature} → {kind}")
# x=1: second derivative=-6 → maximum
# x=3: second derivative= 6 → minimum  ← gradient descent finds this

# In neural networks: loss landscapes have millions of dimensions,
# thousands of saddle points, and no global minimum — just "good enough" minima

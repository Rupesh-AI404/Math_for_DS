from sympy import symbols, diff

x = symbols('x')

# Rule 1 — power rule: bring exponent down, reduce by 1
f = x**3          # f(x) = x³
print(diff(f, x)) # 3x²  ← exponent came down, power reduced

# Rule 2 — constant disappears
f = 5*x**2 + 3*x + 10
print(diff(f, x)) # 10x + 3  ← the 10 constant vanished

# Rule 3 — what the derivative MEANS
# At x=2, slope of f = 5x² is:
f  = 5*x**2
df = diff(f, x)   # → 10x
slope_at_2 = df.subs(x, 2)
print(slope_at_2)  # 20 ← function rising steeply at x=2

# Numerically verify — tiny step approximation
def approx_derivative(f_fn, x_val, step=1e-5):
    return (f_fn(x_val + step) - f_fn(x_val)) / step

print(approx_derivative(lambda x: 5*x**2, 2))  # ≈ 20.00001
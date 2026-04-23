from sympy import symbols, diff

x = symbols('x')
f = x**4 - 4*x**2    # has two minima

df  = diff(f, x)     # first derivative  → 4x³ - 8x
d2f = diff(df, x)    # second derivative → 12x² - 8

# At x=0 (saddle point):
print("Second deriv at x=0:", d2f.subs(x, 0))   # -8 (negative → concave down → max/saddle)

# At x=√2 ≈ 1.41 (true minimum):
import sympy as sp
print("Second deriv at x=√2:", d2f.subs(x, sp.sqrt(2)))  # 16 (positive → concave up → min)

# Adam optimizer uses exponential moving averages of squared gradients
# which approximates second-order info without computing the full Hessian
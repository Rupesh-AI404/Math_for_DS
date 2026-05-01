from sympy import symbols, diff

x, y = symbols('x y')

# Loss function with two parameters
f = 3*x**2 + 2*x*y + y**3

# Partial w.r.t. x — treat y as a constant number
df_dx = diff(f, x)
print("df/dx =", df_dx)   # 6x + 2y

# Partial w.r.t. y — treat x as a constant number
df_dy = diff(f, y)
print("df/dy =", df_dy)   # 2x + 3y²

# At point (x=1, y=2):
print("Slope in x direction:", df_dx.subs([(x,1),(y,2)]))  # 10
print("Slope in y direction:", df_dy.subs([(x,1),(y,2)]))  # 14
print("Loss at (1,2):", f.subs([(x,1),(y,2)]))
# → x needs a bigger nudge than y to reduce loss at this point
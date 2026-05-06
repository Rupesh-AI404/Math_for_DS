import numpy as np

# A derivative IS a limit:
# f'(x) = lim(h→0) [f(x+h) - f(x)] / h

def f(x): return x**2

# Watch as step h shrinks → answer approaches true derivative (2x at x=3 = 6)
x_val = 3.0
for h in [1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001]:
    slope = (f(x_val + h) - f(x_val)) / h
    print(f"h={h:.5f}: slope ≈ {slope:.6f}")

# h=1.00000: slope ≈ 7.000000
# h=0.10000: slope ≈ 6.100000
# h=0.01000: slope ≈ 6.010000
# h=0.00100: slope ≈ 6.001000
# h=0.00001: slope ≈ 6.000010  ← converging to exactly 6

# This is what sympy.diff() computes symbolically — the limit at h→0

print(np.diff(f, x_val))
print(np.diff(f, x_val, n=2))  # second derivative (should be 2 everywhere)


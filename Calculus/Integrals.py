from sympy import symbols, integrate
from scipy import integrate as sci_integrate
import numpy as np

x = symbols('x')

# Symbolic integral
f = x**2 + 1
area = integrate(f, (x, 0, 2))   # area under curve from 0 to 2
print(f"Exact area: {area}")      # 14/3

# Numerical integral (more common in ML practice)
result, error = sci_integrate.quad(lambda x: x**2 + 1, 0, 2)
print(f"Numerical: {result:.4f}") # 4.6667

# Where you ACTUALLY see integrals in ML:
from scipy.stats import norm

# 1. CDF is an integral of the PDF
prob = norm.cdf(1.96) - norm.cdf(-1.96)
print(f"P(-1.96 < x < 1.96) = {prob:.3f}")   # 0.950

# 2. Expected value E[X] = integral of x * P(x)dx
# scipy handles this under the hood in all distribution methods
mean, var = norm.stats(moments='mv')
print(f"Standard normal: mean={mean}, variance={var}")  # 0, 1
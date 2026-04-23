from sympy import symbols, diff, exp

x = symbols('x')

# Two nested functions — like two layers in a network
# Layer 1: g(x) = x² + 1
# Layer 2: f(g) = e^g   (activation function)
# Combined: f(g(x)) = e^(x²+1)

g   = x**2 + 1
f_g = exp(g)       # e^(x²+1)

# Method 1: derive directly (expand and differentiate)
direct = diff(f_g, x)
print("Direct  :", direct)   # 2*x*exp(x**2 + 1)

# Method 2: chain rule — multiply each layer's derivative
g_sym = symbols('g')
df_dg = diff(exp(g_sym), g_sym)   # d(e^g)/dg = e^g
dg_dx = diff(g, x)                # d(x²+1)/dx = 2x

chain = (df_dg * dg_dx).subs(g_sym, g)
print("Chain   :", chain)    # 2*x*exp(x**2 + 1)  ← same answer

# In a neural network with 100 layers:
# total gradient = product of 100 individual layer derivatives
# This is exactly what backpropagation computes automatically
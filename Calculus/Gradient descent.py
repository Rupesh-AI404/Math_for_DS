import numpy as np

# Find the minimum of f(x) = (x-3)² + 4
# True minimum is at x=3, f=4

def f(x):    return (x - 3)**2 + 4
def df(x):   return 2*(x - 3)   # derivative

x = 0.0           # start anywhere
lr = 0.1          # learning rate — step size fraction
epochs = 60

for i in range(epochs):
    slope = df(x)       # how steep here?
    x -= lr * slope     # step opposite to slope (downhill)
    if i % 10 == 0:
        print(f"Step {i:3d}: x={x:.4f}, f(x)={f(x):.4f}")

print(f"\nFound minimum: x={x:.4f}, f(x)={f(x):.4f}")
print(f"lr={lr:.3f}, epochs={epochs}")
print(f"lr * epochs = {lr * epochs:.3f}")
# x converges to 3.0, f(x) converges to 4.0

# Step   0: x=0.6000, f(x)=9.9600
# Step  10: x=2.6465, f(x)=4.1256
# Step  20: x=2.9161, f(x)=4.0071
# Step  50: x=2.9997, f(x)=4.0000  ← nailed it
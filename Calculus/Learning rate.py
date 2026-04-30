import numpy as np

def f(x):  return (x - 3)**2 + 4
def df(x): return 2*(x - 3)

# Watch what happens with different learning rates
for lr, label in [(0.01, "too small"), (0.1, "just right"), (0.99, "too large")]:
    x = 0.0
    for _ in range(30):
        x -= lr * df(x)
    print(f"lr={lr} ({label:10s}): x={x:.4f}")

# lr=0.01  (too small  ): x=1.4508  ← hasn't converged yet
# lr=0.10  (just right ): x=2.9999  ← converged cleanly
# lr=0.99  (too large  ): x=2.0000  ← oscillating, unstable

# In real ML: start with 0.001 or 0.01 and use a scheduler
from sklearn.linear_model import SGDRegressor
model = SGDRegressor(learning_rate='invscaling', eta0=0.01)
# sklearn handles lr scheduling for you

print("\nIn practice, use a scheduler to adjust learning rate during training:")
for epoch in range(1, 11):
    lr = 0.01 / np.sqrt(epoch)  # example of inverse scaling
    print(f"Epoch {epoch:2d}: learning rate = {lr:.4f}")


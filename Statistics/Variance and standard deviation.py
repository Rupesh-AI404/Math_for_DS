import numpy as np

a = [10, 10, 10, 10, 10]   # no spread
b = [2,  6,  10, 14, 18]   # wide spread

print(f"Std dev A: {np.std(a):.2f}")   # 0.00
print(f"Std dev B: {np.std(b):.2f}")   # 5.66

# In ML: high std dev in a feature = that feature has big range
# → needs scaling before training or it dominates the model

# Sample vs population — the n-1 correction
data = [2, 6, 10, 14, 18]
pop_std  = np.std(data, ddof=0)    # divide by n   → population
samp_std = np.std(data, ddof=1)    # divide by n-1 → sample (always use this)
print(f"Population std: {pop_std:.3f}")   # 5.657
print(f"Sample std    : {samp_std:.3f}")  # 6.325  ← larger = more honest uncertainty
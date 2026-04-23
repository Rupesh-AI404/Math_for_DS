import numpy as np
from sklearn.preprocessing import StandardScaler

# Two features on wildly different scales
age    = np.array([25, 35, 45, 55, 65])   # range: 25-65
salary = np.array([30000, 50000, 70000, 90000, 110000])  # range: 30k-110k

# Without scaling: salary dominates distance calculations completely
# Z-score: (x - mean) / std → puts everything on same scale
def zscore(x):
    return (x - x.mean()) / x.std()

print("Z-scored age   :", np.round(zscore(age), 2))
print("Z-scored salary:", np.round(zscore(salary), 2))
# Both now range from roughly -1.4 to +1.4  ← equal footing

# sklearn does this automatically:
scaler = StandardScaler()
X = np.column_stack([age, salary])
X_scaled = scaler.fit_transform(X)
print("Scaled shape:", X_scaled.shape)  # (5, 2) — both features now balanced
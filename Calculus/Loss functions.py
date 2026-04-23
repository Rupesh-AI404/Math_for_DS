import numpy as np

y_true = np.array([3.0, 5.0, 7.0, 9.0])
y_pred = np.array([2.5, 5.2, 6.8, 9.4])

# MSE — Mean Squared Error (regression)
mse = np.mean((y_true - y_pred)**2)
print(f"MSE: {mse:.4f}")          # 0.0875
# Derivative of MSE w.r.t. prediction:
# dMSE/dy_pred = -2(y_true - y_pred)/n ← this is what gradient descent uses

# MAE — Mean Absolute Error (robust to outliers)
mae = np.mean(np.abs(y_true - y_pred))
print(f"MAE: {mae:.4f}")          # 0.275

# Cross-entropy — classification (logistic regression, neural nets)
y_true_cls = np.array([1, 0, 1, 0])
y_pred_prob = np.array([0.9, 0.1, 0.8, 0.3])

eps = 1e-9   # prevent log(0)
ce = -np.mean(y_true_cls * np.log(y_pred_prob + eps) +
              (1 - y_true_cls) * np.log(1 - y_pred_prob + eps))
print(f"Cross-entropy: {ce:.4f}")  # 0.1643
# sklearn uses this automatically for LogisticRegression
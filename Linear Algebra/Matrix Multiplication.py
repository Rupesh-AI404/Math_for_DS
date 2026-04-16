import numpy as np

# Neural network forward pass — demystified
# Input: 1 sample with 3 features
X = np.array([[0.9, 0.2, 0.6]])      # shape (1, 3)

# Hidden layer: 3 inputs → 4 neurons
W1 = np.random.randn(3, 4)           # shape (3, 4)
b1 = np.zeros((1, 4))

# Output layer: 4 neurons → 1 prediction
W2 = np.random.randn(4, 1)           # shape (4, 1)
b2 = np.zeros((1, 1))

# Forward pass — this is literally what happens inside sklearn/pytorch
hidden = np.maximum(0, X @ W1 + b1)  # ReLU activation
output = hidden @ W2 + b2

print("Shapes:", X.shape, "→", hidden.shape, "→", output.shape)
# (1,3) → (1,4) → (1,1)   ← data flows through as matrix ops
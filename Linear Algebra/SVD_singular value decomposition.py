import numpy as np

X = np.array([[1, 2], [3, 4], [5, 6]])

U, S, Vt = np.linalg.svd(X, full_matrices=False)
# S = singular values → how much variance each component holds
print(S)   # [9.52, 0.51] → first component carries almost all info

# This is literally what sklearn PCA does internally
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit_transform(X)   # uses SVD under the hood
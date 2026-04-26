import numpy as np

# Dot product = multiply element-by-element, then sum
weights = np.array([0.5, 0.3, 0.2])   # learned model weights
features = np.array([100, 200, 150])   # one data point

prediction = np.dot(weights, features) # = 0.5*100 + 0.3*200 + 0.2*150
print(prediction)  # 140.0

# This IS a neuron. One neuron = one dot product + activation.
# A whole layer = matrix multiply (many neurons at once)
W = np.array([[0.5, 0.3, 0.2],
              [0.1, 0.8, 0.4]])   # 2 neurons, 3 inputs each

layer_output = W @ features        # @ is matrix multiply in numpy
print(layer_output)



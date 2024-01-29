import numpy as np

# Number of samples
num_samples = 50

# Initialize the array
data = np.zeros((num_samples, 8))

# For each sample
for i in range(num_samples):
    # Set a random budget between ₹35,000 and ₹3,50,000
    budget = np.random.uniform(35000, 350000)
    data[i, 0] = budget

    # Set the cost of each component to a random fraction of the budget
    for j in range(1, 8):
        # Each component costs between 10% and 20% of the budget
        data[i, j] = np.random.uniform(0.1, 0.2) * budget

# Ensure that the total cost does not exceed the budget
data[:, 1:] = data[:, 0:1] * data[:, 1:] / np.sum(data[:, 1:], axis=1, keepdims=True)

print(data)

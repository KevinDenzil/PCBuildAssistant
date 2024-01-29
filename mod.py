import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from ts_generator import TS_Generator

# Define the neural network model
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc = nn.Linear(1, 8)

    def forward(self, x):
        x = self.fc(x)
        first, rest = torch.split(x, [1, 7], dim=1)
        rest = torch.nn.functional.softmax(rest, dim=1) * first
        x = torch.cat((first, rest), dim=1)
        return x

# Function to train the model
def train_model(model, inputs, targets, epochs=100, lr=1):  # Reduced learning rate
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=lr)
    inputs_torch = torch.tensor(inputs, dtype=torch.float32)
    targets_torch = torch.tensor(targets, dtype=torch.float32)
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(inputs_torch)
        loss = criterion(outputs, targets_torch)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f'Epoch {epoch}/{epochs}, Loss: {loss.item()}')

# User input: Nested array with 10 arrays, each having 9 values
user_input = TS_Generator()
user_input = np.array(user_input)
# Extract the first values as inputs and the rest as targets
inputs = user_input[:, :1]
targets = user_input[:, :8]  # Adjusted target size to match model output
print(inputs.shape,targets.shape)
# Scale inputs and targets
inputs = inputs / np.max(np.abs(inputs))
targets = targets / np.max(np.abs(targets))

# Create and train the model
model = MyModel()
train_model(model, inputs, targets)

# User input for prediction: Nested array with 1 array, having 1 value
user_input_for_prediction = np.array([[69000]])

# Convert to PyTorch tensor and make prediction
input_for_prediction = torch.tensor(user_input_for_prediction, dtype=torch.float32)
predicted_values = model(input_for_prediction)

# Display the predicted values
print("Predicted Values:", predicted_values.detach().numpy())

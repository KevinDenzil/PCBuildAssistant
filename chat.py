import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from PCBuilderWithBudget import *
from PCPartsFinderWithBudget import *
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# PC Parts Dataset unpacking

# with open('PC_Parts_Dataset/video-card.json', 'r') as d:
#     parts_data = json.load(d)

# for part in parts_data:
#     if part["price"] is not None:
#         print(part["name"]," : ", int(part["price"]))

bot_name = "JARVIS" 
print("Let's chat! Type 'quit' to exit")
tagsList = ['CPU', 'GPU', 'PSU', 'Motherboard', 'RAM', 'Memory', 'Case']

while True:
    sentence = input('You:')
    if sentence == "quit":
        break
    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                if tag in tagsList:
                    getPrice(tag)
                elif tag == "PC":
                    PCBuilderWithBudget()
                else:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name} : I do not understand...")
import numpy as np 
import torch
import json

def TS_Generator():
    parts = ["PC_Parts_Dataset/cpu.json", "PC_Parts_Dataset/video-card.json", "PC_Parts_Dataset/memory.json", "PC_Parts_Dataset/internal-hard-drive.json", "PC_Parts_Dataset/motherboard.json","PC_Parts_Dataset/case.json", "PC_Parts_Dataset/power-supply.json"]
    # cpu = open("PC_Parts_Dataset/cpu.json" , "r")
    # gpu = open("PC_Parts_Dataset/video-card.json" , "r")
    # ram = open("PC_Parts_Dataset/memory.json" , "r")
    # rom = open("PC_Parts_Dataset/internal-hard-drive.json" , "r")
    # mob = open("PC_Parts_Dataset/motherboard.json" , "r")
    # case = open("PC_Parts_Dataset/case.json" , "r")
    # psu = open("PC_Parts_Dataset/power-supply.json", "r")

    file_counter = 0

    data = []

    for part in parts:
        f = open(parts[file_counter], "r")
        jsondata = json.load(f)
        data.append(jsondata)
        f.close()
        file_counter+=1

    
    budgets = [60000, 70000, 80000, 90000, 100000, 120000, 150000, 170000, 200000]
    prices = []
    print("CPU\tGPU\tRAM\tROM\tMOBO\tCASE\tPSU")
    for budget in budgets:
        entry = [budget*0.25, budget*0.30, budget*0.1, budget*0.075, budget*0.15, budget*0.05, budget*0.075]
        prices.append(entry)
        print(entry)

TS_Generator()
import json
import random
from PCBuilderWithBudget import *

def getStartingPrice(tag, random):
    tag = tag[0]
    if random.lower() != "yes":
        response = {
        "response": "Exiting Parts Recommender...",
        "func": "get_response",
        "arg": -1}
    else:
        response = {
            "response": "What is the starting price range(only a number is accepted) ?",
            "func": "getEndingPrice",
            "arg": [tag]
        }
    return json.dumps(response)

def getEndingPrice(arg, startingPrice):
    tag= arg[0]
    if(tag == "PC"):
        response = {
            "response": "What is the ending price range(only a number is accepted) ?",
            "func": "calculatePCPrice",
            "arg": [tag, startingPrice]
    }
    else:
        response = {
        "response": "What is the ending price range(only a number is accepted) ?",
        "func": "calculatePrice",
        "arg": [tag, startingPrice]
        }
    return json.dumps(response)

def calculatePrice(arg, endingPrice):
    print(arg, "arg")
    tag = arg[0]
    startingPrice = arg[1]
    mappingOfTagsToFiles = {"CPU": "PC_Parts_Dataset/cpu.json", "GPU": "PC_Parts_Dataset/video-card.json", "PSU":"PC_Parts_Dataset/power-supply.json","Motherboard": "PC_Parts_Dataset/motherboard.json", "RAM": "PC_Parts_Dataset/memory.json", "Memory":"PC_Parts_Dataset/internal-hard-drive.json","Case":"PC_Parts_Dataset/case.json"}
    f = open(mappingOfTagsToFiles[tag], "r")
    jsondata = json.load(f)
    newList = [x for x in jsondata if x['price'] != None and int(startingPrice) <= (int(x['price']) * 80) <= int(endingPrice)]
    if(len(newList) == 0):
        return json.dumps({
            "response": "Please give a reasonable budget",
            "func": "getStartingPrice",
            "arg": [tag]
        })
    data = random.choices(newList, k = 5)
    op = ""
    for datum in data:
        op += datum["name"] + "\t-\t" + u'\u20B9'+ str(int((datum["price"]*80))) + "\n"
    return json.dumps({
        "response": op,
        "func": "get_response",
        "arg": -1
    })
    

def getPrice(tag, startingPrice = 0, endingPrice = 0):
    # mappingOfTagsToFiles = {"CPU": "PC_Parts_Dataset/cpu.json", "GPU": "PC_Parts_Dataset/video-card.json", "PSU":"PC_Parts_Dataset/power-supply.json","Motherboard": "PC_Parts_Dataset/motherboard.json", "RAM": "PC_Parts_Dataset/memory.json", "Memory":"PC_Parts_Dataset/internal-hard-drive.json","Case":"PC_Parts_Dataset/case.json"}
    # f = open(mappingOfTagsToFiles[tag], "r")
    # jsondata = json.load(f)
    # isBudgetGiven = 0
    # while(isBudgetGiven != 1):
    #     if(startingPrice == 0 and endingPrice == 0):
    #         print("What is the starting price range(only a number is accepted) ?")
    #         startingPrice = int(input())
    #         print("What is the ending price range(only a number is accepted) ?")
    #         endingPrice = int(input())
    #     newList = [x for x in jsondata if x['price'] != None and startingPrice <= (int(x['price']) * 80) <= endingPrice]
    #     if(len(newList) == 0):
    #         print("Please give a reasonable budget")
    #         startingPrice = 0
    #         endingPrice = 0
    #         # print("Please give a reasonable budget or enter skip to not get options for " + tag)
    #         # canContinue = input()
    #         # if(canContinue == 'skip'):
    #         #     print("skipping for " + tag)
    #         #     return -1
    #     else:
    #         isBudgetGiven = 1
    # data = random.choices(newList, k = 5)
    # op = ""
    # for datum in data:
    #     op += datum["name"] + "\t-\t" + u'\u20B9'+ str(int((datum["price"]*80))) + "\n"
                
    return json.dumps({
        "response": "Finding options within your budget range, type YES to continue",
        "func" : "getStartingPrice",
        "arg": [tag]
    })
    
    return op
import json

def getPrice(tag, startingPrice = 0, endingPrice = 0):
    mappingOfTagsToFiles = {"CPU": "PC_Parts_Dataset/cpu.json", "GPU": "PC_Parts_Dataset/video-card.json", "PSU":"PC_Parts_Dataset/power-supply.json","Motherboard": "PC_Parts_Dataset/motherboard.json", "RAM": "PC_Parts_Dataset/memory.json", "Memory":"PC_Parts_Dataset/internal-hard-drive.json","Case":"PC_Parts_Dataset/case.json"}
    f = open(mappingOfTagsToFiles[tag], "r")
    jsondata = json.load(f)
    isBudgetGiven = 0
    while(isBudgetGiven != 1):
        if(startingPrice == 0 and endingPrice == 0):
            print("What is the starting price range(only a number is accepted) ?")
            startingPrice = int(input())
            print("What is the ending price range(only a number is accepted) ?")
            endingPrice = int(input())
        newList = [x for x in jsondata if x['price'] != None and startingPrice <= (int(x['price']) * 80) <= endingPrice]
        if(len(newList) == 0):
            print("Please give a reasonable budget")
            startingPrice = 0
            endingPrice = 0
            # print("Please give a reasonable budget or enter skip to not get options for " + tag)
            # canContinue = input()
            # if(canContinue == 'skip'):
            #     print("skipping for " + tag)
            #     return -1
        else:
            isBudgetGiven = 1
    print(newList)
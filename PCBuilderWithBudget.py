from PCPartsFinderWithBudget import *

tagsList = ['CPU', 'GPU', 'PSU', 'Motherboard', 'RAM', 'Memory', 'Case']

def calculatePCPrice(arg, endingPrice):
    startingPrice = int(arg[1])
    endingPrice = int(endingPrice)
    percentageOfEachPart = {
        "CPU" : 0.25,
        "GPU": 0.30,
        "RAM": 0.1,
        "Memory": 0.075,
        "Motherboard": 0.15,
        "Case": 0.05,
        "PSU": 0.075
    }
    op = ""
    for tag in tagsList:
        op += "Finding " + tag + " for price range: " + str(startingPrice * percentageOfEachPart[tag]) + " to " + str(endingPrice * percentageOfEachPart[tag]) + "\n"
        response = calculatePrice([tag, startingPrice * percentageOfEachPart[tag]] , endingPrice * percentageOfEachPart[tag])
        res = json.loads(response)
        op += res["response"] + "\n"
            
    return json.dumps({
        "response": op,
        "func" : "get_response",
        "arg": -1
    })

def PCBuilderWithBudget(tag):
    return json.dumps({
        "response": "Finding options within your budget range, type YES to continue",
        "func" : "getStartingPrice",
        "arg": [tag]
    })
    
   
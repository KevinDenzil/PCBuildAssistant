from PCPartsFinderWithBudget import *

tagsList = ['CPU', 'GPU', 'PSU', 'Motherboard', 'RAM', 'Memory', 'Case']

def PCBuilderWithBudget():
    print("What is the starting price range(only a number is accepted) ?")
    startingPrice = int(input())
    print("What is the ending price range(only a number is accepted) ?")
    endingPrice = int(input())
    percentageOfEachPart = {
        "CPU" : 0.25,
        "GPU": 0.30,
        "RAM": 0.1,
        "Memory": 0.075,
        "Motherboard": 0.15,
        "Case": 0.05,
        "PSU": 0.075
    }
    for tag in tagsList:
        print("Finding " + tag + " for price range:", startingPrice * percentageOfEachPart[tag], "to", endingPrice * percentageOfEachPart[tag])
        getPrice("CPU", startingPrice * percentageOfEachPart[tag] , endingPrice * percentageOfEachPart[tag])
        print("")
  
import re

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

class Workflow:
    def __init__(self, line) -> None:
        lineRgx = re.findall("([A-z]+)\{(.+)}", line)[0]
        self.name = lineRgx[0]
        rules = lineRgx[1].split(",")

        self.rules = []

        for rule in rules:
            rgxFind = re.findall("([a-z])([><=])([0-9]+)\:([A-z]+)|([A-z]+)", rule)[0]

            print(rgxFind)

            if rgxFind[0] != "":
                self.rules.append((rgxFind[0], rgxFind[1], int(rgxFind[2]), rgxFind[3]))   
            else:
                self.rules.append((rgxFind[4],))

    def __str__(self) -> str:
        return self.name + str(self.rules)

workflows = {}

ratings = []
ruleMode = True
for line in input:
    if line == "":
        ruleMode = False
    elif ruleMode:
        workflow = Workflow(line)
        workflows[workflow.name] = workflow
    else:
        rating = line[1:-1].split(",")
        print(rating)
        ratingList = {}
        for ratingComp in rating:
            ratingComp = ratingComp.split("=")
            ratingList[ratingComp[0]] = int(ratingComp[1])
        
        ratings.append(ratingList)

total = 0
for rating in ratings:
    curLoc = "in"
    while curLoc != "R" and curLoc != "A":
        print(curLoc, rating)
        curWorkflow = workflows[curLoc]

        for rule in curWorkflow.rules:
            print(rule)
            if len(rule) == 4:
                cmpValue = rating[rule[0]]
                if rule[1] == "<":
                    if cmpValue < rule[2]:
                        curLoc = rule[3]
                        break
                elif rule[1] == ">":
                    if cmpValue > rule[2]:
                        curLoc = rule[3]
                        break
            elif len(rule) == 1:
                curLoc = rule[0]

        if curLoc == "A":
            total += sum(rating.values())

print(total)
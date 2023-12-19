import re
import math

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

class Workflow:
    def __init__(self, line) -> None:
        lineRgx = re.findall("(.+)\{(.+)}", line)[0]
        self.name = lineRgx[0]
        rules = lineRgx[1].split(",")

        self.rules = []
        self.hasAcceptCond = False
        self.froms = []

        for rule in rules:
            rgxFind = re.findall("(.+)([><=])([0-9]+)\:(.+)|(.+)", rule)[0]

            # print(rgxFind)

            if rgxFind[0] != "":
                self.rules.append((rgxFind[0], rgxFind[1], int(rgxFind[2]), rgxFind[3]))
                if rgxFind[3] == "A":
                    self.hasAcceptCond = True
            else:
                if self.rules[-1][-1] == rgxFind[4]:
                    self.rules.pop()
                self.rules.append((rgxFind[4],))
                if rgxFind[4] == "A":
                    self.hasAcceptCond = True

    def __repr__(self) -> str:
        return self.name + str(self.rules) + str(self.hasAcceptCond)
    
    def hasRuleWithName(self, name) -> bool:
        for rule in self.rules:
            if rule[-1] == name:
                return True
            
        return False

workflows = {}

for line in input:
    if line == "":
        break
    else:
        workflow = Workflow(line)
        workflows[workflow.name] = workflow

# print(workflows)

workflowsWithAccepts = [x for x in filter(lambda x: (x.hasAcceptCond), workflows.values())]

# print(len(workflowsWithAccepts))
# print()

for workflow in workflows.values():
    for rule in workflow.rules:
        if rule[-1] != "A" and rule[-1] != "R":
            workflows[rule[-1]].froms.append(workflow)

totalPermu = 0

for workflow in workflowsWithAccepts:
    withAs = [x for x in filter(lambda x: (x[-1] == "A"), workflow.rules)]

    for withA in withAs:
        ranges = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}
        curLoc = workflow
        next = None
        
        while next is None or (next is not None and next.name != "in"):
            if curLoc == workflow:
                indx = workflow.rules.index(withA)
            else:
                # print("bofa", [i for i in curLoc.rules if i[-1] == next.name])
                indx = curLoc.rules.index([i for i in curLoc.rules if i[-1] == next.name][0])
                # print([i for i in curLoc.rules if i[-1] == next.name])

            while indx >= 0:
                if len(curLoc.rules[indx]) != 1:
                    if (next is None and curLoc.rules[indx] == withA) or (next is not None and curLoc.rules[indx] == [i for i in curLoc.rules if i[-1] == next.name][0]):
                        if curLoc.rules[indx][1] == "<":
                            ranges[curLoc.rules[indx][0]][1] = min(curLoc.rules[indx][2]-1, ranges[curLoc.rules[indx][0]][1])
                        elif curLoc.rules[indx][1] == ">":
                            ranges[curLoc.rules[indx][0]][0] = max(curLoc.rules[indx][2]+1, ranges[curLoc.rules[indx][0]][0])
                    else:
                        if curLoc.rules[indx][1] == "<":
                            ranges[curLoc.rules[indx][0]][0] = max(curLoc.rules[indx][2], ranges[curLoc.rules[indx][0]][0])
                        elif curLoc.rules[indx][1] == ">":
                            ranges[curLoc.rules[indx][0]][1] = min(curLoc.rules[indx][2], ranges[curLoc.rules[indx][0]][1])
                
                    indx -= 1
                else:
                    indx -= 1

            next = curLoc
            if curLoc.name != "in":
                curLoc = curLoc.froms[0]

        # print(ranges)

        # print()

        thisres = math.prod([x[1] - x[0] + 1 for x in ranges.values()])
        if thisres < 0: 
            print(ranges)

        totalPermu += thisres

print(totalPermu)
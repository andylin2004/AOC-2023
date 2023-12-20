from math import lcm

LOW = 0
HIGH = 1

f = open("input.txt", 'r')
# f = open("test_input.txt", 'r')
input = f.read().splitlines()

class Module:
    def __init__(self, line=None) -> None:
        if line is not None:
            splitLine = line.split(" -> ")
            # print(splitLine[0][:-1], splitLine [1][2:])
            
            if splitLine[0][0] in "&%":
                self.type = splitLine[0][0]
                self.name = splitLine[0][1:]

                if self.type == "&":
                    self.states = {}
                else:
                    self.states = False
            else:
                self.type = "in"
                self.name = splitLine[0]
                self.states = None

            self.nexts = splitLine[1].split(", ")

            # print(self.nexts)

    def __repr__(self) -> str:
        return self.name + " " + self.type + " " + str(self.nexts) + " " + str(self.states)
    
    def __copy__(self):
        new = Module()
        new.name = self.name
        new.type = self.type
        new.nexts = self.nexts.copy()
        if self.type == "in":
            new.states = None
        elif self.type == "&":
            new.states = self.states.copy()
        else:
            new.states = self.states

        return new

broadcaster = None
modules = {}

for line in input:
    thisModule = Module(line)

    if thisModule.name == "broadcaster":
        broadcaster = thisModule

    modules[thisModule.name] = thisModule

for module in modules.values():
    for nextModuleName in module.nexts:
        if nextModuleName not in modules:
            continue
        nextModule = modules[nextModuleName]
        if nextModule.type == "&":
            nextModule.states[module.name] = LOW

rx_pipe = [x for x in modules.values() if "rx" in x.nexts][0]

rx_pipe_feeds = rx_pipe.states.keys()
rx_pipe_name = rx_pipe.name

print(rx_pipe_name)

occurences = {}

for feed in rx_pipe_feeds:
    occurences[feed] = []

totalInterval = 0
rxFound = False
for i in range(20000):
    curDelivery = {(broadcaster, ("", LOW))}

    while len(curDelivery) > 0:
        nextDelivery = set()

        for delivery in curDelivery:
            if delivery[0].type == "in":
                for nextModule in delivery[0].nexts:
                    if nextModule not in modules:
                        if delivery[1][1] == LOW:
                            rxFound = True
                        continue
                    elif nextModule == rx_pipe_name and delivery[1][1] == HIGH:
                        occurences[nextModule].append(i)
                    nextDelivery.add((modules[nextModule], (delivery[0].name, delivery[1][1])))
                    
            elif delivery[0].type == "%":
                if delivery[1][1] == LOW:
                    delivery[0].states = not delivery[0].states
                    for nextModule in delivery[0].nexts:
                        if delivery[0].states:
                            if nextModule not in modules:
                                continue
                            elif nextModule == rx_pipe_name:
                                occurences[delivery[0].name].append(i)
                            nextDelivery.add((modules[nextModule], (delivery[0].name, HIGH)))                    
                        else:
                            if nextModule not in modules:
                                rxFound = True
                                continue
                            nextDelivery.add((modules[nextModule], (delivery[0].name, LOW)))
            else:
                delivery[0].states[delivery[1][0]] = delivery[1][1]

                # print(delivery[0].states.values())

                if LOW in delivery[0].states.values():
                    for nextModule in delivery[0].nexts:
                        if nextModule not in modules:
                            continue
                        elif nextModule == rx_pipe_name:
                            occurences[delivery[0].name].append(i)
                        nextDelivery.add((modules[nextModule], (delivery[0].name, HIGH)))
                        
                else:
                    for nextModule in delivery[0].nexts:
                        if nextModule not in modules:
                            rxFound = True
                            continue
                        nextDelivery.add((modules[nextModule], (delivery[0].name, LOW)))

        curDelivery = nextDelivery

    totalInterval += 1
    # if min([len(x) for x in occurences.values()]) > 0:
    #     break

print(occurences)

lcms = 1
for value in occurences.values():
    lcms = lcm(lcms, value[0]+1)

print(lcms)
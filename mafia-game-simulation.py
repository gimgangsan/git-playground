# git test code
playerList = []
graveYard = []

class civilian:
    def __init__(self, name):
        self.name = name
        self.executionVote = "nobody"
        self.job = "civilian"
        self.isHealed = False
        try:
            playerList.append(self)
        except NameError:
            print("player list does not exist")

    def vote(self, who):
        self.executionVote = who

    def whenAssassinated(self):
        if self.isHealed == False:
            print(self.name + " has been assassinated by mafia")
            self.die()
        else:
            print("medic saved " +  self.name)

    def whenExecuted(self):
        print(self.name + " has been executed")
        self.die()

    def die(self):
        graveYard.append(self)
        playerList.remove(self)

class mafia(civilian):
    def __init__(self, name):
        super().__init__(name)

    def assassinate(self, who):
        who.whenAssassinated()

class medic(civilian):
    def __init__(self, name):
        super().__init__(name)

    def medicare(self, who):
        who.isHealed = True

randomGuy1 = civilian("bob")
randomGuy1.whenAssassinated()

class Boat:
    def __init__(self,name,team,length,x,y):
        self.name = name
        self.team = team
        self.length = length
        self.hp = length
        self.maxhp = length
        self.firepower = 1
        self.maxfirepower = 1
        self.offensive = True

        #Range lengte defineren
        if offensive == True:
            #Horizontal + Vertical range!
            range = length
            maxrange = length
        else:
            #Vertical only
            range = length + 1
            maxrange = length +1



        #Movement defineren
        if offensive == True:
            if length == 3:
                self.movement = 3
            if length == 4:
                self.movement = 2
            if length == 5:
                self.movement = 1
        else:
            self.movement = 0

    def PosSwitch(self, offensive):
        if offensive == True:
                offensive = False
        else:
                offensive = True

    def RIPship:
        if self.name = ... and hp = 0

        elif self.name = ... and hp = 0

        elif self.name = ... and hp = 0

        elif self.name = ... and hp = 0

        elif self.name = ... and hp = 0

        elif self.name = ... and hp = 0

        elif self.name = ... and hp = 0

        elif self.name = ... and hp = 0



class Cards
    #OffensieveKaarten
    def FMJ_Upgrade(self):
        ship.firepower += 1
    def Rifling(self):
        ship.range += 1
    def Advanced_Rifling(self):
        ship.range += 1
    def Neval_Mine(self):

    def EMP_Upgrade(self):


    #DefensieveKaarten
    def Reinforced_Hull(self):
        ship.hp += 1
    def Smokescreen(self):

    def Sabotage(self):
        ship.hp -=1

    #HulpKaarten
    def Backup(self):

    def Extra_Fuel(self):
        ship.movement += 1
    def Extra_Fuel2(self):
        ship.movement += 2
    def Rally(self):
        ship.movement += 1
    def Adrenaline_Rush(self):

    def Repair(self):
        ship.hp = ship.maxhp
    def Flak_Armor(self):

    def Hack_Intel(self):

    def Far_Sight(self):
        ship.range += 2

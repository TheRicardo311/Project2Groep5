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
            self.range = length
            self.maxrange = length
        else:
            #Vertical only
            self.range = length + 1
            self.maxrange = length + 1


        #Movement defineren
        if offensive == True:
            if length == 3:
                self.movement = 3
                self.maxmovement = 3
            if length == 4:
                self.movement = 2
                self.maxmovement = 2
            if length == 5:
                self.movement = 1
                self.maxmovement = 1
        else:
            self.movement = 0
            self.maxmovement = 0

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
            return ship.firepower
        FMJ_Upgrade = FMJ_Upgrade()

        def Rifling(self):
            ship.range += 1
            return ship.range
        Rifling = Rifling()

        def Advanced_Rifling(self):
            ship.range += 1
            return ship.range
        Advanced_Rifling = Advanced_Rifling()

        def Neval_Mine(self):

            return
        Neval_Mine = Neval_Mine()
        def EMP_Upgrade(self):

            return
        EMP_Upgrade = EMP_Upgrade()

        #DefensieveKaarten
        def Reinforced_Hull(self):
            ship.hp += 1
            return ship.hp
        Reinforced_Hull = Reinforced_Hull()

        def Sonar(self):

            return
        Sonar = Sonar()

        def Smokescreen(self):

            return
        Smokescreen = Smokescreen()

        def Sabotage(self):
            ship.hp -=1
            return ship.hp()
        Sabotage = Sabotage()

        #HulpKaarten
        def Backup(self):

            return
        Backup = Backup()

        def Extra_Fuel(self):
            ship.movement += 1
            return ship.movement
        Extra_Fuel = Extra_Fuel()

        def Extra_Fuel2(self):
            ship.movement += 2
            return ship.movement
        Extra_Fuel2 = Extra_Fuel2()

        def Rally(self):
            ship.movement += 1
            return ship.movement
        Rally = Rally()

        def Adrenaline_Rush(self):

            return
        Adrenaline_Rush = Adrenaline_Rush()

        #SpeciaalKaarten
        def Repair(self):
            ship.hp = ship.maxhp
            return ship.hp
        Repair = Repair()

        def Flak_Armor(self):

            return
        Flak_Armor = Flak_Armor()

        def Hack_Intel(self):

            return
        Hack_Intel = Hack_Intel()

        def Far_Sight(self):
            ship.range += 2
            return ship.range
        Far_Sight = Far_Sight()

        def Aluminium_Hull(self):
            ship.movement *= 2
            return ship.movement
        Aluminium_Hull = Aluminium_Hull()

        def Jack_Sparrow(self):

            return
        Jack_Sparrow = Jack_Sparrow()


        def reset(self):
            self.firepower = self.maxfirepower
            self.movement = self.maxmovement
            self.range = self.maxrange


taart = [1,2,3,4,5,6,7,8,9,10]

a = randomint(taart)
print(a)
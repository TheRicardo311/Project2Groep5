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




        def reset(self):
            self.firepower = self.maxfirepower
            self.movement = self.maxmovement
            self.range = self.maxrange




class Player:

    def __init__(self, name, kleur):
        self.name = name
        self.score = 0
        self.kleur = kleur

        self.Furgo = Boat(2, 3, 2, 1)
        self.Intensity = Boat(3, 2, 3, 1)
        self.Silver = Boat(3, 2, 3, 1,)
        self.Merapi = Boat(4, 1, 4, 1,)

        self.Cards = []

        # OffensieveKaarten
        def FMJ_Upgrade(self):
            ship.firepower += 1
            return ship.firepower

        self.FMJ_Upgrade = FMJ_Upgrade()

        def Rifling(self):
            ship.range += 1
            return ship.range

        self.Rifling = Rifling()

        def Advanced_Rifling(self):
            ship.range += 1
            return ship.range

        self.Advanced_Rifling = Advanced_Rifling()

        def Neval_Mine(self):
            return

        self.Neval_Mine = Neval_Mine()

        def EMP_Upgrade(self):
            return

        self.EMP_Upgrade = EMP_Upgrade()

        # DefensieveKaarten
        def Reinforced_Hull(self):
            ship.hp += 1
            return ship.hp

        self.Reinforced_Hull = Reinforced_Hull()

        def Sonar(self):
            return

        self.Sonar = Sonar()

        def Smokescreen(self):
            return

        self.Smokescreen = Smokescreen()

        def Sabotage(self):
            ship.hp -= 1
            return ship.hp()

        self.Sabotage = Sabotage()

        # HulpKaarten
        def Backup(self):
            return

        self.Backup = Backup()

        def Extra_Fuel(self):
            ship.movement += 1
            return ship.movement

        self.Extra_Fuel = Extra_Fuel()

        def Extra_Fuel2(self):
            ship.movement += 2
            return ship.movement

        self.Extra_Fuel2 = Extra_Fuel2()

        def Rally(self):
            ship.movement += 1
            return ship.movement

        self.Rally = Rally()

        def Adrenaline_Rush(self):
            return

        self.Adrenaline_Rush = Adrenaline_Rush()

        # SpeciaalKaarten
        def Repair(self):
            ship.hp = ship.maxhp
            return ship.hp

        self.Repair = Repair()

        def Flak_Armor(self):
            return

        self.Flak_Armor = Flak_Armor()

        def Hack_Intel(self):
            return

        self.Hack_Intel = Hack_Intel()

        def Far_Sight(self):
            ship.range += 2
            return ship.range

        self.Far_Sight = Far_Sight()

        def Aluminium_Hull(self):
            ship.movement *= 2
            return ship.movement

        self.Aluminium_Hull = Aluminium_Hull()

        def Jack_Sparrow(self):
            return

        self.Jack_Sparrow = Jack_Sparrow()

    Card_Deck = [self.FMJ_Upgrade, self.FMJ_Upgrade, self.Rifling, self.Rifling, self.Advanced_Rifling, self.Advanced_Rifling, self.Neval_Mine, self.Neval_Mine, self.Neval_Mine, self.Neval_Mine, self.Neval_Mine, self.eval_Mine, self.EMP_Upgrade, self.EMP_Upgrade, self.EMP_Upgrade, self.EMP_Upgrade, self.Reinforced_Hull, self.Reinforced_Hull, self.Sonar, self.Sonar, self.Sonar, self.Sonar, self.Smokescreen, self.Smokescreen, self.Sabotage, self.Sabotage, self.Backup, self.Backup, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel2, self.Extra_Fuel2, self.Extra_Fuel2, self.Extra_Fuel2, self.Rally, self.Adrenaline_Rush, self.Adrenaline_Rush, self.Adrenaline_Rush, self.Adrenaline_Rush]
    def Draw_Card(self, Card_Deck):
        if len(Card_Deck) == 0:
            Card_Deck = [self.FMJ_Upgrade, self.FMJ_Upgrade, self.Rifling, self.Rifling, self.Advanced_Rifling, self.Advanced_Rifling, self.Neval_Mine, self.Neval_Mine, self.Neval_Mine, self.Neval_Mine, self.Neval_Mine, self.eval_Mine, self.EMP_Upgrade, self.EMP_Upgrade, self.EMP_Upgrade, self.EMP_Upgrade, self.Reinforced_Hull, self.Reinforced_Hull, self.Sonar, self.Sonar, self.Sonar, self.Sonar, self.Smokescreen, self.Smokescreen, self.Sabotage, self.Sabotage, self.Backup, self.Backup, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel, self.Extra_Fuel2, self.Extra_Fuel2, self.Extra_Fuel2, self.Extra_Fuel2, self.Rally, self.Adrenaline_Rush, self.Adrenaline_Rush, self.Adrenaline_Rush, self.Adrenaline_Rush]
            Random_Card = random.choice(Card_Deck)
            print(Random_Card)
            Card_Deck.remove(Random_Card)

            self.Cards.add(Random_Card)
            print(self.Cards)
            return Card_Deck
    Card_Deck = Draw_Card(Card_Deck)
import random
import pygame

class Player:

    def __init__(self, name, kleur):
        self.name = name
        self.score = 0
        self.kleur = kleur

        self.Furgo = Boat(2, 3, 2, 1)
        self.Intensity = Boat(3, 2, 3, 1)
        self.silver = Boat(3, 2, 3, 1,)
        self.Merapi = Boat(4, 1, 4, 1,)

        self.Cards = []

    Card_Deck = [FMJ_Upgrade, FMJ_Upgrade, Rifling, Rifling, Advanced_Rifling, Advanced_Rifling, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, EMP_Upgrade, EMP_Upgrade, EMP_Upgrade, EMP_Upgrade, Reinforced_Hull, Reinforced_Hull, Sonar, Sonar, Sonar, Sonar, Smokescreen, Smokescreen, Sabotage, Sabotage, Backup, Backup, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel2, Extra_Fuel2, Extra_Fuel2, Extra_Fuel2, Rally, Adrenaline_Rush, Adrenaline_Rush, Adrenaline_Rush, Adrenaline_Rush]

    def Draw_Card(self, Card_Deck):
        if len(Card_Deck) == 0:
            Card_Deck = [FMJ_Upgrade, FMJ_Upgrade, Rifling, Rifling, Advanced_Rifling, Advanced_Rifling, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, EMP_Upgrade, EMP_Upgrade, EMP_Upgrade, EMP_Upgrade, Reinforced_Hull, Reinforced_Hull, Sonar, Sonar, Sonar, Sonar, Smokescreen, Smokescreen, Sabotage, Sabotage, Backup, Backup, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel2, Extra_Fuel2, Extra_Fuel2, Extra_Fuel2, Rally, Adrenaline_Rush, Adrenaline_Rush, Adrenaline_Rush, Adrenaline_Rush]
            Random_Card = random.choice(Card_Deck)
            print(Random_Card)
            Card_Deck.remove(Random_Card)

            self.Cards.add(Random_Card)
            print(self.Cards)
            return Card_Deck
    Card_Deck = Draw_Card(Card_Deck)

import random
import pygame

Card_Deck = [FMJ_Upgrade, FMJ_Upgrade, Rifling, Rifling, Advanced_Rifling, Advanced_Rifling, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, EMP_Upgrade, EMP_Upgrade, EMP_Upgrade, EMP_Upgrade, Reinforced_Hull, Reinforced_Hull, Sonar, Sonar, Sonar, Sonar, Smokescreen, Smokescreen, Sabotage, Sabotage, Backup, Backup, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel2, Extra_Fuel2, Extra_Fuel2, Extra_Fuel2, Rally, Adrenaline_Rush, Adrenaline_Rush, Adrenaline_Rush, Adrenaline_Rush]

def Draw_Card(Card_Deck):
    if len(Card_Deck) == 0:
        Card_Deck = [FMJ_Upgrade, FMJ_Upgrade, Rifling, Rifling, Advanced_Rifling, Advanced_Rifling, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, Neval_Mine, EMP_Upgrade, EMP_Upgrade, EMP_Upgrade, EMP_Upgrade, Reinforced_Hull, Reinforced_Hull, Sonar, Sonar, Sonar, Sonar, Smokescreen, Smokescreen, Sabotage, Sabotage, Backup, Backup, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel, Extra_Fuel2, Extra_Fuel2, Extra_Fuel2, Extra_Fuel2, Rally, Adrenaline_Rush, Adrenaline_Rush, Adrenaline_Rush, Adrenaline_Rush]
    Random_Card = random.choice(Card_Deck)
    print(Random_Card)
    Card_Deck.remove(Random_Card)
    return taart

Card_Deck = remove(Card_Deck)

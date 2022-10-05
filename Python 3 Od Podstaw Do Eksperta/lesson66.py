import random
from enum import Enum

def findApproximateValue(value, percentRange = 10):
    lowestValue = value - percentRange/100 * value
    highestValue = value + percentRange/100 * value
    return random.randint(lowestValue, highestValue)

Event_enum = Enum('Event', ('Chest', 'Empty'))

Event_dict = {
    Event_enum.Chest : 0.6,
    Event_enum.Empty : 0.4
    }

Event_list = list(Event_dict.keys())
Event_propability = list(Event_dict.values())

Colours_enum = Enum('Colours', {'Green': 'zielony',
                                'Orange': 'pomarańczowy',
                                'Purple': 'fiolet',
                                'Gold': 'złoty'
})

chestColoursDictionary = {
    Colours_enum.Green: 0.75,
    Colours_enum.Orange: 0.2,
    Colours_enum.Purple: 0.04,
    Colours_enum.Gold: 0.01,
}
chestColourList = list(chestColoursDictionary.keys())
chestColourPropability = list(chestColoursDictionary.values())

rewardsForChest = {  
    chestColourList[reward]: (reward +1) * (reward +1) * 1000
    for reward in range(len(chestColourList))
}

game_length = 0
goldAcquired = 0

while game_length < 5:
       
    gamer_answer = input('\nDo you want to go forward: y/n\n')
    if gamer_answer == 'y':
        print('Great! Lets see what you got.')
        drawn_event = random.choices(Event_list, Event_propability)[0]
        # print(drawn_event)
        if drawn_event == Event_enum.Chest:
            print('You have drawn a CHEST')
            drawn_chest = random.choices(chestColourList, chestColourPropability)[0]
            print('The chest colour is ', drawn_chest.value)
            gamerRewards = findApproximateValue(rewardsForChest[drawn_chest])
            goldAcquired = goldAcquired + gamerRewards
            print(f'In chest was {gamerRewards} gold')
        elif drawn_event == Event_enum.Empty:
            print('You have drawn nothing! Sorry.\n')
    else:
        print('You can go just forward, nothing else.')
        continue

    game_length = game_length + 1

print(f'\nCongratukations, you have acquired {goldAcquired} gold')
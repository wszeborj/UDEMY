import random

def will_weapon_hit(percentageWeaponChance):
    isHitChance=random.uniform(0,100)
    if isHitChance < percentageWeaponChance:
        return "hit"
    else:
        return "not hit"


x = 0
listHit = []

while x < 100:
    x= x + 1
    listHit.append(will_weapon_hit(50))

print('hit = ', listHit.count('hit'))
print('not hit = ', listHit.count('not hit'))

from collections import Counter
dictHit = Counter(listHit)
print(dictHit)


lista_nagrod = ['zielony', 'pomarańczowy', 'purpurowy', 'legendarny']
losowana_jedna = random.choice(lista_nagrod)
print('losowana_jedna', losowana_jedna)
losowana_wiele = random.choices(lista_nagrod, [80, 14, 5, 1], k=1000)
print('losowana_wiele = counter - ', Counter(losowana_wiele))






# VOC-DTP
# 1. Visualize
# 2. Outline
# 3. Code
# 4. Debug
# 5. Test
# 6. Polish

# import the stuff we require
from random import randint
from typing import Final

# -------------------------------------------------------------------------
# TYPE ALIAS:
# ===========
# Each time typing type as dict[str, str | int] is so boring, so we instead
# create a type alias and make our lives simpler.
# -------------------------------------------------------------------------
Character = dict[str, str | int]

# Super Heros
IRONMAN: Final[Character] = {"name": "Ironman", "attack_power": 250, "life": 1000}
BLACKWIDOW: Final[Character] = {"name": "Blackwidow", "attack_power": 180, "life": 800}
SPIDERMAN: Final[Character] = {"name": "Spiderman", "attack_power": 190, "life": 700}
HULK: Final[Character] = {"name": "Hulk", "attack_power": 300, "life": 1100}

# Super Villains
THANOS: Final[Character] = {"name": "Thanos", "attack_power": 1500, "life": 1500}
REDSKULL: Final[Character] = {"name": "Redskull", "attack_power": 300, "life": 800}
PROXIMA: Final[Character] = {"name": "Proxima", "attack_power": 320, "life": 800}

# All Super Heros & Super Villains
superheros: list[Character] = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
villains: list[Character] = [THANOS, REDSKULL, PROXIMA]

# Helper Variables
hero_life = 0
villain_life = 0

WIN_MSG: Final[str] = "You successfully saved Zortan!!!"
LOST_MSG: Final[str] = "Thanos killed Avergers and captured Zortan!!"

# Attack
for attack in range(3):
    # each iteration get a new hero & villain
    hero_index = randint(0, 3)
    villain_index = randint(0, 2)
    # helper variables
    current_superhero = superheros[hero_index]
    current_villain = villains[villain_index]
    # life
    hero_life += current_superhero['life']
    villain_life += current_villain['life']
    print(
        f"Attack: {attack + 1} => {current_superhero['name']} is going to fight with {current_villain['name']}."
        )
    # attack
    hero_life -= current_villain['attack_power']
    villain_life -= current_superhero['attack_power']

# Print a nice separating line
print("=" * 70)

# Win or Lose
if hero_life >= villain_life:
    print(WIN_MSG)
else:
    print(LOST_MSG)


# MSG = """
# --------------------------------------------------------------------
# Zortan is under attack, choose the pairs no. that will ataack Thanos

# 1) Ironman & Black Widow
# 2) Black Widow & Spiderman
# 3) Spiderman & Hulk
# 4) Hulk & Ironman
# --------------------------------------------------------------------
# """

# while True:

#     # win / loose 
#     if thanos_life <= 0 and attack_num <= 3:
#         # win
#         print(WIN_MSG)
#         break
#     elif attack_num >= 3:
#         # loose
#         print(LOST_MSG)
#         break


#     print(MSG)
#     choice = int(input("Enter your pair no >>> "))

#     if choice == 1:
#         print("Ironman & Black widow are attacking Thanos...")
#         thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
#         attack_num = attack_num + 1
#     elif choice == 2:
#         print("Black widow & Spiderman are attacking Thanos...")
#         thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
#         attack_num = attack_num + 1
#     elif choice == 3:
#         print("Spiderman & Hulk are attacking Thanos...")
#         thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
#         attack_num = attack_num + 1
#     elif choice == 4:
#         print("Hulk & Ironman are attacking Thanos...")
#         thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
#         attack_num = attack_num + 1

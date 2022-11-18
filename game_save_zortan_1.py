# VOC-DTP
# 1. Visualize
# 2. Outline
# 3. Code
# 4. Debug
# 5. Test
# 6. Polish

# import the stuff we require
from typing import Final

# indicating constant using all capitals
IRONMAN_ATTACK_POWER: Final[int] = 250 
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life: int = 1500
choice = 0
attack_num = 0

# declare ehelper messages
WIN_MSG: Final[str] = "You successfully saved Zortan!!!"
LOST_MSG: Final[str] = "Thanos killed Avergers and captured Zortan!!"

MSG = """
--------------------------------------------------------------------
Zortan is under attack, choose the pairs no. that will ataack Thanos

1) Ironman & Black Widow
2) Black Widow & Spiderman
3) Spiderman & Hulk
4) Hulk & Ironman
--------------------------------------------------------------------
"""

while True:

    # win / loose 
    if thanos_life <= 0 and attack_num <= 3:
        # win
        print(WIN_MSG)
        break
    elif attack_num >= 3:
        # loose
        print(LOST_MSG)
        break


    print(MSG)
    choice = int(input("Enter your pair no >>> "))

    if choice == 1:
        print("Ironman & Black widow are attacking Thanos...")
        thanos_life = thanos_life - IRONMAN_ATTACK_POWER - BLACKWIDOW_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 2:
        print("Black widow & Spiderman are attacking Thanos...")
        thanos_life = thanos_life - BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 3:
        print("Spiderman & Hulk are attacking Thanos...")
        thanos_life = thanos_life - SPIDERMAN_ATTACK_POWER - HULK_ATTACK_POWER
        attack_num = attack_num + 1
    elif choice == 4:
        print("Hulk & Ironman are attacking Thanos...")
        thanos_life = thanos_life - HULK_ATTACK_POWER - IRONMAN_ATTACK_POWER
        attack_num = attack_num + 1






"""
Save Zortan:
------------

Improve the design by using classes.
"""
# VOC-DTP
# 1. Visualize 2. Outline 3. Code 4. Debug 5. Test 6. Polish
# Convert the game logic into small fucntions


# import the stuff we require
from random import randint
from typing import Final
from enum import Enum, auto

class CharacterType(Enum):
    """Defined the Character Type"""
    SUPERHERO = auto()
    VILLAIN = auto()


class Character:
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        """Creates an instance of `Character`"""
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, Attack Power: {self.attack_power}, Life: {self.life}"
            )


class SuperHero(Character):
    """Superhero"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.SUPERHERO

    def __str__(self) -> str:
        return (
            f"Superhero => Name: {self.name}, Attack Power: {self.attack_power}, Life: {self.life}"
        )


class Villain(Character):
    """Superhero"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.VILLAIN

    def __str__(self) -> str:
        return (
            f"Villain => Name: {self.name}, Attack Power: {self.attack_power}, Life: {self.life}"
        )


# ------------------------------ Life -------------------------------------

class Life:
    """
    Helper class for managing Life.

    Note: Also see `Data Classes' for alternative solution.
    """

    # Class members
    hero_life = 0
    villain_life = 0

    @staticmethod # method for the class
    def inc_hero_life(life: int) -> None:
        """Increases Hero Life"""

        Life.hero_life += life

    @staticmethod
    def dec_hero_life(life: int) -> None:
        """Decreas Hero Life"""

        Life.hero_life -= life

    @staticmethod
    def inc_villain_life(life: int) -> None:
        """Increases villain Life"""

        Life.villain_life += life

    @staticmethod
    def dec_villain_life(life: int) -> None:
        """Decreas villain Life"""

        Life.villain_life -= life


# ---------------------------- Superheros ---------------------------------

def get_all_superherods() -> list[SuperHero]:
    # Super Heros
    ironman = SuperHero(name="Ironman", attack_power=250, life=1000)
    blackwidow = SuperHero(name="Blackwidow", attack_power=100, life=800)
    spiderman = SuperHero(name="Spiderman", attack_power=190, life=700)
    hulk = SuperHero(name="Hulk", attack_power=300, life=1100)

    superheros: list[SuperHero] = [ironman, blackwidow, spiderman, hulk]
    return superheros

def get_superhero(index: int) -> SuperHero | None:
    """Returns superhero from the given index."""

    superheros = get_all_superherods()
    if index < len(superheros):
        return superheros[index]
    else:
        # out of index
        return None

# ---------------------------- Villains ---------------------------------
def get_all_villains() -> list[Villain]:
    # Super Villains
    thanos = Villain(name="Thanos", attack_power=400, life=1500)
    redskull = Villain(name="Redskull", attack_power=300, life=800)
    proxima = Villain(name="Proxima", attack_power=320, life=800)

    villains: list[Villain] = [thanos, redskull, proxima]
    return villains

def get_villain(index: int) -> Villain | None:
    """Returns villain from the given index."""

    villains = get_all_villains()
    if index < len(villains):
        return villains[index]
    else:
        # out of index
        return None


# ---------------------------- Main Logic ---------------------------------
def attack() -> None:

    # Attack
    for attack_num in range(3):
        # each iteration get a new hero & villain
        hero_index = randint(0, 3)
        villain_index = randint(0, 2)

        current_superhero = get_superhero(hero_index)
        current_villain = get_villain(villain_index)

        if current_superhero and current_villain:
            # attack
            simulate_attack(attack_num, current_superhero, current_villain)
        else:
            print("Error! No superheros or villains to fight.")

        
def simulate_attack(attack_num: int, superhero: SuperHero, villain: Villain) -> None:
    """Simulate the actual attack."""

    # Set life
    Life.inc_hero_life(superhero.life)
    Life.inc_villain_life(villain.life)

    print(
        f"Attack: {attack_num + 1} => {superhero.name} is going to fight with {villain.name}."
    )

    # Actual attack
    Life.dec_hero_life(villain.attack_power)
    Life.dec_villain_life(superhero.attack_power)


# ---------------------------- Final Game Status --------------------------

def win_or_lose() -> None:
    """Determine if Avergers won or lost"""

    # declare helper messages
    WIN_MSG: Final[str] = "You successfully saved Zortan!!!"
    LOST_MSG: Final[str] = "Thanos killed Avergers and captured Zortan!!"

    # Print a nice separating line
    print("=" * 58)

    # Win or Lose
    if Life.hero_life >= Life.villain_life:
        print(WIN_MSG)
    else:
        print(LOST_MSG)

# ---------------------------- Main  --------------------------------------

def main() -> None:
    """Starts the Game"""
    attack()
    win_or_lose()

# ---------------------------- Start Game ---------------------------------
main()
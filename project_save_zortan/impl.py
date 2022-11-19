"""
Save Zortan:
------------

Practicing modules and packages
"""
# VOC-DTP
# 1. Visualize 2. Outline 3. Code 4. Debug 5. Test 6. Polish
# Convert the game logic into small fucntions

# import the stuff we require
from __future__ import annotations
from random import randint
# from typing import Final

from .constants import NUM_ATTACKS, WIN_MSG, LOST_MSG
from .models.superheros import SuperHeroModel
from .models.villains import VillainModel
from .schemas.player import Player
from .schemas.game_state import GameState
from .schemas.superhero import SuperHero
from .schemas.villain import Villain
from .schemas.life import Life


class Game:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.state = GameState.INITIALIZING
        self.superheros = SuperHeroModel()
        self.villains = VillainModel()

    def __repr__(self) -> str:
        return "<class 'Game'>"
    
    def __str__(self) -> str:
        return (
            f"Player: {self.player},\nState: {self.state},\nSuperheroes: {self.superheros},\n"
            f"Villains: {self.villains}"
            )

    # -------------------------- Attack ---------------------------------------------------
    def attack(self) -> Game:
        """Start the attack"""
        self.state = GameState.IN_PROGRESS
        print("Starting attack...")
        print(self.state)

        # Attack
        for attack_num in range(NUM_ATTACKS):
            # each iteration get a new hero & villain
            hero_index = randint(0, len(self.superheros.all) - 1)
            villain_index = randint(0, len(self.villains.all) - 1)

            current_superhero = self.superheros.get_superhero(hero_index)
            current_villain = self.villains.get_villain(villain_index)

            if current_superhero and current_villain:
                # attack
                self.__do_attack(attack_num, current_superhero, current_villain)
            else:
                print("Error! No superheros or villains to fight.")
        
        return self

            
    # private method
    def __do_attack(self, attack_num: int, superhero: SuperHero, villain: Villain) -> None:
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
    def win_or_lose(self) -> Game:
        """Determine if Avergers won or lost"""

        # Print a nice separating line
        print("=" * 58)

        # Win or Lose
        if Life.hero_life >= Life.villain_life:
            self.state = GameState.WIN
            print(WIN_MSG)
        else:
            self.state = GameState.LOST
            print(LOST_MSG)

        return self

# # ---------------------------- Main  --------------------------------------

# def main() -> None:
#     """Starts the Game"""
#     attack()
#     win_or_lose()

# # ---------------------------- Start Game ---------------------------------
# main()
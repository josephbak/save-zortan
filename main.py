"""
CLIENT:
-------
This module can be logically thought as a `client` as it consumes our API `game`
"""

from project_save_zortan import Game, Player

def main() -> None:
    """Game begins here"""

    p1 = Player("Louis", "Zappa")
    p2 = Player("Chiko", "Neutron")
    game1 = Game(p1)

    print(game1.state)
    print(game1)

    # method chaining by returning self
    game1 =game1.attack().win_or_lose()
    print(game1.state)

    print()

    game2 = Game(player=p2).attack().win_or_lose()


main()
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
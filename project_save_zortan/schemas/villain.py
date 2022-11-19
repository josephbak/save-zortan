from .character import Character
from .chatacter_type import CharacterType


class Villain(Character):
    """Superhero"""

    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.VILLAIN

    def __str__(self) -> str:
        return (
            f"Villain => Name: {self.name}, Attack Power: {self.attack_power}, Life: {self.life}"
        )
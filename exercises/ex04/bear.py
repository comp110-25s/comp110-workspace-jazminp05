"""File to define Bear class."""

__author__ = "730672588"


class Bear:
    """Beginning of the Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes the bear class."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """What occurs in one day to the bear population."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bears eating habits."""
        self.hunger_score += num_fish
        return None

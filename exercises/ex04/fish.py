"""File to define Fish class."""

__author__ = "730672588"


class Fish:
    """Beginning of fish class."""

    age: int

    def __init__(self):
        """Initializes fish class."""
        self.age = 0

    def one_day(self):
        """What happens in one day to the fish populaiton."""
        self.age += 1
        return None

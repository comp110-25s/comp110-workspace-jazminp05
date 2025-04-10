__author__ = "730672588"


"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """checks tha age of the fish and bears, removing if too old"""
        remaining_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                remaining_fish.append(fish)
        self.fish = remaining_fish
        remaining_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                remaining_bears.append(bear)
        self.bears = remaining_bears
        return None

    def bears_eating(self):
        """defines what bears need to eat"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """defines the hunger of the bears"""
        fed_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                fed_bears.append(bear)
        self.bears = fed_bears
        return None

    def repopulate_fish(self):
        """fish repopulation"""
        baby_bears = len(self.bears) // 2
        idx = 0
        while idx < baby_bears:
            self.bears.append(Bear())
            idx += 1
        return None

    def repopulate_bears(self):
        """bear repopulation"""
        baby_fish = (len(self.fish) // 2) * 4
        idx = 0
        while idx < baby_fish:
            self.fish.append(Fish())
            idx += 1
        return None

    def view_river(self):
        """animal count in river by day"""
        x = self.day
        y = len(self.fish)
        z = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """simulates what happens in the river in a week"""
        days_passed = 1
        while days_passed < 7:
            self.one_river_day()
            days_passed += 1
        return None

    def remove_fish(self, amount: int):
        """removes fish from the river"""
        idx = 0
        while idx < amount and self.fish:
            self.fish.pop(0)
            idx += 1
        return None

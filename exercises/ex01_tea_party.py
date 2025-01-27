"""plan a tea party: tea, treats, and cost"""

__author__: str = "730672588"


def main_planner(guests: int) -> None:
    """guests attending the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """tea needed for each guest"""
    return 2 * people


def treats(people: int) -> int:
    """treats needed for each guest"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """total cost to host the tea party"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

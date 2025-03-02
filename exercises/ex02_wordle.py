"""Guess the word in 6 tries or less!"""

__author__: str = "730672588"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    guessed: bool = False
    while turn < 6 and not guessed:
        turn = turn + 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        box_string = emojified(guess, secret)
        print(box_string)

        if guess == secret:
            guessed = True
            print(f"You won in {turn}/6 turns!")
        else:
            if turn == 6:
                print("X/6 - Sorry, try again tomorrow!")


def contains_char(search_string: str, find_character: str) -> bool:
    """Finds a character in a given string"""

    assert len(find_character) == 1, f"len('{find_character}') is not 1"
    idx: int = 0
    while idx < len(search_string):
        if search_string[idx] == find_character:
            return True
        idx = idx + 1
    else:
        return False


def emojified(guess: str, hidden: str) -> str:
    """Changes the guessed word into colored boxes if in the correct position."""
    assert len(guess) == len(hidden), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    emoji: str = ""

    while idx < len(guess):
        if guess[idx] == hidden[idx]:
            emoji = emoji + GREEN_BOX

        elif contains_char(hidden, guess[idx]):
            emoji = emoji + YELLOW_BOX

        else:
            emoji = emoji + WHITE_BOX
        idx = idx + 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Gives feedback based on length of the input value."""
    guess: str = input(f"Enter a {expected_length} character word:")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


if __name__ == "__main__":
    main(secret="codes")

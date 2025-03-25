__author__ = "730672588"


def invert(original: dict[str, str]) -> dict[str, str]:
    """inverts the keys and values for a dictionary."""
    inverted_dict = {}
    for key in original:
        value = original[key]
        if value in inverted_dict:
            raise KeyError("Oops! You can't have the same key. Try again.")
        inverted_dict[value] = key
    return inverted_dict


def count(frequency: list[str]) -> dict[str, int]:
    """counts how many times an item appears in a list and returns to a dict."""
    count_dict = {}

    for item in frequency:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def favorite_color(colors: dict[str, str]) -> str:
    """determines most liked color from a dictionary."""
    color_list = []
    for name in colors:
        color: str = colors[name]
        color_list.append(color)

    appearances = count(color_list)
    most_apps = ""
    max_count = 0

    for color in color_list:
        if appearances[color] > max_count:
            most_apps = color
            max_count = appearances[color]
    return most_apps


def bin_len(string: list[str]) -> dict[int, set[str]]:
    """organizes list of strings into a dictionary by length."""
    bins = {}
    for characters in string:
        length = len(characters)

        if length not in bins:
            bins[length] = set()
        bins[length].add(characters)
    return bins

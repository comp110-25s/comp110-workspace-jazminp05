__author__ = "730672588"


from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len
import pytest


def test_invert() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}
    assert invert({"op": "81", "mv": "1", "cl": "16"}) == {
        "81": "op",
        "1": "mv",
        "16": "cl",
    }
    assert invert({}) == {}
    with pytest.raises(KeyError):
        my_dict = {"jazmin": "puebla", "jolette": "puebla"}
        assert invert(my_dict) == KeyError


def test_count() -> None:
    assert count(["a", "a", "a"]) == {"a": 3}
    assert count(["apple", "apple", "orange", "cherry", "grape", "cherry"]) == {
        "apple": 2,
        "orange": 1,
        "cherry": 2,
        "grape": 1,
    }
    assert count([]) == {}


def test_favortie_color() -> None:
    assert (
        favorite_color(
            {
                "carlos": "blue",
                "nico": "green",
                "oscar": "orange",
                "charles": "red",
                "lando": "orange",
            }
        )
        == "orange"
    )
    assert (
        favorite_color(
            {
                "carlos": "blue",
                "alex": "blue",
                "oscar": "orange",
                "charles": "red",
                "lando": "orange",
            }
        )
        == "blue"
    )
    assert favorite_color({}) == ""


def test_bin_len() -> None:
    assert bin_len(["ice", "water", "steam"]) == {3: {"ice"}, 5: {"water", "steam"}}
    assert bin_len(["sleep", "sleep", "study"]) == {5: {"sleep", "study"}}
    assert bin_len([]) == {}

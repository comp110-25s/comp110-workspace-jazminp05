__author__ = "730672588"


from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len
import pytest


def test_invert_use_1() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_2() -> None:
    assert invert({"op": "81", "mv": "1", "cl": "16"}) == {
        "81": "op",
        "1": "mv",
        "16": "cl",
    }


def test_invert_empty() -> None:
    assert invert({}) == {}


def test_invert_KeyError() -> None:
    with pytest.raises(KeyError):
        my_dict = {"jazmin": "puebla", "jolette": "puebla"}
        assert invert(my_dict) == KeyError


def test_count_use_1() -> None:
    assert count(["a", "a", "a"]) == {"a": 3}


def test_count_use_2() -> None:
    assert count(["apple", "apple", "orange", "cherry", "grape", "cherry"]) == {
        "apple": 2,
        "orange": 1,
        "cherry": 2,
        "grape": 1,
    }


def test_count_empty() -> None:
    assert count([]) == {}


def test_favortie_color_use() -> None:
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


def test_favortie_color_tie() -> None:
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


def test_favortie_color_empty() -> None:
    assert favorite_color({}) == ""


def test_bin_len_use() -> None:
    assert bin_len(["ice", "water", "steam"]) == {3: {"ice"}, 5: {"water", "steam"}}


def test_bin_len_use_2() -> None:
    assert bin_len(["sleep", "sleep", "study"]) == {5: {"sleep", "study"}}


def test_bin_len_empty() -> None:
    assert bin_len([]) == {}

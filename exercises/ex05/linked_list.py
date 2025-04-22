"""Exercise 05."""

from __future__ import annotations

__author__ = "730672588"


class Node:
    """Defines class Node."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None) -> None:
        """Node constructor."""
        self.value = val
        self.next = next


"""Node objects."""
two: Node = Node(2, None)
one: Node = Node(1, two)


def value_at(head: Node | None, idx: int) -> int:
    """Defines value_at function using the Node class."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if idx == 0:
        return head.value
    return value_at(head.next, idx - 1)


def max(head: Node | None) -> int:
    """Defines max function using the Node class."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    else:
        rest: int = max(head.next)
        return head.value + rest


def linkify(items: list[int]) -> Node | None:
    """Defines linkify function using the Node class."""
    if not items:
        return None
    head = Node(items[0], linkify(items[1:]))
    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Defines scale function using the Node class."""
    if head is None:
        return None
    scaled = Node(head.value * factor, scale(head.next, factor))
    return scaled

"""
a modle of a stacktree class
"""
from game import Game


class Stack:
    """
    Last-in, first-out (LIFO) stack.
    """

    def __init__(self) -> None:
        """
        Create a new, empty Stack self.

        >>> s = Stack()
        """
        self._contents = []

    def add(self, obj: object) -> None:
        """
        Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(7)
        """
        self._contents.append(obj)

    def remove(self) -> "Tree":
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty.

        doctest moited becasue of tree
        """
        return self._contents.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(7)
        >>> s.is_empty()
        False
        """
        return len(self._contents) == 0


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    ****Attributes****
    game1: Game
    """
    game1: Game

    def __init__(self, game1: Game, score=None, children=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.score = score
        self.game1 = game1
        self.children = children[:] if children is not None else []


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

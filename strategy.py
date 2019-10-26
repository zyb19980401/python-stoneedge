"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from copy import copy
from stacktree import Stack
from stacktree import Tree
from game import Game


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def helper(game: Any) ->int:
    """
    input ta game into and return the score of all possible moves
    """
    all_games = []
    for i in game.current_state.get_possible_moves():
        game3 = copy(game)
        game3.current_state = game.current_state.make_move(i)
        all_games.append(game3)
    if game.is_over(game.current_state):
        if not game.is_winner('p1') and not game.is_winner('p2'):
            return 0
        elif not game.is_winner(game.current_state.get_current_player_name()):
            return -1
        return 1
    else:
        return max([-1*helper(x) for x in all_games])


def minimax_strategy(game: Any) -> Any:
    """
    Return a move for game through minimaxly asking the user for input.
    """
    allmoves = []
    allscores = []
    for i in game.current_state.get_possible_moves():
        allmoves.append(i)
        game2 = copy(game)
        game2.current_state = game.current_state.make_move(i)
        allscores.append(helper(game2))
    allscores = [-1 * x for x in allscores]
    if 1 in allscores:
        return allmoves[allscores.index(1)]
    elif 0 in allscores:
        return allmoves[allscores.index(0)]
    return allmoves[0]


def interminimax_strategy(game: Game) -> Any:
    """
     Return a move for game through minimaxly asking
     the user for input but without recursive.
    """

    tree1 = Tree(game)
    a = Stack()
    a.add(tree1)
    while not a.is_empty():
        firstree = a.remove()
        if firstree.children == [] and \
                firstree.game1.is_over(firstree.game1.current_state):
            if not firstree.game1.is_winner('p1') and \
                    not firstree.game1.is_winner('p2'):
                firstree.score = 0
            player = firstree.game1.current_state.get_current_player_name()
            if not firstree.game1.is_winner(player):
                firstree.score = -1
            else:
                firstree.score = 1
        elif firstree.children == [] and \
                firstree.game1.current_state.get_possible_moves() != []:
            a.add(firstree)
            for i in firstree.game1.current_state.get_possible_moves():
                gamecopy = copy(firstree.game1)
                state = firstree.game1.current_state.make_move(i)
                gamecopy.current_state = state
                subtree = Tree(gamecopy)
                firstree.children.append(subtree)
                a.add(subtree)
        elif firstree.children != []:
            firstree.score = max([-1 * i.score for i in firstree.children])
    listscore = []
    for i in tree1.children:
        listscore.append(-1 * i.score)
    listmoves = []
    for x in tree1.game1.current_state.get_possible_moves():
        listmoves.append(x)
    if 1 in listscore:
        return listmoves[listscore.index(1)]
    elif 0 in listscore:
        return listmoves[listscore.index(0)]
    return listmoves[0]


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")

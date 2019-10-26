"""
the class of stonehenge game
"""
from game import Game
from stonestate import Stonestate


def get_markers(n: int) -> dict:
    """
    get the markers of a new game
    """
    a = {}
    if n == 1:
        a[1], a[2], a[3], a[4] = ['@1', '@2'], ['@6'], ['@5', '@3'], ['@4']
    if n == 2:
        a[1], a[2], a[3], a[4], a[5] = ['@1', '@2'], \
                                       ['@9', '@3'], ['@8'], \
                                       ['@7', '@4'], ['@6', '@5']
    if n == 3:
        a[1], a[2], a[3], a[4], a[5], a[6] = ['@1', '@2'], ['@12', '@3'], \
                                             ['@11', '@4'], \
                                             ['@10'], ['@9', '@5'], \
                                             ['@8', '@7', '@6']
    if n == 4:
        a[1], a[2], a[3], a[4], a[5], a[6], a[7] = ['@1', '@2'], \
                                                   ['@15', '@3'], \
                                                   ['@14', '@4'], \
                                                   ['@13', '@5'], ['@12'], \
                                                   ['@11', '@6'], \
                                                   ['@10', '@9', '@8', '@7']
    if n == 5:
        a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8] = \
            ['@1', '@2'], ['@18', '@3'], ['@17', '@4'], \
            ['@16', '@5'], ['@15', '@6'], ['@14'], ['@13', '@7'], \
            ['@12', '@11', '@10', '@9', '@8']
    return a


def get_lines(n: int) -> dict:
    """
    get lines of a new game
    """
    b = {}
    if n == 1:
        b['@1'], b['@2'], b['@3'], b['@4'], b['@5'], b['@6'] = \
            ['A'], ['B', 'C'], \
            ['B'], ['C', 'A'], ['C'], ['A', 'B']
    if n == 2:
        b['@1'], b['@2'], b['@3'], b['@4'], \
         b['@5'], b['@6'], b['@7'], b['@8'], b['@9'] = \
         ['A', 'C'], ['B', 'D', 'F'], ['E', 'G'], \
         ['E', 'B'], ['G', 'D', 'A'], ['F', 'C'], \
         ['F', 'G'], \
         ['C', 'D', 'E'], ['A', 'B']
    if n == 3:
        b['@1'], b['@2'], b['@3'], b['@4'], b['@5'], \
         b['@6'], b['@7'], b['@8'], b['@9'], b['@10'], b['@11'], \
         b['@12'] = ['A', 'C', 'F'], ['B', 'D', 'G', 'J'], \
                    ['E', 'H', 'K'], ['I', 'L'], \
                    ['I', 'E', 'B'], ['L', 'H', 'D', 'A'], \
                    ['K', 'G', 'C'], ['J', 'F'], \
                    ['J', 'K', 'L'], ['F', 'G', 'H', 'I'], \
                    ['C', 'D', 'E'], ['A', 'B']
    if n == 4:
        b['@1'], b['@2'], b['@3'], b['@4'], \
         b['@5'], b['@6'], b['@7'], b['@8'], b['@9'], b['@10'], \
         b['@11'], b['@12'], b['@13'], b['@14'], \
         b['@15'] = ['A', 'C', 'F', 'J'], \
                    ['B', 'D', 'G', 'K', 'O'],\
                    ['E', 'H', 'L', 'P'], \
                    ['I', 'M', 'Q'], ['N', 'R'],\
                    ['N', 'I', 'E', 'B'], \
                    ['R', 'M', 'H', 'D', 'A'], \
                    ['Q', 'L', 'G', 'C'], \
                    ['P', 'K', 'F'], ['O', 'J'], \
                    ['O', 'P', 'Q', 'R'], \
                    ['J', 'K', 'L', 'M', 'N'], \
                    ['F', 'G', 'H', 'I'], \
                    ['C', 'D', 'E'], ['A', 'B']
    if n == 5:
        b['@1'], b['@2'], b['@3'], \
         b['@4'], b['@5'], b['@6'], \
         b['@7'], b['@8'], b['@9'], b['@10'], b['@11'], \
         b['@12'], b['@13'], b['@14'], b['@15'],\
         b['@16'], b['@17'], \
         b['@18'] = ['A', 'C', 'F', 'J', 'O'], \
                    ['B', 'D', 'G', 'K', 'P', 'U'], \
                    ['E', 'H', 'L', 'Q', 'V'],\
                    ['I', 'M', 'R', 'W'], \
                    ['N', 'S', 'X'], ['T', 'Y'], \
                    ['T', 'N', 'I', 'E', 'B'], \
                    ['Y', 'S', 'M', 'H', 'D', 'A'],\
                    ['X', 'R', 'L', 'G', 'C'],\
                    ['W', 'Q', 'K', 'F'], \
                    ['V', 'P', 'J'], ['U', 'O'], \
                    ['U', 'V', 'W', 'X', 'Y'], \
                    ['O', 'P', 'Q', 'R', 'S', 'T'], \
                    ['J', 'K', 'L', 'M', 'N'], \
                    ['F', 'G', 'H', 'I'], \
                    ['C', 'D', 'E'], ['A', 'B']

    return b


def get_letters(n: int) -> dict:
    """
    get letters of a new games
    """
    c = {}
    if n == 1:
        c[2], c[3] = ['A', 'B'], ['C']
    if n == 2:
        c[2], c[3], c[4] = ['A', 'B'], ['C', 'D', 'E'], ['F', 'G']
    if n == 3:
        c[2], c[3], c[4], c[5] = \
            ['A', 'B'], ['C', 'D', 'E'], \
            ['F', 'G', 'H', 'I'], \
            ['J', 'K', 'L']
    if n == 4:
        c[2], c[3], c[4], c[5], c[6] = ['A', 'B'], ['C', 'D', 'E'], \
                                       ['F', 'G', 'H', 'I'], \
                                       ['J', 'K', 'L', 'M', 'N'], \
                                       ['O', 'P', 'Q', 'R']
    if n == 5:
        c[2], c[3], c[4], c[5], c[6], c[7] = ['A', 'B'], \
                                             ['C', 'D', 'E'], \
                                             ['F', 'G', 'H', 'I'], \
                                             ['J', 'K', 'L', 'M', 'N'],\
                                             ['O', 'P', 'Q', 'R', 'S', 'T'], \
                                             ['U', 'V', 'W', 'X', 'Y']
    return c


class Stonegame(Game):
    """
    Abstract class for a stonegame to be played with two players
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        initialize a new stone game
        """
        self.side_length = input('what is the side_length of the input')
        letters = get_letters(int(self.side_length))
        markers = get_markers(int(self.side_length))
        lines = get_lines(int(self.side_length))
        self.mix = [markers, lines, letters]
        self.current_state = Stonestate(p1_starts, self.mix)
        self.size = self.side_length
        self.p1_starts = p1_starts

    def get_instructions(self) -> str:
        """
        return the instruction of the game
        """
        return 'the Players take turns claiming \
        cells (in the diagram: circles labelled with a capital \
        letter). When a playercaptures at least \
        half of the cells in a ley-line (in the diagram: hexagons\
         with a line connecting it to cells),then the \
         player captures that ley-line. The first player to \
         capture at least half of the ley-lines is the winner'

    def is_over(self, state: Stonestate) -> bool:
        """
        return true iff over over half of the markers are captuared
        example are omited becasue of input
        """
        a = []
        markers = state.mix[0]
        for i in markers:
            a.extend(markers[i])
        if (a.count('p1') >= 0.5 * len(a)) or (a.count('p2') >= 0.5 * len(a)):
            return True
        return False

    def is_winner(self, player: str) -> bool:
        """
        return true if player is the winner
        example ommited becasue of input
        """
        if self.is_over(self.current_state):
            if self.current_state.is_p1_turn:
                return player == "p2"
            return player == "p1"
        return False

    def str_to_move(self, string: str) -> str:
        """
        tranform input str into move
        """
        return string


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")

"""
a modle of a stonestate
"""

from typing import Any
from game_state import GameState


def get_new_diction(olddict: dict)->dict:
    """
    return a identical dictionary but not change the old one
    >>> letters = {2: ['A', 'B'], 3: ['C']}
    >>> a = get_new_diction(letters)
    >>> letters[2] = 0
    >>> letters == a
    False
    >>> a
    {2: ['A', 'B'], 3: ['C']}
    >>> letters
    {2: 0, 3: ['C']}
    """
    temp = {}
    for z in olddict:
        temp[z] = []
        for y in olddict[z]:
            temp[z].append(y)
    return temp


def change_diction(diction: dict, move: Any, p1turn: bool) -> None:
    """
    change the dicitonary by the move
    >>> dicts = {2: ['B', 'D','F'], 3: ['A','B'],4:['E','B']}
    >>> move = 'B'
    >>> p1turn = True
    >>> change_diction(dicts,move,p1turn)
    >>> dicts
    'ddd'
    """
    items = diction.items()
    for x in items:
        if move in x[1]:
            location = x[0]
            helper_change_dictionary(diction, location, p1turn, move)


def helper_change_dictionary(dictionary: dict, location1: int,
                             isp1turn: bool, move: Any) -> None:
    """
    >>> dicts = {2: ['B', 'D', 'F'], 3: ['A', 'B'], 4: ['E', 'B']}
    >>> move = 'B'
    >>> p1turn = True
    >>> location1 = 2
    >>> helper_change_dictionary(dicts, location1,p1turn, move)
    >>> dicts
    {2: ['p1', 'D', 'F'], 3: ['A', 'B'], 4: ['E', 'B']}
    """

    for i in range(len(dictionary[location1])):
        if dictionary[location1][i] == move:
            if isp1turn:
                dictionary[location1][i] = 'p1'
            else:
                dictionary[location1][i] = 'p2'


def change_markers(diction: dict)->dict:
    """
    change the value of dictionary if @ has number,\
    without changing dictionary if it is p1 or p2
    >>> a = {1: ['p1', '@2'], 2: ['p1', '@3'], 3: ['@8'], 4: ['@7', '@4'], 5: ['@6', '@5']}
    >>> change_markers(a)
    {1: ['1', '@'], 2: ['1', '@'], 3: ['@'], 4: ['@', '@'], 5: ['@', '@']}
    """
    b = get_new_diction(diction)
    for i in b:
        for x in range(len(b[i])):
            if '@' in b[i][x]:
                b[i][x] = '@'
            if 'p' in b[i][x]:
                b[i][x] = b[i][x][1]
    return b


def helper_makemove1(temp11: dict, turn: bool, name1: str)->None:
    """
    change the temp11'value if it is the same as name
    nested bloks
        >>> markers={1: ['@1','@2'], 2: ['@6'], 3:['@5','@3'],4: ['@4']}
        >>> turn = True
        >>> name1 = '@1'
        >>> helper_makemove1(markers,turn,name1)
        >>> markers
        {1: ['p1', '@2'], 2: ['@6'], 3: ['@5', '@3'], 4: ['@4']}
    """
    for item in temp11:
        for i in range(len(temp11[item])):
            if temp11[item][i] == name1 and turn:
                temp11[item][i] = 'p1'
            if temp11[item][i] == name1 and not turn:
                temp11[item][i] = 'p2'


def helper_makemove_letters(temp33: dict, move: str, p1turn: bool) -> None:
    """
    a helper function of makemove to change the value in \
    the dictionary of letters
    >>> letters = {2: ['A', 'B'], 3: ['C']}
    >>> helper_makemove_letters(letters,'A',True)
    >>> letters
    {2: ['p1', 'B'], 3: ['C']}

    """
    for gg in temp33:
        for ii in range(len(temp33[gg])):
            if move == temp33[gg][ii] and p1turn:
                temp33[gg][ii] = 'p1'
            if move == temp33[gg][ii] and not p1turn:
                temp33[gg][ii] = 'p2'


class Stonestate(GameState):
    """
    a Stonegame class for the stonegame
    """
    mix: list
    siez: int
    is_p1_turn: bool

    def __init__(self, is_p1_turn: bool, mix: list) -> None:
        GameState.__init__(self, is_p1_turn)
        self.mix = mix
        self.size = self.get_size()
        self.is_p1_turn = is_p1_turn

    def get_size(self) -> int:
        """
        get the size of the current game state
        >>> markers={1: ['@1','@2'], 2: ['@6'], 3:['@5','@3'],4: ['@4']}
        >>> lines={'@1': ['A'], '@2': ['B', 'C'], '@3': ['B'], '@4':['C','A'],'@5':['C'],'@6':['A','B']}
        >>> letters = {2: ['A', 'B'], 3: ['C']}
        >>> mix = [markers,lines,letters]
        >>> a = Stonestate(True,mix)
        >>> a.get_size()
        1
        """
        size = len(self.mix[2])-1
        return size

    def __str__(self) -> str:
        """
        make a string representation of a stonestate
        >>> markers={1: ['@1','@2'], 2: ['@6'], 3:['@5','@3'],4: ['@4']}
        >>> lines={'@1': ['A'], '@2': ['B', 'C'], '@3': ['B'], '@4':['C','A'],'@5':['C'],'@6':['A','B']}
        >>> letters = {2: ['A', 'B'], 3: ['C']}
        >>> mix = [markers,lines,letters]
        >>> a = Stonestate(True,mix)
        >>> print(a)
              @   @
             /   /
        @ - A - B
             \\ / \\
          @ - C   @
               \\
                @
        """
        markersori = self.mix[0]
        lettersori = self.mix[2]
        markers = change_markers(markersori)
        letters = change_markers(lettersori)
        temp = '      '+markers[1][0]+'   ' +\
               markers[1][1] + '\n' + '     /   /\n'
        for i in range(self.size-1):
            num = i + 2
            temp += (markers[num][0])
            for g in letters[num]:
                temp += (' - ' + g)
            temp += ('   ' + markers[num][1])
            temp += '\n'
            temp += '   '
            for _ in range(len(letters[num])):
                temp += (' /' + ' \\')
            temp += ' /'
            temp += '\n'
        temp += markers[self.size+1][0]
        for x in letters[self.size+1]:
            temp += ' - '
            temp += x
        temp += '\n'
        temp += '    '
        for _ in range(self.size):
            temp += (' \\' + ' /')
        temp += (' \\' + '\n')
        temp += ('  ' + markers[self.size + 2][0])
        for z in letters[self.size + 2]:
            temp += (' - '+z)
        temp += ('   '+markers[self.size+2][1])
        temp += ('\n'+'    ')
        for _ in range(self.size):
            temp += '   \\'
        temp += ('\n'+'     ')
        for xx in markers[self.size+3]:
            temp += ('   '+xx)
        return temp

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        >>> markers={1: ['@1','@2'], 2: ['@6'], 3:['@5','@3'],4: ['@4']}
        >>> lines={'@1': ['A'], '@2': ['B', 'C'], '@3': ['B'], '@4':['C','A'],'@5':['C'],'@6':['A','B']}
        >>> letters = {2: ['A', 'B'], 3: ['C']}
        >>> mix = [markers,lines,letters]
        >>> a = Stonestate(True,mix)
        >>> b = a.make_move('B')
        >>> b.get_possible_moves()
        []
        """
        a = []
        b = []
        letters = self.mix[2]
        c = []
        markers = self.mix[0]
        for i in markers:
            c.extend(markers[i])
        if (c.count('p1') >= 0.5 * len(c)) or (c.count('p2') >= 0.5 * len(c)):
            return []
        for i in letters:
            a.extend(letters[i])
        for x in a:
            if x not in 'p1p2':
                b.append(x)
        return b

    def make_move(self, move: Any) -> 'GameState':
        """
        Return the GameState that results from applying move to this GameState.
        >>> markers={1: ['@1','@2'], 2: ['@6'], 3:['@5','@3'],4: ['@4']}
        >>> lines={'@1': ['A'], '@2': ['B', 'C'], '@3': ['B'], '@4':['C','A'],'@5':['C'],'@6':['A','B']}
        >>> letters = {2: ['A', 'B'], 3: ['C']}
        >>> mix = [markers,lines,letters]
        >>> a = Stonestate(True,mix)
        >>> b = a.make_move('B')
        >>> b.p1_turn
        False
        """
        temp1 = get_new_diction(self.mix[0])
        temp2 = get_new_diction(self.mix[1])
        temp22 = get_new_diction(self.mix[1])
        temp3 = get_new_diction(self.mix[2])
        turns = self.is_p1_turn
        change_diction(temp2, move, turns)
        change_diction(temp3, move, turns)
        change_diction(temp22, move, turns)
        a = []
        if self.is_p1_turn:
            for x in temp2:
                if (temp2[x].count('p1') >= 0.5*len(temp2[x])) and \
                        ('p1' not in x) and ('p2' not in x):
                    temp22[(x+'p1')] = temp2[x]
                    a.append(x)
            for item in a:
                del temp22[item]
        else:
            for x in temp2:
                if (temp2[x].count('p2') >= 0.5*len(temp2[x])) and\
                        ('p1' not in x) and ('p2' not in x):
                    temp22[(x+'p2')] = temp2[x]
                    a.append(x)
            for item in a:
                del temp22[item]
        temp22key = temp22.keys()
        for z in temp22key:
            if 'p' in z:
                name = z[:z.index('p')]
                helper_makemove1(temp1, self.is_p1_turn, name)
                helper_makemove_letters(temp3, move, self.is_p1_turn)
        if turns:
            turns = False
        else:
            turns = True
        newstate = Stonestate(turns, [temp1, temp22, temp3])
        return newstate

    def __repr__(self) -> str:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return 'The current player is p1 {}, the board is \n {}'.\
            format(self.is_p1_turn, str(self))

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        >>> markers={1: ['@1','@2'], 2: ['@6'], 3:['@5','@3'],4: ['@4']}
        >>> lines={'@1': ['A'], '@2': ['B', 'C'], '@3': ['B'], '@4':['C','A'],'@5':['C'],'@6':['A','B']}
        >>> letters = {2: ['A', 'B'], 3: ['C']}
        >>> mix = [markers,lines,letters]
        >>> a = Stonestate(True,mix)
        >>> a.rough_outcome()
        1
        """
        result = []
        if self.get_possible_moves() == []:
            return self.LOSE
        for i in self.get_possible_moves():
            if self.make_move(i).get_possible_moves() == []:
                return self.WIN
            acc = []
            for x in self.make_move(i).get_possible_moves():
                a = self.make_move(i).make_move(x).get_possible_moves() == []
                acc.append(a)
            result.append(any(acc))
        if all(result):
            return self.LOSE
        return 0


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

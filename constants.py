##start arrangement

CHESS_BOARD = [
    ['0R', '0H', '0B', '0K', '0Q', '0B', '0H', '0R'],
    ['0P', '0P', '0P', '0P', '0P', '0P', '0P', '0P'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['1P', '1P', '1P', '1P', '1P', '1P', '1P', '1P'],
    ['1R', '1H', '1B', '1K', '1Q', '1B', '1H', '1R']
]

CHESS_BOARD_COLOR = [
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0]
]

KING = 'K'
QUEEN = 'Q'
HORSE = 'H'
ROOK = 'R'
PAWN = 'P'
BISHOP = 'B'
BLACK=0
WHITE=1
EMPTY = '__'

BLACK_PIECE_LIST = ['0R', '0H', '0B', '0K', '0Q', '0B', '0H', '0R', '0P', '0P', '0P', '0P', '0P', '0P', '0P', '0P']
WHITE_PIECE_LIST = ['1R', '1H', '1B', '1K', '1Q', '1B', '1H', '1R', '1P', '1P', '1P', '1P', '1P', '1P', '1P', '1P']


## different chess boards
ROWS = 8
COLUMNS = 8

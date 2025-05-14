import constants
import os
import pandas as pd



def start_position_of_chess_grid(page):
    for i in range(page.shape[0]):
        for j in range(page.shape[1]):
            if page.iloc[i,j]=='*':
                vertical = i+1
                horizontal = j+1
                return (page.iloc[ vertical: vertical+8, horizontal: horizontal+8 ]).fillna('__').values.tolist()
    raise Exception("chess grid not in order in excel file")
    
    
def read_chess_board(file_name):
    page = pd.read_excel(file_name, engine='openpyxl', header=None)
    board = start_position_of_chess_grid(page) # h = horizontal, v = vertical
    return board

def position(board, val):
    for i in range(constants.ROWS):
        for j in range(constants.COLUMNS):
            if board[i][j]==val:
                return (i,j)

def get_position(color, board, piece):
    return position(board, str(color)+piece)

def show(config, length_):
    os.system("cls")
    ''' displays chess board on console'''
    board = config[1]
    print("\n",end='')
    for i in range(constants.ROWS):
        for j in range(constants.COLUMNS):
            print(board[i][j]+" ",end='')
        print ("\n")
    print("\ntotal config(s) = "+str(length_),end='')

    '''
    white_pieces_eliminated = pieces_eliminated(board, constants.WHITE)
    black_pieces_eliminated = pieces_eliminated(board, constants.BLACK)
    print("\nblack: ",end='')
    for i in range(len(black_pieces_eliminated)):
        print(black_pieces_eliminated[i]+"  ", end='')
    print("\n",end='')
    
    print("\nwhite: ",end='')
    for i in range(len(white_pieces_eliminated)):
        print (white_pieces_eliminated[i]+"  ", end='')
    print("\n",end='')
    '''


'''
def pieces_eliminated(board, color):
    pieces_remaining = []
    full_list = []
    if color==constants.BLACK:
        full_list = constants.BLACK_PIECE_LIST
    else:
        full_list = constants.WHITE_PIECE_LIST
    for i in range(constants.ROWS):
        for j in range(constants.COLUMNS):
            if board[i][j][0]==str(color):
                pieces_remaining += board[i][j]
    return (list)(set(full_list)-set(pieces_remaining))
'''


'''
def is_check_mate(config, color):
    board = config[1]
    pos = helper_functions.get_position(color, board, constants.KING)
    checkmate = True
    x = pos[0]
    y = pos[1]
    #check for if king is in a checkmate
    #same pos
    checkmate = checkmate and threat_on_pos(board, (x,y))
    
    # n-w
    checkmate = checkmate and board[x-1][y-1][0]!=str(color) and threat_on_pos(board, (x-1, y-1))
    
    # n
    checkmate = checkmate and board[x-1][y][0]!=str(color) and threat_on_pos(board, (x-1, y))
    
    # n-e
    checkmate = checkmate and board[x-1][y+1][0]!=str(color) and threat_on_pos(board, (x-1, y+1))
    
    # w
    checkmate = checkmate and board[x][y-1][0]!=str(color) and threat_on_pos(board, (x, y-1))
    
    # e
    checkmate = checkmate and board[x][y+1][0]!=str(color) and threat_on_pos(board, (x, y+1))

    # s-w
    checkmate = checkmate and board[x+1][y-1][0]!=str(color) and threat_on_pos(board, (x+1, y-1))
    
    # s
    checkmate = checkmate and board[x+1][y][0]!=str(color) and threat_on_pos(board, (x+1, y))

    # s-e
    checkmate = checkmate and board[x+1][y+1][0]!=str(color) and threat_on_pos(board, (x+1, y+1))
    
    if not checkmate:
        return False
    # check if some other piece can intervene to save king
    piece_pos = get_pos_of_piece_threatening_the_pos(board, (x,y)) #because checkmate flag is true till here, this list is not empty
    if len(piece_pos)>1:
        return True
    else:

    if helper_functions.threat_on_pos(board, pos) and any_place_to_safety(board, pos):
        return True
    return False
'''
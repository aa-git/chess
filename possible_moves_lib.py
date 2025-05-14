import constants
def inside_board(i, j):
    if i>=0 and i<constants.ROWS and j >= 0 and j < constants.COLUMNS:
        return True
    return False

def possible_moves(pos, board):
    color = (int)(board[pos[0]][pos[1]][0])
    i = pos[0]
    j = pos[1]
    if board[pos[0]][pos[1]][1]==constants.PAWN:
        return moves_of_pawn(i, j, board, color)
    
    if board[pos[0]][pos[1]][1]==constants.BISHOP:
        return moves_of_bishop(i, j, board, color)
    
    if board[pos[0]][pos[1]][1]==constants.KING:
        return moves_of_king(i, j, board, color)
    
    if board[pos[0]][pos[1]][1]==constants.QUEEN:
        return moves_of_queen(i, j, board, color)
    
    if board[pos[0]][pos[1]][1]==constants.ROOK:
        return moves_of_rook(i, j, board, color)
    
    if board[pos[0]][pos[1]][1]==constants.HORSE:
        return moves_of_horse(i, j, board, color)
    
    return None


def moves_of_pawn(i, j, board, color):
    moves = []
    if color == constants.WHITE:
        direction = -1
    else:
        direction = 1 #  '+ 1'

    if inside_board(i+direction, j) and board[i+direction][j]==constants.EMPTY:
        moves += [(i+direction, j)]
    if inside_board(i+direction, j-1) and board[i+direction][j-1][0]==str(1-color):
        moves += [(i+direction, j-1)]
    if inside_board(i+direction, j+1) and board[i+direction][j+1][0]==str(1-color):
        moves += [(i+direction, j+1)]
    return moves

def moves_of_bishop(i, j, board, color):
    moves = []
    for vector_x, vector_y in [(-1,-1), (-1, 1), (1, -1), (1,1)]:
        stride = 1
        while True:
            if not inside_board(i + vector_x*stride, j + vector_y*stride):
                break
            if board[i + vector_x*stride][j + vector_y*stride]==constants.EMPTY or board[i + vector_x*stride][j + vector_y*stride][0]==str(1-color):
                moves += [(i + vector_x*stride, j + vector_y*stride)]
            else:
                break
            stride += 1    
    return moves

def moves_of_king(i, j, board, color):
    moves = []
    if inside_board(i-1, j-1) and not board[i-1][j-1][0]==str(color):
        moves += [(i-1, j-1)]
    if inside_board(i-1, j) and not board[i-1][j][0]==str(color):
        moves += [(i-1, j)]
    if inside_board(i-1, j+1) and not board[i-1][j+1][0]==str(color):
        moves += [(i-1, j+1)]
    if inside_board(i, j-1) and not board[i][j-1][0]==str(color):
        moves += [(i, j-1)]
    if inside_board(i, j+1) and not board[i][j+1][0]==str(color):
        moves += [(i, j+1)]
    if inside_board(i+1, j-1) and not board[i+1][j-1][0]==str(color):
        moves += [(i+1, j-1)]
    if inside_board(i+1, j) and not board[i-1][j][0]==str(color):
        moves += [(i+1, j)]
    if inside_board(i+1, j+1) and not board[i-1][j+1][0]==str(color):
        moves += [(i+1, j+1)]
    return moves
    
    

def moves_of_queen(i, j, board, color):
    moves = []
    for vector_x, vector_y in [(0,-1), (-1, -1), (-1,0), (-1,1), (0,1), (1, 1), (1,0), (1, -1)]:
        stride = 1
        while True:
            if not inside_board(i + vector_x*stride, j + vector_y*stride):
                break
            if board[i + vector_x*stride][j + vector_y*stride]==constants.EMPTY or board[i + vector_x*stride][j + vector_y*stride][0]==str(1-color):
                moves += [(i + vector_x*stride, j + vector_y*stride)]
            else:
                break
            stride += 1    
    return moves

def moves_of_rook(i, j, board, color):
    moves = []
    for vector_x, vector_y in [(0,-1), (-1,0), (0,1), (1,0)]:
        stride = 1
        while True:
            if not inside_board(i + vector_x*stride, j + vector_y*stride):
                break
            if board[i + vector_x*stride][j + vector_y*stride]==constants.EMPTY or board[i + vector_x*stride][j + vector_y*stride][0]==str(1-color):
                moves += [(i + vector_x*stride, j + vector_y*stride)]
            else:
                break
            stride += 1    
    return moves

def moves_of_horse(i, j, board, color):
    moves = []
    if inside_board(i-2, j-1) and not board[i-2][j-1][0]==str(color):
        moves += [(i-2, j-1)]

    if inside_board(i-2, j+1) and not board[i-2][j+1][0]==str(color):
        moves += [(i-2, j+1)]

    if inside_board(i-1, j-2) and not board[i-1][j-2][0]==str(color):
        moves += [(i-1, j-2)]

    if inside_board(i+1, j-2) and not board[i+1][j-2][0]==str(color):
        moves += [(i+1, j-2)]

    if inside_board(i-1, j+2) and not board[i-1][j+2][0]==str(color):
        moves += [(i-1, j+2)]

    if inside_board(i+1, j+2) and not board[i+1][j+2][0]==str(color):
        moves += [(i+1, j+2)]

    if inside_board(i+2, j-1) and not board[i+2][j-1][0]==str(color):
        moves += [(i+2, j-1)]

    if inside_board(i+2, j+1) and not board[i+2][j+1][0]==str(color):
        moves += [(i+2, j+1)]
        
    return moves



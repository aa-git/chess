import constants
import helper_functions
import possible_moves_lib
from copy import deepcopy
import sys

######################################
######################################
######################################
######## initialize content ##########
######################################
######################################
######################################

#chess_board = constants.CHESS_BOARD
chess_board = helper_functions.read_chess_board("chess.xlsx")


#config means a 'id', board arrangement', 'link to next boards/ids', 'is_check_mate_flag'
#[id, board config, [id1, id2, ...(pointer to next config) ]], is_check_mate_flag(true/false)
config_count = 0
config = []
config_store = []##is a sorted list, by ids
total_check_mates = 0

def pieces(board, color):
    result = []
    for i in range(constants.ROWS):
        for j in range(constants.COLUMNS):
            if board[i][j]!=constants.EMPTY and board[i][j][0]==str(color):
                result += [(i,j)]
    return result

def possible_moves(pos, board):
    return possible_moves_lib.possible_moves(pos, board)

def make_move(org_board, initial, final):
    board = deepcopy(org_board)
    board[final[0]][final[1]] = board[initial[0]][initial[1]]
    board[initial[0]][initial[1]]=constants.EMPTY
    return board

def already_config_achieved(board):
    i=0
    while i<len(config_store):
        if config_store[i][1]==board:
            return [True, config_store[i][0], config_store[i]]
        i += 1
    return [False, None, None]

def make_config(board, count):
    return [count, board, [], False]
    
def store_config(config):
    global config_store
    config_store += [config]

def threat_on_pos(board, pos):
    piece_val_at_pos = board[pos[0]][pos[1]]
    if piece_val_at_pos==constants.EMPTY:
        print("checking func: threat_on_pos(board, pos) for empty location - file: helper_function.py")
        sys.exit(1)
    opponent_color = 1-int(piece_val_at_pos[0])
    for piece_pos in pieces(board, opponent_color):
        for move in possible_moves(piece_pos, board):#move is a list of 2 tuple, (end-i, end-j)
            temp_board_config = make_move(board, piece_pos, move)
            if temp_board_config[pos[0]][pos[1]]!=piece_val_at_pos:
                return True
    return False

def compress(x):
    #compress config for storage purposes
    return x

def save_configs_to_disk():
    print("\nsaving configs to disk")
    file_ = open("configs_store.txt","w")
    for i in config_store:
        file_.write(str(compress(i))+"\n")
    file_.close()
    print("saved")

#this function should be iterative, not recursive
#while writing, think of c++ programming, then change code to python programming
# color = 0,1: 0 = black, 1 = white
def next_move_recursive_to_check_mate(color, config, recursion_depth):

    ''' 
        color(white/black) moves, gives next configuration 
        1 = white, 0 = black
        returns: True if this incoming config is a checkmate config, else false
    '''
    global config_count, total_check_mates
    check_mate = True
    if config_count>=total_configs_to_compute:
        return False

    if recursion_depth==0:
        return False

    if make_moves_and_show_on_keystroke:
        input()

    if config_count % display_after_iterations==0:
        helper_functions.show(config, config_count)

    if display_only_iterations_flag:
        print("\rconfig count = "+str(config_count)+"     , check mate count =   "+str(total_check_mates)+"         ",end='')


    king_in_threat = threat_on_pos(config[1], helper_functions.get_position(color, config[1], constants.KING))
    for piece_pos in pieces(config[1], color):
        for move in possible_moves(piece_pos, config[1]):#move is a list of 2 tuple, (end-i, end-j)
            temp_board_config = make_move(config[1], piece_pos, move)

            game_not_finished = not king_in_threat and not threat_on_pos(temp_board_config, helper_functions.get_position(color, temp_board_config, constants.KING))
            game_not_finished = game_not_finished or king_in_threat and not threat_on_pos(temp_board_config, helper_functions.get_position(color, temp_board_config, constants.KING))
            if game_not_finished:
                check_mate=False
                result = already_config_achieved(temp_board_config) #result[0] = true/false, result[1] = config number, result[2] = config for that config number at index [1]
                if result[0]:
                    config[2] += [result[1]]
                    #next_move_recursive_to_check_mate(1-color, result[2]) #commented to break cycle in graph
                else:
                    config_count+=1
                    config_made = make_config(temp_board_config, config_count) #make config list = [id, board, [ids,..]] 
                    #checkmate checking variable
                    config_made[3] = next_move_recursive_to_check_mate(1-color, config_made, recursion_depth-1)
                    if config_made[3]:
                        total_check_mates += 1
                    store_config(config_made)##put 'config_made' in' config_store'
                    config[2] += [config_made[0]]  
    return check_mate        

def clean_graph():
    ## cleans unnecessary chess boards, with no concrete result
    if not save_configs_to_disk_flag:
        print("Graph not stored to disk")
        sys.exit(1)


#########################################
#########################################
#########################################
######## initialization variables #######
#########################################
#########################################
#########################################
display_after_iterations = 1
make_moves_and_show_on_keystroke = False
save_configs_to_disk_flag = True
total_configs_to_compute = 1000000 # anythiing '< 0' here would imply exhaustive search
display_only_iterations_flag = True

#########################################
#########################################
#########################################
# ##########   start code ###############
#########################################
#########################################
#########################################
starting_color = constants.WHITE
initial_config = make_config(chess_board, config_count)
store_config(initial_config)
next_move_recursive_to_check_mate(starting_color, initial_config, 100)
if save_configs_to_disk_flag:
        save_configs_to_disk()
clean_graph()
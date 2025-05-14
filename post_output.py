import xlrd
import helper_functions


def format_column_1(data):#ids
    for i in range(len(data)):
        data[i][0] = (int)(data[i][0])
    return data

def format_column_2(data):#chess board
    for i in range(len(data)):
        board = data[i][1].split("|")
        print(board)
        for j in range(8):
            board[j] = board[j].split(",")
        data[i][1] = board
    return data

def format_column_3(data):
    for i in range(len(data)):
        #to remove '~', and separate in comma separated integers
        data[i][2] = data[i][2][1:].split(",")
        data[i][2] = map(int, data[i][2])
    return data

def format_column_4(data):
    for i in range(len(data)):
        if data[i][3]=='FALSE':
            data[i][0] = False
        else:
            data[i][0] = True
    return data


def read_data(file_name):
    workbook = xlrd.open_workbook(file_name)
    worksheet = workbook.sheet_by_index(0)
    data = [['' for i in range(COLUMNS)] for j in range(ROWS)]

    # data is sorted, as excel is sorted

    for i in range(ROWS):
        for j in range(COLUMNS):
            data[i][j] = worksheet.cell_value(i,j)

    return data

#################################################################################
#################################################################################
#################################################################################
#################################################################################
########################               START       ##############################
#################################################################################
#################################################################################
#################################################################################
#################################################################################

file_name = "output_in_excel.xlsx"
ROWS = 145484
COLUMNS = 4

data = read_data(file_name)
data = format_column_1(data)
data = format_column_2(data)
data = format_column_3(data)
data = format_column_4(data)

helper_functions.show([None, data[4][1] ,None, None], -1)

# will contains all games ending with 'id' given
# data[id] will give the output, dont need to do data[id-1]
games = []

def display_game(id):

    get_hierarchy()
    data[id]

def fun(id):
    pass

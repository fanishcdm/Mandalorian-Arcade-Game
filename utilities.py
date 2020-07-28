'''Utility Functions'''
import os

def superimpose(item, board):
    '''Function to place objects
    onto the map of the board
    '''
    board_matrix = board.get_matrix()
    item_matrix = item.get_matrix()
    ii = 0
    for i in range(item.y, item.y + item.height):
        jj = 0
        for j in range(item.x, item.x + item.width):
            board_matrix[i][j] = item_matrix[ii][jj]
            jj += 1
        ii += 1
    board.update_matrix(board_matrix)


def clear_sprite(item, board):
    '''Function to clear the object off the
    console screen
    '''
    board_matrix = board.get_matrix()

    for i in range(item.y, item.y + item.height):
        for j in range(item.x, item.x + item.width):
            board_matrix[i][j] = ' '
    board.update_matrix(board_matrix)

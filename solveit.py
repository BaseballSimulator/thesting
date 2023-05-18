import numpy as np
#make board

board_zero = np.zeros(shape=(9,9), dtype=int)

board_init = board_zero

#fred board

board_init[0,:] = [0,3,1,0,0,6,2,4,0]
board_init[1,:] = [6,2,4,3,0,8,0,0,7]
board_init[2,:] = [8,5,0,2,0,1,6,3,0]
board_init[3,:] = [1,4,0,0,0,3,8,0,0]
board_init[4,:] = [3,8,0,0,0,4,7,1,2]
board_init[5,:] = [7,9,0,0,0,5,0,0,0]
board_init[6,:] = [5,6,0,4,0,7,9,2,0]
board_init[7,:] = [2,1,3,6,0,9,0,0,0]
board_init[8,:] = [0,7,9,0,0,2,3,8,6]

print(board_init)


def roundup_near(index):
    roundup_float = np.ceil((index + 1) / 3) * 3 # add 
    roundup_int = int(roundup_float)

    return roundup_int


def check_unique(board, row, column):
    # Get distinct 
    row_values = np.unique(board[row,:])
    col_values = np.unique(board[:,column])
    
    # First define the sub cell that the row/column falls into
    # This will be a group of 3 in each axis
    row_end_pos = roundup_near(row)
    col_end_pos = roundup_near(column)
    
    #get distinct
    box_values = np.unique(board[row_end_pos-3:row_end_pos, 
                                 col_end_pos-3:col_end_pos])
    
    print(box_values)
    
    # Bring all into one list
    all_values = np.concatenate((row_values, col_values, box_values), axis=None)
    
    # Then take the unique values from all of them
    unique_values = np.unique(all_values)
    
    return unique_values

def fill_values(board, row, column):
    # We're only interested in values not yet filled
    if board[row,column] == 0:
      
        # Check unique numbers in row, column, and sub cell
        existing_values = check_unique(board, row, column)
        
        # Get numbers from 1-9 that don't appear in unique numbers list
        potential_values = [value for value in range(1,10) if value not in existing_values]
        
        # If there's only one potential solution, overwrite zero with that value
        if len(potential_values) == 1:
            board_play[row,column] = potential_values[0]
            print('Row: ', str(row + 1), '& Col: ', str(column + 1), ' overwritten with ', str(potential_values[0]))


board_play = board_init.copy()

# Restrict to max of 10 loops of the board
for i in range(10):
    
    # Loop through table columns & rows
    for row in range(9):
        for column in range(9):
            fill_values(board_play, row, column)
                
    print('\n Loop number ', str(i + 1), ' complete \n')
    
    # Checks array for number of non-filled values remaining
    zeroes_remaining = np.count_nonzero(board_play == 0)
    
    if zeroes_remaining == 0:
        print('Finished!')
        break
    else:
        print(' ', str(zeroes_remaining), ' zeroes left\n')

print(board_play)
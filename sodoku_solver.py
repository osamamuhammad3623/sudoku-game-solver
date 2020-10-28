def take_grid(grid):
    file = open("grid.txt", 'r')
    for line in file:
        row_list = line.split()
        num_list = []
        for n in row_list:
            num_list.append(int(n))
        grid.append(num_list)
    return grid

def print_grid(grid):
    file = open("grid_solution.txt", 'w')
    for row in grid:
        file.write(str(row))
        file.write("\n")

def get_empty_cell(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                return (row,col)
    return False
            
def check_if_valid(grid, cell_num, position):
    # checking if the cell_number exists in the same row before actually adding it
    for i in range(0,9):
        if grid[position[0]][i] == cell_num:
            return False
        
    # checkig if the cell_number exists in the same col
    for i in range(0,9):
        if grid[i][position[1]] == cell_num:
            return False
    
    # checking if the cell_number exists in the same subgrid
    group_row_index = int(position[0] / 3) * 3
    group_col_index = int(position[1] / 3) * 3
    for row in range(group_row_index,group_row_index+3):
        for col in range(group_col_index,group_col_index+3):
            if grid[row][col] == cell_num:
                return False
    return True

def complete_the_game(grid):
    if get_empty_cell(grid) == False:
        return True # we are done then!
    else:
        row, col = get_empty_cell(grid)
        
    for i in range(1,10):
        # we check if the number will be valid before adding it to the grid
        if check_if_valid(grid, i, (row,col)):
            # if it's valid, then we actually add it!
            grid[row][col] = i
            
            if complete_the_game(grid) == True:
                return True
            
            # if we can't finish the solution(complete_the_game(grid) isn't true), 
            #   then we Backtrack and reset the last empty cell to 0 and try another number
            grid[row][col] = 0
    return False

def empty_cells_number(grid):
    empty_cells = 0
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                empty_cells += 1
    return empty_cells

def check_final_board(grid):
    for i in range(9):
        row_set = set(grid[i])
        if len(row_set) != 9 or (0 in row_set):
            print("Row " + str(i) + " has duplicates or empty cells")
        else:
            print("Row " + str(i) + " is OK.")

#----------------------------------------------------------------
            
grid = []
take_grid(grid)
print(empty_cells_number(grid))
if complete_the_game(grid) == True:
    check_final_board(grid)
    print_grid(grid)
else:
    print("I can't find a solution :(")
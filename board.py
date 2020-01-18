from sudoku import Sudoentry, Sudosquare

class Board:
    def __init__(self):
        '''
        The highest level class that represents the board and all the operations associated with it.  
        Members:
            Board (list (Sudoentries)) - Format:
            0  1  2  3  4  5  6  7  8 
            9  10 11 12 13 14 15 16 17
            18 19 20 21 22 23 24 25 26
            27
            36
            45
            54
            63
            72 73 74 75 76 77 78 79 80
        '''
        self.board = [Sudoentry(x * 0, (x // 9) % 9, x % 9) for x in range(81)]
        self.update_board_pieces_from_board()

    #################################################
    ################# Main Function #################
    #################################################
    def solve(self):
        '''
        Solve the board by filling in until you need to guess, then guess, then repeat.
        Args:
            None
        Returns:
            Boolean - true if the board has been filled in completely and is valid, false otherwise
        Raises:
            None
        '''
        # Check if the board is valid, if so return true
        if self.is_complete_board():
            return True
        # If the board is invalid return false as we filled in something we shoudln't have
        elif not self.is_valid():
            return False

        # Do a loop of filling in until we have to guess, follow up with a guess, then recursively call itself
        self.solve_upto_guarenteed()

        guess = self.guess()

        result = self.solve()

        # If we get a complete and valid board back we are done, propagate up the stack
        if result == True:
            return True
        # Otherwise we put an invalid guess down and need to invalidate that guess for this level of the stack frame
        else:



        
    #######################################################
    ################## Helper Functions ###################
    #######################################################
    def is_complete_board(self):
        '''
        Determines if a board is filled in completely and is valid by checking the rules of sudoku
        Args:
            None
        Returns:
            Boolean - true if the board is valid, false otherwise
        Raises:
            None
        '''
        # Check if the board is valid
        if not self.is_valid_board():
            return False

        # Check if the baord is completely filled in
        for entry in self.board:
            if entry.value = 0:
                return False
            
        return True

    def is_valid_board(self):
        '''
        Determines if a board is valid or not by checking the rules of sudoku
        Args:
            None
        Returns:
            Boolean - true if the board is valid, false otherwise
        Raises:
            None
        '''
        added = set()
        for column in self.columns:
            added = set()
            for entry in column:
                if entry.value in added:
                    print("Invalid Board. Duplicate in column: ", self.columns.index(column))
                    return False
                added.add(entry.value)

        for row in self.rows:
            added = set()
            for entry in row:
                if entry.value in added:
                    print("Invalid Board. Duplicate in row: ", self.rows.index(row))
                    return False
                added.add(entry.value)

        for sudosquare in self.sudosquares:
            added = set()
            for entry in sudosquare.square:
                if entry.value in added:
                    print("Invalid Board. Duplicate in square: ", self.sudosquares.index(sudosquare))
                    return False
                added.add(entry.value)
        
        print("Valid Board")
        return True

    def copy_board_from(self, toCopy):
        '''
        Copies a list of ints to a board object by creating a Sudoentry object for every int.
        If an entry has a wrong type, it assigns the value 0 to the associated Sudoentry object.  
        Args:
            toCopy (list) - integer list of size 81
        Returns:
            None
        Raises:
            Length Error - Invalid Matrix to copy from
        '''
        INT_TYPE = type(1)
        #If the length is wrong, the raise an error and dont copy board
        if len(toCopy) != len(self.board):
            print("Invalid matrix to copy from")
            print("Requires matrix of length 61; given matrix of length ", len(toCopy))
        else:
            #Builds a Sudoentry object for each entry in the toCopy list
            for index in range(len(toCopy)):
                if type(toCopy[index]) != INT_TYPE:
                    self.board[index].value = 0
                else:
                    self.board[index].value = toCopy[index]
                    if toCopy[index] != 0:
                        self.board[index].poss_values = set([toCopy[index]])
                    else:
                        self.board[index].poss_values = set()
                    
    def clear_sets(self):
        for entry_index in range(len(self.board)):
            if self.board[entry_index].value == 0:
                self.board[entry_index].poss_values = set()

    ##################################################################
    ################### Data Structure Maintenance ###################
    ##################################################################
    def update_board_pieces_from_board(self):
        '''
        Updates all the squares, columns, and rows lists based on the current board. As well as updates all possible value sets in board
        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        #Fix possible value sets
        for entry in self.board:
            if entry.value != 0:
                entry.poss_values = set([entry.value])

        #Updates all the squares
        self.square_one = Sudosquare(self.board[0:3] + self.board[9:12] +  self.board[18:21], [0,1,2,9,10,11,18,19,20])
        self.square_two = Sudosquare(self.board[3:6] + self.board[12:15] + self.board[21:24], [3,4,5,12,13,14,21,22,23])
        self.square_three = Sudosquare(self.board[6:9] + self.board[15:18] + self.board[24:27], [6,7,8,15,16,17,24,25,26])
        self.square_four = Sudosquare(self.board[27:30] + self.board[36:39] + self.board[45:48], [27,28,29,36,37,38,45,46,47])
        self.square_five = Sudosquare(self.board[30:33] + self.board[39:42] + self.board[48:51], [30,31,32,39,40,41,48,49,50])
        self.square_six = Sudosquare(self.board[33:36] + self.board[42:45] + self.board[51:54], [33,34,35,42,43,44,51,52,53])
        self.square_seven = Sudosquare(self.board[54:57] + self.board[63:66] + self.board[72:75], [54,55,56,63,64,65,72,73,74])
        self.square_eight = Sudosquare(self.board[57:60] + self.board[66:69] + self.board[75:78], [57,58,59,66,67,68,75,76,77])
        self.square_nine = Sudosquare(self.board[60:63] + self.board[69:72] + self.board[78:], [60,61,62,69,70,71,78,79,80])
        #Assigns all the squares to the list
        self.sudosquares = [self.square_one, self.square_two, self.square_three, self.square_four, self.square_five, self.square_six, self.square_seven, self.square_eight, self.square_nine]
        
        #Updates all the rows
        self.row_one = self.board[:9]
        self.row_two = self.board[9:18]
        self.row_three = self.board[18:27]
        self.row_four = self.board[27:36]
        self.row_five = self.board[36:45]
        self.row_six = self.board[45:54]
        self.row_seven = self.board[54:63]
        self.row_eight = self.board[63:72]
        self.row_nine = self.board[72:]
        #Assigns all the rows to the list
        self.rows = [self.row_one, self.row_two, self.row_three, self.row_four, self.row_five, self.row_six, self.row_seven, self.row_eight, self.row_nine]
        
        #Updates all the columns
        self.column_one = self.board[::9]
        self.column_two = self.board[1::9]
        self.column_three = self.board[2::9]
        self.column_four = self.board[3::9]
        self.column_five = self.board[4::9]
        self.column_six = self.board[5::9]
        self.column_seven = self.board[6::9]
        self.column_eight = self.board[7::9]
        self.column_nine = self.board[8::9]
        #Assigns all the columns to the list
        self.columns = [self.column_one, self.column_two, self.column_three, self.column_four, self.column_five, self.column_six, self.column_seven, self.column_eight, self.column_nine]

    def fix_board(self):
        '''
        Determines if every entry in the table is a Sudoentry
        If an entry is any other type, a Sudoentry with value 0 is
        assigned.  
        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        INT_TYPE = type(1)
        SUDOENTRY_TYPE = type(Sudoentry(1, 1, 1))

        #Runs through every entry in the board and checks its type
        for index in range(len(self.board)):
            if type(self.board[index]) != SUDOENTRY_TYPE:
                if type(self.board[index]) == INT_TYPE:
                    self.board[index] = Sudoentry(self.board[index], (index // 9) % 9, index % 9)
                else:
                    self.board[index] = Sudoentry(0, (index // 9) % 9, index % 9)

        #Updates the various lists associated with the board object
        self.update_board_pieces_from_board()


    ####################################################
    ########### Basic Deterministic Guessing ###########
    ####################################################
    def solve_upto_guarenteed(self):
        '''
        Solves upto the point that a number is guarenteed to go into a position based on the current board
        Does not test out numbers using guess and check or other future methods. Uses the method of filling
        in each square with all the possible values it can have, if a Sudosentry's value is written to, then it
        starts over with updated the possible values member in each Sudoentry.  
        Args:
            None
        Raises:
            None
        Returns:
            None
        '''
        self.clear_sets()
        was_updated = False
        updated_during_filling = False
        #For each number in a range 1 - 9
        for number in range(1, 10):
            #for each 3x3 square within the board (each Sudosquare)
            for sq_index in range(len(self.sudosquares)):
                #Find all places the current number can be had at based on the current board
                #Update possible values member in each entry
                if self.fill_in_poss_value(sq_index, number):
                    updated_during_filling = True

        #after going through all values and filling in all poss_value members for each Sudoentry, determine if anything can be written
        was_updated = self.write_if_possible()
        #If a spot was written to, then restart the filling process over again
        if was_updated or updated_during_filling:
            #Recursively call the function again. On return the calling function terminates
            self.solve_upto_guarenteed()

    def guess(self, possible_values=None):
        '''
        Fills in a spot randomly with a number that is valid.
        Args:
            None
        Raises:
            None
        Returns:
            None
        '''
        # If a possible values list was provided, then use that
        if possible_values != None:
            pass
        # Otherwise use the built in one
        else:
            pass

        
        #for each square in a board
        for square_index in range(len(self.sudosquares)):
            #Find the next square that supports a valid entry
            for entry in self.sudosquares[square_index].square:
                #If a square has a possible value, set it to that value
                for pos in entry.poss_values:
                    if pos == entry.value:
                        continue
                    print(entry.value)
                    entry.value = pos
                    self.update_board_pieces_from_board()
                    return (square_index, entry.value)

        return (0, 0)

    def fill_in_poss_value(self, sq_index, value):
        '''
        Fills in the possible values list for all Sudoentries in the Sudosquare (9 entry list of Sudoentries)
        with the value if it can go there. If the value is already present in 1 of the 9 entries then the method quits
        Args:
            sq_index (int) - index of the Sudosquare in the self.squares list
            value (int) - value to be added to each square
        Returns:
            Boolean - True if a value was written to the board (sudoentry value member was updated)
                      False if a value was not written
        Raises:
            None
        '''
        sudosquare = self.sudosquares[sq_index]
        added = list()
        ONLY_ELEMENT = 0
        #check if the entry is already in the square, if it is then we skip it
        for entry_index in range(9):
            if value == sudosquare.square[entry_index].value:
                return False

        #For each Sudoentry in the Sudosquare
        for entry_index in range(9):
            #if the entry already is filled in (the value is non 0), then skip over it as we already know the value
            if sudosquare.square[entry_index].value != 0:
                continue
            #else determine if the number can go there and if so, add that number to the possible values list
            else:
                if self.is_valid_value(value, sq_index, entry_index):
                    added.append(entry_index)
                    self.sudosquares[sq_index].square[entry_index].poss_values.add(value)

        #if the count is 1 then only 1 got filled in and that means a value can only go in 1 spot in the square, meaning it is valid
        if len(added) == 1:
            board_index = self.sudosquares[sq_index].indices[added[ONLY_ELEMENT]]
            self.board[board_index].value = value
            self.update_board_pieces_from_board()
            return True
        else:
            return False

    def is_valid_value(self, value, sq_index, entry_index):
        '''
        Determines if a value is able to be added to the possible value list of an entry
        by seeing if it is already in the row or column
        Args:
            value (int) - the value in question on whether or not it should be added
            sq_index (int) - index of the square in the squares list that contains the entry we are checking
            entry_index (int) - index of the entry within the square that we are investigating
        Returns:
            None
        Raises:
            None
        '''
        entry = self.sudosquares[sq_index].square[entry_index]
        #Check if the value is in the same column already
        for sudoentry in self.columns[entry.column]:
            if value == sudoentry.value:
                return False
        #Check if the value is in the same row already
        for sudoentry in self.rows[entry.row]:
            if value == sudoentry.value:
                return False
        #Check if the value is in the same square already
        for sudoentry in self.sudosquares[sq_index].square:
            if value == sudoentry.value:
                return False
        return True

    def write_if_possible(self):
        '''
        Runs through every Sudoentry on the board and determines if it has no value 
        and that its possible values list has length 1
        Args:
            None
        Returns:
            Boolean - True if an entry was written to
                      False if no entry was written to
        Raises:
            None
        '''
        beenUpdated = False
        #Runs through all entries in the list
        for entry_index in range(len(self.board)):
            #if there is only 1 possible value for that entry and the entry does not have a value in it aleady, then assign it to it
            if self.board[entry_index].value == 0 and len(self.board[entry_index].poss_values) == 1:
                value_to_add = self.board[entry_index].poss_values.pop()
                self.board[entry_index].value = value_to_add
                self.board[entry_index].poss_values.add(value_to_add)
                beenUpdated = True
        self.update_board_pieces_from_board()
        return beenUpdated

    ######################################################
    #############    Recursive NP Solving    #############
    ######################################################

    


    ###################################################
    ############    Special NP Solving    #############
    ###################################################
    def correct(self, solved_puzzle):
        '''
        Changes around the solved board so that the numbers in the known cells (in the solved board) 
        align with the board we are currently trying to solve
        Args:
            solved_puzzle(list(int)) - The solved puzzle we will morph into our solution
        Returns:
            None
        Raises:
            None
        '''
        #Morph the solved solution to what we currently have
        solved_puzzle = self.morph_solved_init(solved_puzzle)

        #make sure the number line up with the possible values
        solved_puzzle = self.morph_solved_poss_values(solved_puzzle)

        #Find errors in rows and swap them when another row has a corresponding error. Do not rearrange boxes
        solved_puzzle = self.morph_solved_fix_rows(solved_puzzle)

        #Find errors in columns and swap them when another column has a corresponding error
        #solved_puzzle = self.morph_solved_fix_columns(solved_puzzle)

        #Print details to user
        print("Morphed:")
        print_matrix_as_board(solved_puzzle)


    def morph_solved_init(self, solved_puzzle):
        #For each 3x3 square in the board
        for sudosquare in self.sudosquares:
            #for each entry in the square
            for entry in sudosquare.square:
                #Get the position in the 1d array
                position = entry.row * 9 + entry.column
                
                #If the position in the solved array and the puzzle are different, then find the corresponding position to swap with it
                if solved_puzzle[position] != entry.value and entry.value != 0:
                    #Find the piece that we need to swap with
                    for swap_with in sudosquare.square:
                        #compute the position in the 1d array
                        swap_position = swap_with.row * 9 + swap_with.column

                        #Once we find the number thats supposed to go there, swap them
                        if solved_puzzle[swap_position] == entry.value:
                            #Swap the values
                            temp = solved_puzzle[swap_position]
                            solved_puzzle[swap_position] = solved_puzzle[position]
                            solved_puzzle[position] = temp
                            break

        return solved_puzzle
    
    def morph_solved_poss_values(self, solved_puzzle):
        #For each 3x3 square in the board
        for sudosquare in self.sudosquares:
            #for each entry in the square
            for entry in sudosquare.square:
                #Get the position in the 1d array
                position = entry.row * 9 + entry.column
                
                #If the position in the solved array is not in the poss_values set for that positiont
                #then find the corresponding position to swap with it
                if solved_puzzle[position] not in entry.poss_values and entry.value == 0:
                    #Find the piece that we need to swap with
                    for swap_with in sudosquare.square:
                        #compute the position in the 1d array
                        swap_position = swap_with.row * 9 + swap_with.column

                        #Once we find the number thats supposed to go there, swap them
                        if solved_puzzle[position] in swap_with.poss_values and solved_puzzle[swap_position] in entry.poss_values:
                            #Swap the values
                            temp = solved_puzzle[swap_position]
                            solved_puzzle[swap_position] = solved_puzzle[position]
                            solved_puzzle[position] = temp
                            break

        return solved_puzzle

    def morph_solved_fix_rows(self, solved_puzzle):
        #For each row on the board find what values are missing by marking off values once theyve been seen
        missing = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for y in range(9)]

        #For each row on the board find what values are duplicated by appending the row to the list then removing any duplicates
        #This list contains all the duplicates, so to solve the board overtime this list would empty. Can contain duplicates
        mult_values = [[] for x in range(9)]

        solved_rows = [solved_puzzle[0:9], solved_puzzle[9:18], solved_puzzle[18:27], solved_puzzle[27:36], solved_puzzle[36:45],
        solved_puzzle[45:54], solved_puzzle[54:63], solved_puzzle[63:72], solved_puzzle[72:81]]

        #Keep track of each row
        row_index = 0

        #For each row on the board
        for row in solved_rows:
            #For each entry in the row determine if its a duplicate
            for entry in row:
                try:
                    #If the entry is in the set still, then this is the first time weve seen it
                    missing[row_index].remove(entry)
                except: 
                    #Else the entry is not in the set and this is not the first time weve seen it, therefore its a duplicate
                    mult_values[row_index].append(entry)

            #Move to the next row
            row_index += 1

        #Sort each mult values array
        for row in mult_values:
            row.sort()

        #----------------PRINT------------------
        row_index = 0
        for row in missing:

            print("Missing in row", row_index + 1, ": ", end="")
            for entry in row:
                print(entry, " ", end="")

            print()
            row_index += 1
        print()

        row_index = 0
        for row in mult_values:
            print("Duplicate in row", row_index + 1, ": ", end="")
            for entry in row:
                print(entry, " ", end="")
            
            print()
            row_index += 1

        print()
        #------------------END_PRINT-------------------

        
        #For each row in the mult value array
        for mult_row_index in range(len(mult_values)):
            #For each duplicate entry in the row
            for mult_entry in mult_values[mult_row_index]:
                #Go through the solved board and find the first instance of the duplicate variable
                for mult_entry_index in range(len(solved_rows[mult_row_index])):
                    #Once weve found the row_entry in the solved_board and the corresponding entry isnt a locked value
                    if solved_rows[mult_row_index][mult_entry_index] == mult_entry and self.rows[mult_row_index][mult_entry_index].value == 0:
                        #Get the row group that the duplicate element is in and get the square that it is in
                        row_group_index = mult_row_index % 3
                        square_index = mult_row_index % 3 + mult_entry_index // 3
                        print(mult_row_index, mult_entry_index, mult_entry)
                        print(row_group_index, square_index)

                        #Find the entry in the missing list, to know which row the duplicate should be swapped to
                        for miss_row_index in range(row_group_index, row_group_index + 3):
                            #If we find a valid swap then swap and move onto the next value
                            if mult_entry in missing[miss_row_index] and missing[miss_row_index].index(mult_entry) :
                                #swap the values
                                pass
                            #tell the for loop one level up that we want to move onto the next value
                            #If we dont find a valid swap then move onto the next instance of the duplicate
                            else:
                                pass

                        break
        '''

        diff = list()

        #Go by groups of 3 rows and make sure that the groups of 3 have the same sub groups 
        #Sub groups do not have to be in the same order
        for row_group_last_index in range(3, 10, 3):
            #Used for indexing each row group
            row_group_base_index = row_group_last_index - 3
            row_group_diff = list()

            #Check to make sure each sub group is in the other array's row group
            for row_index in range(row_group_base_index, row_group_last_index):
                #if the row is not in the others row group, then copy it to the diff list of arrays
                if mult_values[row_index] not in missing[row_group_base_index:row_group_last_index]:
                    row_group_diff.append(row_index)

            #Keep track of the differences in rows
            diff.append(row_group_diff)

        
        #for each row group, swap values in the subgroups, till the subgroups are the same
        for row_group in diff:
            #For each row within the row group
            for row_index in row_group:
                #For each entry in that row in the mult values array
                for entry_index in range(len(mult_values[row_index])):
                    #cycle through the other rows and swap the value
                    for other_row_index in row_group:
                        #If its the same row, dont compare
                        if other_row_index == row_index:
                            continue
                        #Else, test by swaping with all other values in the row
                        else:
                            for other_entry_index in range(len(mult_values[other_row_index])):
                                #Swap the values
                                temp = mult_values[row_index][entry_index]
                                mult_values[row_index][entry_index] = mult_values[other_row_index][other_entry_index] 
                                mult_values[other_row_index][other_entry_index]  = temp

                                #test to see if the swap improved anything
        '''

        return solved_puzzle


    def morph_solved_fix_columns(self, solved_puzzle):
        #For each row on the board find what values are missing by marking off values once theyve been seen
        missing = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for y in range(9)]

        #For each row on the board find what values are duplicated by appending the row to the list then removing any duplicates
        #This list contains all the duplicates, so to solve the board overtime this list would empty. Can contain duplicates
        mult_values = [[] for x in range(9)]

        solved_columns = [solved_puzzle[::9], solved_puzzle[1::9], solved_puzzle[2::9], solved_puzzle[3::9], 
        solved_puzzle[4::9], solved_puzzle[5::9], solved_puzzle[6::9], solved_puzzle[7::9], solved_puzzle[8::9]]

        #Keep track of which column we are in
        col_index = 0

        #For each row on the board
        for col in solved_columns:
            #For each entry in the row determine if its a duplicate
            for entry in col:
                try:
                    #If the entry is in the set still, then this is the first time weve seen it
                    missing[col_index].remove(entry)
                except: 
                    #Else the entry is not in the set and this is not the first time weve seen it, therefore its a duplicate
                    mult_values[col_index].append(entry)

            #Move to the next row
            col_index += 1


        col_index = 0
        for col in missing:
            print("Missing in column", col_index + 1, ": ", end="")
            for entry in col:
                print(entry, " ", end="")

            print()
            col_index += 1

        print()

        col_index = 0
        for col in mult_values:
            print("Duplicate in column", col_index + 1, ": ", end="")
            for entry in col:
                print(entry, " ", end="")

            print()
            col_index += 1

        print()

        return solved_puzzle


    #####################################
    #########     PRINTING     ##########
    #####################################
    def print_board(self):
        '''
        Prints each entry depending on if it has a value or not
        Prints it in the standard format of a sudoku board
        Args:
            None
        Raises:
            None
        Returns:
            None
        '''
        count = 1
        self.fix_board()

        for entry in self.board:
            if entry.value == 0:
                print("_", " ", end="")  
            else:  
                print(entry.value, " ", end="")
            if count % 3 == 0:
                print("| ", end="")
            if count % 9 == 0:
                print()
            if count % 27 == 0:
                print("-------------------------------|")
            count += 1

    def print_board_detailed(self):
        '''
        Formats and prints the contents of the board 
        Args:
            None
        Raises:
            None
        Returns:
            None
        '''
        count = 1
        self.fix_board()

        # For every entry on the board print its possible values or its actual value if it has one
        for entry in self.board:
            # No value has been chosen for this square so print all possible values
            if entry.value == 0:
                # Print 9 regardless of how many numbers are actually possible for formatting reasons
                print("(", end="")
                for value in range(1,10):
                    if value in entry.poss_values:
                        print(value, "", end="")
                    else:
                        print("_ ", end="")
                print(")", end="")

            # Print the value that belongs and fill the rest with spaces
            else:  
                # Print 9 spaces for formatting reasons. Use brackets to indicate that a value has been chosen for this position
                print("[", end="")
                for i in range(1,10):
                    if i == entry.value:
                        print(i, "", end="")
                    else:
                        print("_ ", end="")
                print("]", end="")

            # Used for making new columns
            if count % 3 == 0:
                print("\t", end="")
            # Used for making new rows
            if count % 9 == 0:
                print()
            # Used for printing a new line after 3 rows to indicate a box (9 spaces 3x3)
            if count % 27 == 0:
                print("")
            count += 1

def print_matrix_as_board(puzzle):
    '''
    Takes in a matrix and prints it as a sudoku board, properly formatted
    Args:
        puzzle - list(ints)
    Raises:
        None
    Returns:
        None
    '''
    count = 1
    for entry in puzzle:
        if entry == 0:
            print("_", " ", end="")  
        else:  
            print(entry, " ", end="")
        if count % 3 == 0:
            print("| ", end="")
        if count % 9 == 0:
            print()
        if count % 27 == 0:
            print("-------------------------------|")
        count += 1
    print()
            

HARD_PUZZLE = [
0,7,0,0,0,0,0,0,9,
3,9,0,0,0,1,0,6,0,
1,0,0,0,0,0,0,0,0,
0,3,0,6,0,8,9,0,7,
0,0,0,5,0,7,0,0,0,
7,0,6,9,0,2,0,8,0,
0,0,0,0,0,0,0,0,6,
0,5,0,8,0,0,0,2,3,
8,0,0,0,0,0,0,4,0]

MEDIUM_PUZZLE = [
5,6,0,0,0,0,9,0,4,
0,0,0,0,5,0,6,7,0,
0,1,4,0,0,0,0,2,5,
9,0,0,1,0,0,0,0,0,
2,4,0,3,0,9,0,8,7,
0,0,0,0,0,7,0,0,9,
7,9,0,0,0,0,5,6,0,
0,3,6,0,2,0,0,0,0,
1,0,8,0,0,0,0,4,2
]

EASY_PUZZLE = [
0,0,6,0,7,0,0,0,2,
0,0,1,0,3,0,8,5,4,
5,3,0,0,4,0,6,0,0,
0,0,0,0,8,3,7,0,0,
0,5,0,0,9,0,0,1,0,
0,0,9,1,5,0,0,0,0,
0,0,4,0,1,0,0,2,6,
8,2,7,0,6,0,9,0,0,
6,0,0,0,2,0,3,0,0
]

SOLVED_PUZZLE = [
9, 4, 6, 5 ,7, 8, 1, 3, 2,
2, 7, 1, 6, 3, 9, 8, 5, 4,
5, 3, 8, 2, 4, 1, 6, 7, 9,
1, 6, 2, 4, 8, 3, 7, 9, 5,
4, 5, 3, 7, 9, 6, 2, 1, 8,
7, 8, 9, 1, 5, 2, 4, 6, 3,
3, 9, 4, 8, 1, 7, 5, 2, 6,
8, 2, 7, 3, 6, 5, 9, 4, 1,
6, 1, 5, 9, 2, 4, 3, 8, 7
]

TEST_PUZZLE = [
9, 4, 6, 5 ,7, 8, 1, 3, 2,
2, 7, 1, 6, 3, 9, 8, 5, 4,
5, 3, 8, 2, 4, 1, 6, 7, 9,
1, 6, 2, 4, 8, 3, 7, 9, 5,
4, 5, 3, 7, 9, 6, 2, 1, 8,
7, 8, 9, 1, 5, 2, 4, 6, 3,
3, 9, 4, 8, 1, 7, 5, 2, 6,
8, 2, 7, 3, 6, 5, 9, 4, 1,
6, 1, 5, 9, 2, 4, 3, 8, 7
]

curr_board = Board()
prevBoard = curr_board

curr_board.copy_board_from(HARD_PUZZLE)

print("Initial Board")
curr_board.print_board()

#Solve until we have to guess
print("\nSolving")
curr_board.solve()

print("\nSolved Board")
curr_board.print_board()
curr_board.print_board_detailed()

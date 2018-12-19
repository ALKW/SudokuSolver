class Sudoentry:
    def __init__(self, value, row, column):
        '''
        Each square on the board is one of these objects.  
        Members:
            poss_values (set) - All the possible values that could fill the square. 
            If there is one value then that value fills the square and the list becomes empty
            value (int) - the actual value in the square
            row (int) - value of the row the entry is in
            column (int) - value of the column the entry is in
        '''
        self.poss_values = set([1,2,3,4,5,6,7,8,9])
        self.value = value
        self.row = row
        self.column = column

    def set_value(self, value):
        '''
        Sets the value member of the object.  
        Args:
            value (int) - value to be set
        Returns:
            None
        Raises:
            TypeError - If a value other than an int is put in, it returns invalid and retains the previous entry
        '''
        INT_TYPE = type(1)

        if type(value) == INT_TYPE:
            self.value = value
        else:
            raise TypeError("Invalid Type")

    def print(self):
        '''
        Prints out the contents of the object.  
        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
        print("Value: ", self.value)
        print("Possible values: ", self.poss_values)
        print("Row: ", self.row)
        print("Column: ", self.column)

class Sudosquare:
    def __init__(self, listToCopy, indices):
        '''
        Defines a square on the board and contains a list of the 9 sudoentries within the square.  
        Members:
            square (list - (Sudoentries)) - contains the Sudoentry objects 
            indices (list - (int)) - indices of each entry relative to the board
        '''
        self.square = listToCopy
        self.indices = indices

    def check_valid(self):
        '''
        Checks if the square has a unique set of elements; no duplicates.  
        Args:
            None
        Returns:
            Boolean - True if there are no duplicates
                      False if there are duplicates
        Raises:
            None
        '''
        seen = set()
        for entry in self.square:
            if entry.value in seen:
                return False
            else:
                seen.add(entry.value)

    def print(self): 
        '''
        Formats and prints the contents of the Sudosquare object.  
        Args:
            None
        Raises:
            None
        Returns:
            None
        '''
        #prints the first row
        for entry in self.square[:3]:
            if entry.value < 10:
                print(entry.value, "  ", end="")
            else:
                print(entry.value, " ", end="")
        print()

        #prints the second row
        for entry in self.square[3:6]:
            if entry.value < 10:
                print(entry.value, "  ", end="")
            else:
                print(entry.value, " ", end="")
        print()

        #prints the third row
        for entry in self.square[6:]:
            if entry.value < 10:
                print(entry.value, "  ", end="")
            else:
                print(entry.value, " ", end="")
        print("\n")

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
        
    def update_board_pieces_from_board(self):
        '''
        Updates all the squares, columns, and rows lists based on the current board.  
        Args:
            None
        Returns:
            None
        Raises:
            None
        '''
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

    def validate_board(self):
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

    def clear_sets(self):
        for entry_index in range(len(self.board)):
            if len(self.board[entry_index].poss_values) != 1:
                self.board[entry_index].poss_values = set()

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
                if self.is_valid(value, sq_index, entry_index):
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

    def is_valid(self, value, sq_index, entry_index):
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

    def print_board(self):
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
        self.validate_board()

        for entry in self.board:
            print(entry.value, " ", end="")
            if count % 3 == 0:
                print("| ", end="")
            if count % 9 == 0:
                print()
            if count % 27 == 0:
                print("-------------------------------|")
            count += 1
            

HARD_PUZZLE = [
0,0,0,3,0,0,0,4,0,
8,0,0,0,0,1,0,0,7,
2,6,3,0,0,0,0,0,8,
0,0,0,0,1,0,4,6,0,
0,0,0,9,0,3,0,0,0,
0,2,5,0,6,0,0,0,0,
7,0,0,0,0,0,1,3,2,
5,0,0,8,0,0,0,0,6,
0,3,0,0,0,7,0,0,0]

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

test = Board()
test.copy_board_from(MEDIUM_PUZZLE)

test.print_board()

print("Solving Guarenteed Positions\n")

test.solve_upto_guarenteed()

test.print_board()

print("Solved As Much As Possible")





class Sudoentry:
    def __init__(self, value, row, column):
        self.poss_values = set([1,2,3,4,5,6,7,8,9])
        self.value = value
        self.row = row
        self.column = column

    def set_value(self, value):
        self.value = value

    def print(self):
        print("Value: ", self.value)
        print("Possible values: ", self.poss_values)
        print("Row: ", self.row)
        print("Column: ", self.column)

class Sudosquare:
    def __init__(self, list):
        self.square = list

    def check_valid(self):
        seen = set()
        for entry in self.square:
            if entry.value in seen:
                return False
            else:
                seen.add(entry.value)

    def print(self): 
        for entry in self.square[:3]:
            if entry.value < 10:
                print(entry.value, "  ", end="")
            else:
                print(entry.value, " ", end="")
        print()
        for entry in self.square[3:6]:
            if entry.value < 10:
                print(entry.value, "  ", end="")
            else:
                print(entry.value, " ", end="")
        print()
        for entry in self.square[6:]:
            if entry.value < 10:
                print(entry.value, "  ", end="")
            else:
                print(entry.value, " ", end="")
        print("\n")

class Board:
    def __init__(self):
        '''
        Board:
        1  2  3  4  5  6  7  8  9 
        10 11 12 13 14 15 16 17 18
        19 20 21 22 23 24 25 26 27
        28
        37
        46
        55
        64
        73 74 75 76 77 78 79 80 81
        '''
        self.board = [Sudoentry(x * 0, (x // 9) % 9, x % 9) for x in range(81)]
        self.build_board_pieces()
        
    def build_board_pieces(self):
        self.square_one = Sudosquare(self.board[0:3] + self.board[9:12] +  self.board[18:21])
        self.square_two = Sudosquare(self.board[3:6] + self.board[12:15] + self.board[21:24])
        self.square_three = Sudosquare(self.board[6:9] + self.board[15:18] + self.board[24:27])
        self.square_four = Sudosquare(self.board[27:30] + self.board[36:39] + self.board[45:48])
        self.square_five = Sudosquare(self.board[30:33] + self.board[39:42] + self.board[48:51])
        self.square_six = Sudosquare(self.board[33:36] + self.board[42:45] + self.board[51:54])
        self.square_seven = Sudosquare(self.board[54:57] + self.board[63:66] + self.board[72:75])
        self.square_eight = Sudosquare(self.board[57:60] + self.board[66:69] + self.board[75:78])
        self.square_nine = Sudosquare(self.board[60:63] + self.board[69:72] + self.board[78:])

        self.sudosquares = [self.square_one, self.square_two, self.square_three, self.square_four, self.square_five, self.square_six, self.square_seven, self.square_eight, self.square_nine]

        self.row_one = self.board[:9]
        self.row_two = self.board[9:18]
        self.row_three = self.board[18:27]
        self.row_four = self.board[27:36]
        self.row_five = self.board[36:45]
        self.row_six = self.board[45:54]
        self.row_seven = self.board[54:63]
        self.row_eight = self.board[63:72]
        self.row_nine = self.board[72:]

        self.rows = [self.row_one, self.row_two, self.row_three, self.row_four, self.row_five, self.row_six, self.row_seven, self.row_eight, self.row_eight]

        self.column_one = self.board[::9]
        self.column_two = self.board[1::9]
        self.column_three = self.board[2::9]
        self.column_four = self.board[3::9]
        self.column_five = self.board[4::9]
        self.column_six = self.board[5::9]
        self.column_seven = self.board[6::9]
        self.column_eight = self.board[7::9]
        self.column_nine = self.board[8::9]

        self.columns = [self.column_one, self.column_two, self.column_three, self.column_four, self.column_five, self.column_six, self.column_seven, self.column_eight, self.column_nine]

    def update_board(self):
        INT_TYPE = type(1)
        SUDOENTRY_TYPE = type(Sudoentry(1, 1, 1))

        for index in range(len(self.board)):
            if type(self.board[index]) != SUDOENTRY_TYPE:
                if type(self.board[index]) == INT_TYPE:
                    self.board[index] = Sudoentry(self.board[index], (index // 9) % 9, index % 9)
                else:
                    self.board[index] = Sudoentry(0, (index // 9) % 9, index % 9)

        self.build_board_pieces()

    def copy_board_from(self, toCopy):
        if len(toCopy) != len(self.board):
            print("Invalid matrix to copy from")
            print("Requires matrix of length 61; given matrix of length ", len(toCopy))
            return self
        else:
            self.update_board()
            for index in range(len(toCopy)):
                self.board[index].value = toCopy[index]
                if toCopy[index] != 0:
                    self.board[index].poss_values = set()

    def solve_upto_guarenteed(self):
        is_updated = False
        #For each number in a range 1 - 9
        for number in range(9):
            #for each 3x3 sqaure within the board
            for sq_index in range(len(self.sudosquares)):
                #Find all places the current number can be had at based on the current board
                #Update possible values member in each entry
                self.fill_in_poss_value(sq_index, number)
 
        #If a spot was written to, then restart the filling process over again
        is_updated = self.write_if_possible()
        if is_updated:
            self.solve_upto_guarenteed()

    def fill_in_poss_value(self, sq_index, value):
        sudosquare = self.sudosquares[sq_index]
        for entry_index in range(9):
            if sudosquare.square[entry_index].value != 0:
                continue
            else:
                if self.is_valid(value, sq_index, entry_index):
                    sudosquare.square[entry_index].poss_values.add(value)

    def is_valid(self, value, sq_index, entry_index):
        entry = self.sudosquares[sq_index].square[entry_index]
        #Check if the value is in the same column already
        if value in self.columns[entry.column]:
            return False
        #Check if the value is in the same row already
        if value in self.rows[entry.row]:
            return False
        return True

    def write_if_possible(self):
        beenUpdated = False
        for entry_index in range(len(self.board)):
            if self.board[entry_index].value == 0 and len(self.board[entry_index].poss_values) == 1:
                self.board[entry_index].value = self.board[entry_index].poss_values.pop()
                beenUpdated = True
        self.build_board_pieces()
        return beenUpdated

    def print_board(self):
        count = 1
        self.update_board()

        for entry in self.board:
            print(entry.value, " ", end="")
            if count % 3 == 0:
                print("| ", end="")
            if count % 9 == 0:
                print()
            if count % 27 == 0:
                print("-------------------------------|")
            count += 1
                

    def print_board_squares(self, toPrint=[0,1,2,3,4,5,6,7,8]):
        for index in toPrint:
            print("Square ", index + 1, ": ")
            self.sudosquares[index].print()
            

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
test.copy_board_from(EASY_PUZZLE)

test.print_board()

print("Solving\n\n")
test.solve_upto_guarenteed()

test.print_board()




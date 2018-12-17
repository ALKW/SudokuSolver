class Sudoentry:
    def __init__(self, value):
        self.poss_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.value = value

    def set_value(self, value):
        self.value = value

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
        self.board = [Sudoentry(x * 0) for x in range(81)]

        self.square_one = Sudosquare(self.board[0:3] + self.board[9:12] +  self.board[18:21])
        self.square_two = Sudosquare(self.board[3:6] + self.board[12:15] + self.board[21:24])
        self.square_three = Sudosquare(self.board[6:9] + self.board[15:18] + self.board[24:27])

        self.square_four = Sudosquare(self.board[27:30] + self.board[36:39] + self.board[45:48])
        self.square_five = Sudosquare(self.board[30:33] + self.board[39:42] + self.board[48:51])
        self.square_six = Sudosquare(self.board[33:36] + self.board[42:45] + self.board[51:54])

        self.square_seven = Sudosquare(self.board[54:57] + self.board[63:66] + self.board[72:75])
        self.square_eight = Sudosquare(self.board[57:60] + self.board[66:69] + self.board[75:78])
        self.square_nine = Sudosquare(self.board[60:63] + self.board[69:72] + self.board[78:])

        self.squares = [self.square_one, self.square_two, self.square_three, self.square_four, self.square_five, self.square_six, self.square_seven, self.square_eight, self.square_nine]

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
        SUDOENTRY_TYPE = type(Sudoentry(1))

        for index in range(len(self.board)):
            if type(self.board[index]) != SUDOENTRY_TYPE:
                if type(self.board[index]) == INT_TYPE:
                    self.board[index] = Sudoentry(self.board[index])
                else:
                    self.board[index] = Sudoentry(0)

    def print_board(self):
        count = 0

        self.update_board()

        for entry in self.board:
            if entry.value < 10:
                print(entry.value, "  ", end="")
                count += 1
            else:
                print(entry.value, " ", end="")
                count += 1
            if count == 9:
                print("\n")
                count = 0
                

    def print_board_squares(self, toPrint=[0,1,2,3,4,5,6,7,8]):
        self.update_board()

        for index in toPrint:
            print("Square ", index + 1, ": ")
            self.squares[index].print()
            
        

test = Board()
test.board[0] = 1
test.print_board()
test.print_board_squares()


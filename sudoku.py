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
            print(entry.poss_values, "  ", end="")
        print()

        #prints the second row
        for entry in self.square[3:6]:
            print(entry.poss_values, "  ", end="")
        print()

        #prints the third row
        for entry in self.square[6:]:
            print(entry.poss_values, "  ", end="")
        print("\n")
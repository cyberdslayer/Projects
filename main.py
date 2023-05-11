

class ChessBoard:
    # Construtor for 2D array
    def __init__(self):
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]
    # Defining display 
    def display_board(self):
        for row in self.board:
            print(row)

    # Defining the move function for every 
    def move(self, start, end):
        start_x, start_y = start
        end_x, end_y = end
        piece = self.board[start_x][start_y]
        if not self.is_valid_move(piece, start, end):
            return False

        self.board[start_x][start_y] = " "
        self.board[end_x][end_y] = piece
        return True

    def is_valid_move(self, piece, start, end):
        # checking if the move is within the bound of the board
        if end[0] < 0 or end[0] > 7 or end[1] <0 or end[1] > 7 :
            return False
    #checking if start and end position are same
        if start == end :
            return False

        #check if the piece can move to the end position 
        if piece == "P":
            #pawn movement rules
                

        
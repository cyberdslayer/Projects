

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

            #Determining the direction of the pawn based on its color
            if piece.isupper():
                direction = -1  #white pawn move up the board 
            else:
                direction = 1 #black pawn move down the board
            

            #checking if the pawn is moving one or two squares forward
            if start[0] == 6 and end[0] == start[0] +2 * direction and end[1] == start[1]:
                #check if there are any pieces in the way
                if self.board[start[0] + direction][start[1]] == " " and self.board[end[0] [end[1]]] == " " :
                    return True

                elif end[0] == start[0] + direction and end[1] == start[1]:

                    #checking if the pawn is moving one square
                    if self.board[end[0]][end[1]] == " ":
                        return True

                elif abs(end[1] - start[1]) == 1 and end[0] == start[0] +direction:

                    #check if the pawn is capturing diagonally
                    if self.board[end[0]][end[1]] != " " and self.board[end[0][end[1]]].isupper() != piece.isupper():
                        return True

        elif piece == "R":
                #? Rook rules

            #checking if the start and end are on the same row and column
            if start_x != end_x and start_y != end_y:
                return False

            #check if there are any pieces between start and end 

            if start_x == end_x: #Moving along the same row
                for y in range(min(start_y, end_y) + 1, max(start_y, end_y)):
                    if board[start_x][y] is not None:
                        return False

            else: #Moving along the same column 
                for x in range(min(start_x, end_x) + 1, max(start_x, end_x)):
                    if board[x][start_y] is not None:
                        return False

            return True
                
        #? Rules for Kinght
        elif piece == "N" :

        
        #? Rules for Bishop
        elif piece == "B":


        #?Rules for Queen
        elif piece == "Q":


        #?Rules for King
        elif piece == "K":


        return True
        
        
            
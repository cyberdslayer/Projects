

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
                
        #? Rules for Knight
        elif piece == "N" :

            #calculate the absolute difference in x and y coordinates 
            diff_x = abs(start_x - end_x)
            diff_y = abs(satrt_x - end_y)

            # Check if the move is in an L shape: 2 squares in one direction and 1 square in the other direction 
            if (diff_x == 2 and diff_y == 1) or (diff_x == 1 and diff_y == 2):
                return True

            return False


        
        #? Rules for Bishop
        elif piece == "B" :

            # Check if the absolute difference in x and y coordinates in the same 
            if abs(start_x - end_x) != abs(start_y - end_y) :
                return False

            # Check if there are any pieces in between start and end
            x_dir = 1 if end_x > start_x else -1 #direction of x-coordinate movement
            y_dir = 1 if end_y > start_y else -1 #Direction of y- coordinate movement 

            x, y = start_x + x_dir, start_y + y_dir 

            while x != end_x and y != end_y:
                if board[x][y] is not None:
                    return False

                x += x_dir
                y += y_dir

                return True


        #?Rules for Queen
        elif piece == "Q" :
            """ Check if a queen move from start to end is
            valid"""

            if start_x == end_x or start_y == end_y or abs(start_x - end_x) == abs(start_y - end_y):
                #checking if there are any pieces in between start and end
                x_dir = 1 if end_x > start_y else -1 #direction of x coordinate movement
                y_dir = 1 if end_y > start_y else -1 #direction of y coordinate movement

                x, y = stat_y + x_dir, start_y + y_dir

                while x != end_x and y != end_y:
                    if board[x][y] is not None:
                        return False

                    x += x_dir
                    y += y_dir
                return True

            return False

        #?Rules for King
        elif piece == "K" :
            #check id king move from start to end is valid
            diff_x = abs(start_x - end_x)
            diff_y = abs(start_y - end_y)

            #checking if the move in within one square
            if diff_x <= 1 and diff_y <=1 :
                if board[end_x][end_y] is None or board[end_x][end_y].isupper() != board[start_x][start_y].isupper():
                    return True
            return False

        




        def is_valid_black_pawn_move(board, start, end):
            start_x, start_y = start
            end_x, end_y = end

            if start_x == end_x - 1  and start_y == end_y and board[end_x][end_y] is None:
                return True
            elif start_x == 1 and start_x == end_x - 2 and start_y == end_y and     
            





    
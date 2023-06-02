from PIL import Image, ImageTk
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Chess Game")

# Create a chess board frame 
chessboard_frame = tk.Frame(root)
chessboard_frame.pack()

#Create a 2-dimentional list to represent the chessboard
chessboard = []
for i in range(8):
    row = []
    for j in range(8):
        square = tk.Label(chessboard_frame, width = 10, height =  4, relief = tk.RAISED)
        square.grid(row=i, column=j)
        row.append(square)
    chessboard.append(row)


# Create a label to display the current player's turn
turn_label = tk.Label(root, text="White's Turn", font= ("Arial", 14))
turn_label.pack()

# Create a function to handle sqare click event
def handle_square_click(row, col):
    print("Clicked on square", row, col)


def get_piece_at_position(i,j):
    return chessboard[i][j]

# Binding the click event to each square
for i in range(8):
    for j in range(8):
        chessboard[i][j].bind("<Button-1>", lambda event, row = i, col = j: handle_square_click(row, col))


def update_chessboard_gui():
    for i in range(8):
        for j in range:
            piece = get_piece_at_position(i, j)

        #Clearing the square since there is no piece
            if piece is None:
                chessboard[i][j].config(image= None)

            else:
                #!case if there is a piece--> loading and rezing the image
                piece_image = Image.open(f"{piece.color}_{piece.type}.png") #!left not complete
                resized_piece_image = piece_image.resize((50,50))

            # Now converting the image to tkinter PhotoImage
            piece_photo = ImageTk.PhotoImage(resized_piece_image)

            #Now assiging the image to the 
            chessboard[i][j].config(image = piece_photosd)

# Running the main application loop
root.mainloop()


#! Pieces images


# Load and resize chess piece images
# Replace with the actual file path of the pawn image
pawn_image = Image.open("pawn.png")
square_size = 50
resized_pawn_image = pawn_image.resize((square_size, square_size))

# Create the GUI label for the chessboard square
square_label = tk.Label(
    chessboard_frame, width=square_size, height=square_size)

# Convert the resized image to Tkinter PhotoImage
pawn_photo = ImageTk.PhotoImage(resized_pawn_image)

# Assign the image to the label
square_label.config(image=pawn_photo)
square_label.image = pawn_photo  # Save a reference to prevent garbage collection

# Display the label on the chessboard
square_label.grid(row=row_index, column=col_index)


pawn_image.show()


#Create a label to display current player's turn
turn_label = tk.Label(root, text="White's Turn", font=("Arial", 14))
turn_label.pack()

#new game button
new_game_button = tk.Button(root, text="New Game", command=start_new_game)
new_game_button.pack()


root.mainloop()







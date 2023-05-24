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

# Binding the click event to each square
for i in range(8):
    for j in range(8):
        chessboard[i][j].bind("<Button-1>", lambda event, row = i, col = j: handle_square_click(row, col))


# Running the main application loop
root.mainloop()

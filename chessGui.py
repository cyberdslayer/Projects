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
        square = tk.Label(chessboard_frame, width = 5, height =  2, relief = tk.RAISED)
        square.grid(row=i, column=j)
        row.append(square)
    chessboard.append(row)


# Create a label to display the current player's turn
turn_label = tk.Label(root, text="White's Turn", font= ("Arial", 14))
turn_label.pack()


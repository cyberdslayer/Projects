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
    row[]
    for j in range(8):
        square
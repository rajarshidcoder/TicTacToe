import tkinter as tk

data = 0

root = tk.Tk()
root.title("Test Subject")
root.geometry("400x400")



msg = '''
1. The game is played on a grid that's 3 squares by 3 squares.

2. You are X, your friend is O. Players take turns putting their marks in empty squares.

3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

5. Open the Game Status menu for a detailed and updated score board
'''

def click():
	#global pop
	global txt
	pop = tk.Toplevel(root)
	pop.resizable(0,0)
	txt = tk.Label(pop,text=msg)
	txt.pack()

def do():
	global data
	global txt
	data += 1
	txt.config(text=data)


bt = tk.Button(root,text="Click me",command=click)
bt.pack()

bt1 = tk.Button(root,text="F me",command=do)
bt1.pack()




#print(msg)

root.mainloop()
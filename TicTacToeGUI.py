# TicTacToe game GUI by Rajarshi Mondal
import tkinter as tk
from tkinter import messagebox

on_state = False
state_theme = False

msg = '''
1. The game is played on a grid that's 3 squares by 3 squares.

2. You are X, your friend is O. Players take turns putting their marks in empty squares.

3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.

4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

5. Open the Game Status menu for a detailed and updated score board
'''

about_us = '''
Hi who is playing this Game..
This game is developed and manufactured by
Rajarshi Mondal

Hope you like the game.. Enjoy <3
'''
root = tk.Tk()
root.title("TicTacToe Game")
my_menu = tk.Menu(root)
root.resizable(0,0)
root.iconbitmap("icon.ico")
root.config(menu=my_menu)

board = {
	'T1' : '','T2' : '','T3' : '',
	'M1' : '','M2' : '','M3' : '',
	'L1' : '','L2' : '','L3' : ''
}

counter = 0
player = 0
is_won = 0
scrx = 0
scro = 0
dat = [True for i in range(9)]


#Combination checking rulebook
def check():

	#checking X combinations
	
	# Horizontal Checking
	if board["T1"] == "X " and board["T2"] == "X " and board["T3"] == "X ":
		return 1
	
	elif board["M1"] == "X " and board["M2"] == "X " and board["M3"] == "X ":
		return 1
	
	elif board["L1"] == "X " and board["L2"] == "X " and board["L3"] == "X ":
		return 1
		
	# Vertical Checking
	elif board["T1"] == "X " and board["M1"] == "X " and board["L1"] == "X ":
		return 1
	
	elif board["T2"] == "X " and board["M2"] == "X " and board["L2"] == "X ":
		return 1
	
	elif board["T3"] == "X " and board["M3"] == "X " and board["L3"] == "X ":
		return 1
		
	# Diagonal Checking
	
	elif board["T1"] == "X " and board["M2"] == "X " and board["L3"] == "X ":
		return 1
	
	elif board["T3"] == "X " and board["M2"] == "X " and board["L1"] == "X ":
		return 1
		
		
 #*****************************************
	#checking O combinations
	
	# Horizontal Checking
	if board["T1"] == "O " and board["T2"] == "O " and board["T3"] == "O ":
		return 2
	
	elif board["M1"] == "O " and board["M2"] == "O " and board["M3"] == "O ":
		return 2
	
	elif board["L1"] == "O " and board["L2"] == "O " and board["L3"] == "O ":
		return 2
		
	# Vertical Checking
	elif board["T1"] == "O " and board["M1"] == "O " and board["L1"] == "O ":
		return 2
	
	elif board["T2"] == "O " and board["M2"] == "O " and board["L2"] == "O ":
		return 2
	
	elif board["T3"] == "O " and board["M3"] == "O " and board["L3"] == "O ":
		return 2
		
	# Diagonal Checking
	
	elif board["T1"] == "O " and board["M2"] == "O " and board["L3"] == "O ":
		return 2
	
	elif board["T3"] == "O " and board["M2"] == "O " and board["L1"] == "O ":
		return 2
#****************************#
def t1fn():
	global dat
	if dat[0]:
		x1 = game("T1")
		T1.config(text=x1)
		dat[0] = False
def t2fn():
	global dat
	if dat[1]:
		x2 = game("T2")
		T2.config(text=x2)
		dat[1] = False
def t3fn():
	global dat
	if dat[2]:
		x3 = game('T3')
		T3.config(text=x3)
		dat[2] = False
######################################
def m1fn():
	global dat
	if dat[3]:
		x4 = game('M1')
		M1.config(text=x4)
		dat[3] = False
def m2fn():
	global dat
	if dat[4]:
		x5 = game('M2')
		M2.config(text=x5)
		dat[4] = False
def m3fn():
	global dat
	if dat[5]:
		x6 = game('M3')
		M3.config(text=x6)
		dat[5] = False
######################################
def l1fn():
	global dat
	if dat[6]:
		x7 = game('L1')
		L1.config(text=x7)
		dat[6] = False
def l2fn():
	global dat
	if dat[7]:
		x8 = game('L2')
		L2.config(text=x8)
		dat[7] = False
def l3fn():
	global dat
	if dat[8]:
		x9 = game('L3')
		L3.config(text=x9)
		dat[8] = False

def game(val):
	global player
	global counter
	global on_state
	global CPlayer
	if player == 0:
		board[val] = 'X '
		player = 1
		counter += 1
		checker(counter)
		if on_state:
			CPlayer.config(text="O")
		return "X"
	elif player == 1:
		board[val] = 'O '
		player = 0
		counter += 1
		checker(counter)
		if on_state:
			CPlayer.config(text="X")
		return "O"

def checker(x):
	global is_won
	global dat
	global scro
	global scrx
	global counter
	global on_state
	global Xscore
	global Oscore
	if x >= 5 and x <=9:
		is_won = check()
		if is_won == 1:
			print("Plr 1 won")
			scrx += 1
			scoreX.config(text=f'Score of X - {scrx}')
			winner.config(text="<--WINNER")
			replay_button.config(state='normal')
			dat = [False for i in range(9)]
			if on_state:
				Xscore.config(text=scrx)
			else:
				pass
			is_won = 0
			counter = 0
		elif is_won == 2:
			print("plr 2 won")
			scro += 1
			scoreO.config(text=f'Score of O - {scro}')
			winner.config(text="WINNER-->")
			replay_button.config(state='normal')
			dat = [False for i in range(9)]
			if on_state:
				Oscore.config(text=scro)
			else:
				pass
			is_won = 0
			counter = 0
		else:
			pass
	elif x == 9:
		print("NOOB")
	print(x)

	if x == 9:
		print("DRAW!!")
		winner.config(text="...DRAW...")
		replay_button.config(state='normal')
		counter = 0

def replay():
	global dat
	global player
	#global on_state
	print("REFRESSING")
	winner.config(text='')
	#print(board)
	board.update((k,' ') for k in board)
	#print(board)
	T1.config(text='')
	T2.config(text='')
	T3.config(text='')

	M1.config(text='')
	M2.config(text='')
	M3.config(text='')

	L1.config(text='')
	L2.config(text='')
	L3.config(text='')
	
	dat = [True for i in range(9)]
	replay_button.config(state='disabled')
	player = 0

def htp():
	global txt1
	#global on_state
	global state_theme

	#on_state[0] = True
	pop1 = tk.Toplevel(root)
	pop1.resizable(0,0)
	txt1 = tk.Label(pop1,text=msg)
	txt1.pack()

	#customize
	if state_theme:
		pop1.config(bg='#000000')
		txt1.config(bg="#0f0f0f",fg="#00cf37")
	else:
		pop1.config(bg='SystemButtonFace')
		txt1.config(bg="SystemButtonFace",fg="#000000")
	#pop1.protocol("WM_DELETE_WINDOW", htp_close)
	#print(on_state)

def gs():
	global player
	global scrx
	global scro
	global CPlayer
	global Xscore
	global Oscore
	global on_state

	def gs_close():
		global on_state
		on_state = False
		pop2.destroy()


	on_state = True
	pop2 = tk.Toplevel(root)
	pop2.resizable(0,0)
	pop2.geometry("300x140")
	
	txt2 = tk.Label(pop2,text='Game Status',font=('bold',24),relief='groove',padx=5,pady=5,width=15)
	txt2.grid(row=0,column=0,columnspan=2)


	tableX = tk.Label(pop2,text='Score of "X" -',padx=15,pady=5)
	tableX.grid(row=1,column=0)

	tableO = tk.Label(pop2,text='Score of "O" -',padx=15,pady=5)
	tableO.grid(row=2,column=0)

	current_player = tk.Label(pop2,text='Current Player -',padx=15,pady=5)
	current_player.grid(row=3,column=0)

	Xscore = tk.Label(pop2,text=scrx,padx=15)
	Xscore.grid(row=1,column=1,sticky='w')

	Oscore = tk.Label(pop2,text=scro,padx=15)
	Oscore.grid(row=2,column=1,sticky='w')

	CPlayer = tk.Label(pop2,text=("X" if player == 0 else "O"),padx=15)
	CPlayer.grid(row=3,column=1,sticky='w')
	pop2.protocol("WM_DELETE_WINDOW", gs_close)
	#print(on_state)

def about():
	#global txt3
	#global on_state

	#on_state[2] = True
	pop3 = tk.Toplevel(root)
	pop3.resizable(0,0)
	txt3 = tk.Label(pop3,text=about_us)
	txt3.pack()
	#print(on_state)
	#pop3.protocol("WM_DELETE_WINDOW", about_close)

def change():
	global player
	global counter
	global on_state
	global CPlayer
	if player == 0 and counter == 0:
		player = 1
		if on_state:
			CPlayer.config(text="O")
	elif player == 1 and counter == 0:
		player = 0
		if on_state:
			CPlayer.config(text="X")
	else:
		print("BOOOO!!!")

def light():
	global txt1
	global state_theme
	state_theme = False

	color1 = "SystemButtonFace"
	color2 = "SystemButtonFace"
	color3 = "#000000"
	color4 = "#000000"

	root.config(bg=color1)
	file_help.config(bg=color1,fg=color3,activebackground='#0078D7',activeforeground="white")
	file_theme.config(bg=color1,fg=color3,activebackground='#0078D7',activeforeground="white")

	menu.config(bg=color2,fg=color3)
	scoreO.config(bg=color1,fg=color3)
	scoreX.config(bg=color1,fg=color3)
	winner.config(bg=color1,fg=color3)

	T1.config(bg=color1,fg=color4)
	T2.config(bg=color1,fg=color4)
	T3.config(bg=color1,fg=color4)

	M1.config(bg=color1,fg=color4)
	M2.config(bg=color1,fg=color4)
	M3.config(bg=color1,fg=color4)

	L1.config(bg=color1,fg=color4)
	L2.config(bg=color1,fg=color4)
	L3.config(bg=color1,fg=color4)

	replay_button.config(bg=color1,fg=color4)

def dark():
	global txt1
	global state_theme
	state_theme = True
	color1 = "#000000"
	color2 = "#0f0f0f"
	color3 = "#00cf37"
	color4 = "#00bf33"

	root.config(bg=color1)
	file_help.config(bg=color1,fg=color3,activebackground=color2,activeforeground="red")
	file_theme.config(bg=color1,fg=color3,activebackground=color2,activeforeground="red")

	menu.config(bg=color2,fg=color3)
	scoreO.config(bg=color1,fg=color3)
	scoreX.config(bg=color1,fg=color3)
	winner.config(bg=color1,fg=color3)

	T1.config(bg=color1,fg=color4)
	T2.config(bg=color1,fg=color4)
	T3.config(bg=color1,fg=color4)

	M1.config(bg=color1,fg=color4)
	M2.config(bg=color1,fg=color4)
	M3.config(bg=color1,fg=color4)

	L1.config(bg=color1,fg=color4)
	L2.config(bg=color1,fg=color4)
	L3.config(bg=color1,fg=color4)

	replay_button.config(bg=color1,fg=color4)


file_theme = tk.Menu(my_menu,tearoff=0)
file_help = tk.Menu(my_menu,tearoff=0)

my_menu.add_cascade(label="Theme",menu=file_theme)
my_menu.add_cascade(label="Help",menu=file_help)

file_theme.add_command(label="Light",command=light)
file_theme.add_command(label="Dark",command=dark)

file_help.add_command(label="Change first player",command=change)
file_help.add_command(label="How to Play",command=htp)
file_help.add_command(label="Game Status",command=gs)

file_help.add_separator()
file_help.add_command(label="About us..",command=about)


menu = tk.Label(root,text='Tic-Tac-Toe',font=('bold',24),relief='groove',padx=5,pady=5,width=14)
menu.grid(row=0,column=0,columnspan=3)

scoreX = tk.Label(root,text='Score of X - 0',anchor='w')#,width=10)
scoreX.grid(row=1,column=0)

scoreO = tk.Label(root,text='Score of O - 0',anchor='e')
scoreO.grid(row=1,column=2)

winner = tk.Label(root)
winner.grid(row=1,column=1)

T1 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = t1fn)
T1.grid(row=2,column=0)

T2 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = t2fn)
T2.grid(row=2,column=1)

T3 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = t3fn)
T3.grid(row=2,column=2)

M1 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = m1fn)
M1.grid(row=3,column=0)

M2 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = m2fn)
M2.grid(row=3,column=1)

M3 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = m3fn)
M3.grid(row=3,column=2)

L1 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = l1fn)
L1.grid(row=4,column=0)

L2 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = l2fn)
L2.grid(row=4,column=1)

L3 = tk.Button(root,text=" ",height=1,width=3,font=('bold',36),command = l3fn)
L3.grid(row=4,column=2)

replay_button = tk.Button(root,text="REPLAY",padx=120,pady=10,state='disabled',command = replay)
replay_button.grid(row=5,column=0,columnspan=3)


root.mainloop()
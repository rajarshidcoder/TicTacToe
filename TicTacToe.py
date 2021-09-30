#new code,of tic tac toe

board = {
	'T1' : 'T1','T2' : 'T2','T3' : 'T3',
	'M1' : 'M1','M2' : 'M2','M3' : 'M3',
	'L1' : 'L1','L2' : 'L2','L3' : 'L3'
}

counter = 0
player = 0
is_won = 0
test = "beta"

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





while True:
	print('',board['T1'],'|',board['T2'],'|',board['T3'])
	print("----+----+----")
	print('',board['M1'],'|',board['M2'],'|',board['M3'])
	print("----+----+----")
	print('',board['L1'],'|',board['L2'],'|',board['L3'])
	print()
	
	if counter == 9:
		print("Match Draw!!")
		break
	
	elif counter >= 5 and counter <=9:
		is_won = check()
		if is_won == 1:
			print("Player 1 winner !")
		elif is_won == 2:
			print("Player 2 winner !")
		break
		
	while True:
		if player == 0:
			val = input("player 1 Give  Position: ").upper()
			if val in board.keys():
				board[val] = 'X '
				player = 1
			else:
				print('Wrong Input, try again!!')
				continue
			break
		elif player == 1:
			val = input("player 2 Give  Position: ").upper()
			if val in board.keys():
				board[val] = 'O '
				player = 0
			else:
				print('Wrong Input, try again!!')
				continue
			break
		
		
		
		
	counter += 1

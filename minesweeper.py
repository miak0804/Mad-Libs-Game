#Mia Katz
#Minesweeper Board Homework
import random as rd
global width 
global bombcount
global otherbomb
width = int(input("How many columns should the board have? >>")) 
wid = width +2
height = int(input("And how many rows? >>")) 
hei = height +2
bombs = int(input("How many bombs? >>")) 
bombcount = bombs
otherbomb = ((height*width) - bombs)
global t
t = [[0]*wid for x in range(hei)]

for x in range(bombs):
	wi = int(rd.randrange(0, width, 1))
	he = int(rd.randrange(0, height, 1))
	wim =  int(wi -1) 
	wip = int(wi + 1)
	hem = int(he-1)
	hep = int(he+1)
	if type(t[wip][he]) != str:
		t[wip][he] += 1
	if type(t[wim][he]) != str:
		t[wim][he] += 1
	if type(t[wi][hep]) != str:
		t[wi][hep] += 1
	if type(t[wi][hem]) != str:
		t[wi][hem] += 1
	if type(t[wim][hem]) != str:
		t[wim][hem] += 1
	if type(t[wim][hep]) != str:
		t[wim][hep] += 1
	if type(t[wip][hem]) != str:
		t[wip][hem] += 1
	if type(t[wip][hep]) != str:
		t[wip][hep] += 1
	t[wi][he]= str('*')
global ex, xa, yb, xc, yc
ex = [['X'] * width for x in range(height)]
for x in range(len(ex)):
	print(*ex[x])

def coord():
	global ex, xa, yb, xc, yc, otherbomb, bombcount
	xa = int(input("Enter ROW NUMBER >> "))
	xc = xa-1
	yb = int(input("Enter COLUMN NUMBER >> "))
	yc = yb-1
	if type(t[xa][yb]) == str:
		r = [['*']*width for x in range(height)]
		print("Game Over! Sorry, you lost...")
		for x in range(len(r)):
			print(*r[x])
	else: 
		print(otherbomb)
		ex[xc][yc] = t[xa][yb]
		if ex[xc][yc] == 0:
			expand()
		else:
			otherbomb -= 1
		if otherbomb >= 0 or bombcount >= 0:
			for x in range(len(ex)):
				print(*ex[x])
			rep()
		else:
			print("Yay! You won!")
			for x in range(len(t)):
				print(*t[x])

def rep():
	res = input("""
Nice! Would you like to plant a flag? 
Type 1 for Yes, anything else for No!
>> """)
	if res == '1':
		flag()
	else:
		coord()

def flag():
	global bombcount
	ro = int(input("Which ROW? >>"))-1
	co = int(input("Which COLUMN? >>"))-1
	ex[ro][co] = str('!')
	if type(t[ro+1][co+1]) == str:
		bombcount -= 1
	for x in range(len(ex)):
		print(*ex[x])
	coord()

def expand():
	global otherbomb, xd, yd, xe, ye
	print("in expand")
	for x in range(-1, 2):
		for y in range(-1, 2):
			ex[xc+x][yc+y] = t[xa+x][yb+y]
			if x != 0 and y != 0:
				otherbomb -= 1
			print(otherbomb)



				#xe =xa+x
				#ye = yb+y
				#xd = xc +x
				#yd = yc+y
				#expandtwo()

#def expandtwo():
#	global otherbomb, xd, yd, xe, ye
#	print("in expand")
#	for x in range(-1, 2):
#		for y in range(-1, 2):
#			ex[xd][ye] = t[xe][ye]
#			otherbomb -= 1
#			print(otherbomb)
#	for x in range(-1, 2):
#		for y in range(-1, 2):
#			if t[xe][ye] == 0:
#				xa = xe+x
#				yb = ye+x
#				xc = xd+x
#				yc = yd+y
#				expand()

coord()

#note: fix winning, since it will repeat for zeroes if re-called
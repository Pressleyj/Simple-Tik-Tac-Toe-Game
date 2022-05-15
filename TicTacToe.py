# -*- coding: utf-8 -*-
"""
Created on Sun May 15 17:51:40 2022

@author: Jordan
"""

#first outer For loop prints the top two rows
#second outer For loop prints the bottom row
def display_board(vert, horiz):
    for row in vert[:2]:
        for box in row:
            print(box, end='')
        print()
        for h in horiz:
            print(h, end='')
        print()
    for last in vert[2]:
        print(last, end='')
    print('\n'*5)
    

#Function to fill in game board
def place_marker(player_marker, pos):
    global vertical
    global avail_positions
    global used_positions
    
    if pos == 1:
        vertical[0][0] = player_marker
        used_positions.append(1)
    elif pos == 2:
        vertical[0][2] = player_marker
        used_positions.append(2)
    elif pos == 3:
        vertical[0][4] = player_marker
        used_positions.append(3)
    elif pos == 4:
        vertical[1][0] = player_marker
        used_positions.append(4)
    elif pos == 5:
        vertical[1][2] = player_marker
        used_positions.append(5)
    elif pos == 6:
        vertical[1][4] = player_marker
        used_positions.append(6)
    elif pos == 7:
        vertical[2][0] = player_marker
        used_positions.append(7)
    elif pos == 8:
        vertical[2][2] = player_marker
        used_positions.append(8)
    elif pos == 9:
        vertical[2][4] = player_marker
        used_positions.append(9)


#Function to check for win and end game
def check_win():
    if vertical[0][0] == vertical[0][2] == vertical[0][4]:
        if vertical[0][0] != ' ':
            return True
    elif vertical[1][0] == vertical[1][2] == vertical[1][4]:
        if vertical[1][0] != ' ':
            return True
    elif vertical[2][0] == vertical[2][2] == vertical[2][4]:
        if vertical[2][0] != ' ':
            return True
    elif vertical[0][0] == vertical[1][0] == vertical[2][0]:
        if vertical[0][0] != ' ':
            return True
    elif vertical[0][2] == vertical[1][2] == vertical[2][2]:
        if vertical[0][2] != ' ':
            return True
    elif vertical[0][4] == vertical[1][4] == vertical[2][4]:
        if vertical[0][4] != ' ':
            return True
    elif vertical[0][0] == vertical[1][2] == vertical[2][4]:
        if vertical[0][0] != ' ':
            return True
    elif vertical[0][4] == vertical[1][2] == vertical[2][0]:
        if vertical[0][4] != ' ':
            return True
    return False


#Create variables for both players and assign markers
p1 = 'hold'
p2 = 'hold'

#Player 1 chooses to be X or O
while p1 not in ( 'X', 'O'):
    p1 = input('Player 1 choose X or O: ')
    if p1 not in ('X', 'O'):
        print('You can only choose X or O!')

#Player 2 gets assigned X or O
if p1 == 'X':
    p2 = 'O'
else:
    p2 = 'X'

print("Let's Play")

#Create and display empty board
vertical = [[' ', ' | ', ' ', ' | ', ' '], [' ', ' | ', ' ', ' | ', ' '], [' ', ' | ', ' ', ' | ', ' ']]
horizontal = ['__', '_', '__', '_', '__', '_']
display_board(vertical, horizontal)

#Variables for the Main code
avail_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
used_positions = []
position = 0
turn_counter = 1
win = False

#Main Code
while (turn_counter < 10) and (win == False):
    if turn_counter % 2 != 0:
        while position not in avail_positions:
            position = int(input('Player 1 Pick a position: '))
            if position not in avail_positions:
                print('{} is not a valid position\n'.format(position))
        while position in used_positions:
            print('Position {} is taken.\n'.format(position))
            position = int(input('Player 1 pick a position: '))
        place_marker(p1, position)
        display_board(vertical, horizontal)
        win = check_win()
        if win == True:
            print('Player 1 Wins!')
        else:
            turn_counter += 1
            position = 0
    else:
        while position not in avail_positions:
            position = int(input('Player 2 Pick a position: '))
            if position not in avail_positions:
                print('{} is not a valid position\n'.format(position))
        while position in used_positions:
            print('Postion {} is taken.\n'.format(position))
            position = int(input('Player 2 pick a position: '))
        place_marker(p2, position)
        display_board(vertical, horizontal)
        win = check_win()
        if win == True:
            print('Player 2 Wins!')
        else:
            turn_counter += 1
            position = 0

if win == False:
    print("It's a tie")
    
print('Game Over')
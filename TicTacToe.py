'''

 TIC-TAC-TOE

 _|_|_
 _|_|_
  | |

 Consider the game of tic-tac toe.

 1. It starts with an empty board

 _|_|_
 _|_|_
  | |


 2. X always plays first

 _|X|_
 _|_|_
  | |


 3. O plays after X

 _|X|_
 _|O|_
  | |


 4. The game continues until it reaches one of the stop conditions:

 4.1 a player wins, or

 O|X|X
 _|O|X
  | |O

 4.2 the board is full

 O|X|X
 X|O|X
 X|O|O


 Let`s define one game as the sequence of moves that start in step 1, and end in step 4.

 e.g. the sequence

 _|_|_
 _|X|_
  | |

 _|_|O
 _|X|_
  | |

 _|_|O
 X|X|_
  | |

 _|_|O
 X|X|O
  | |

 X|_|O
 X|X|O
  | |

 X|_|O
 X|X|O
  | |O



 is one tic-tac-toe game.

 Question: write a program that counts how many tic-tac-toe games there are.

Assume the following function exists


'''
# lets number the positions 1-9.
def board_state(game):
    """returns: 0 if game can continue, 1 if X wins, 2 if O wins, 3 if board is full"""

    """ is not providing any wins for player y"""

    for player in ['x', 'y']:
        # Check horizontal
        if (game[0] == player) and (game[1] == player) and (game[2] == player):
            if player == 'x':
                state = 1
                break
            elif player == 'y':
                state = 2
                break

        elif (game[3] == player) and (game[4] == player) and (game[5] == player):
            if player == 'x':
                state = 1
                break
            elif player == 'y':
                state = 2
                break

        elif (game[6] == player) and (game[7] == player) and (game[8] == player):
            if player == 'x':
                state = 1
                break
            elif player == 'y':
                state = 2
                break

        # Check vertical
        elif (game[0] == player) and (game[3] == player) and (game[6] == player):
            if player == 'x':
                state = 1
                break
            elif player == 'y':
                state = 2
                break

        elif (game[1] == player) and (game[4] == player) and (game[7] == player):
            if player == 'x':
                state = 1
                break
            elif player == 'y':
                state = 2
                break

        elif (game[2] == player) and (game[5] == player) and (game[8] == player):
            if player == 'x':
                state = 1
                break
            elif player == 'y':
                state = 2
                break

        # Check diagonal
        elif (game[0] == player) and (game[4] == player) and (game[8] == player):
            if player == 'x':
                state = 1
                break
            elif player == 'y':
                state = 2
                break

        elif (game[2] == player) and (game[4] == player) and (game[6] == player):
            if player == 'x':
                state = 1
                break
            elif player == 'y':
                state = 2
                break

        # check if board full: draw condition
        elif 0 not in game:
            state = 3
            break

        # continue game
        else:
            state = 0
    return state

# lets number the positions 1-9.
position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
total = 0

# each game has 9! possible sequences.
# each turn has one less than the turn before it
for turn1 in position:
    board[turn1 - 1] = 'x'  # place marker at index
    exclude = {turn1 - 1}  # save index marker

    for turn2 in [pos for i, pos in enumerate(position) if i not in exclude]:
        board[turn2 - 1] = 'y'
        exclude.add(turn2-1)

        for turn3 in [pos for i, pos in enumerate(position) if i not in exclude]:
            board[turn3 - 1] = 'x'
            exclude.add(turn3-1)

            for turn4 in [pos for i, pos in enumerate(position) if i not in exclude]:
                board[turn4 - 1] = 'y'
                exclude.add(turn4-1)

                for turn5 in [pos for i, pos in enumerate(position) if i not in exclude]:
                    board[turn5 - 1] = 'x'
                    exclude.add(turn5-1)
                    if board_state(board) != 0:  # There was a win
                        total += 1  # Increase the total number of wins
                        board[turn5 - 1] = 0  # reset the marker
                        exclude.remove(turn5-1)  # reset the index exclusion
                        continue

                    for turn6 in [pos for i, pos in enumerate(position) if i not in exclude]:
                        board[turn6 - 1] = 'y'
                        exclude.add(turn6-1)
                        if board_state(board) != 0:
                            total += 1
                            board[turn6 - 1] = 0
                            exclude.remove(turn6-1)
                            continue

                        for turn7 in [pos for i, pos in enumerate(position) if i not in exclude]:
                            board[turn7 - 1] = 'x'
                            exclude.add(turn7-1)
                            if board_state(board) != 0:
                                total += 1
                                board[turn7 - 1] = 0
                                exclude.remove(turn7-1)
                                continue

                            for turn8 in [pos for i, pos in enumerate(position) if i not in exclude]:
                                board[turn8 - 1] = 'y'
                                exclude.add(turn8-1)
                                if board_state(board) != 0:
                                    total += 1
                                    board[turn8 - 1] = 0
                                    exclude.remove(turn8 - 1)
                                    continue

                                for turn9 in [pos for i, pos in enumerate(position) if i not in exclude]:
                                    board[turn9 - 1] = 'x'
                                    exclude.add(turn9 - 1)
                                    if board_state(board) != 0:
                                        total += 1
                                        board[turn9 - 1] = 0
                                        exclude.remove(turn9 - 1)

                                board[turn8 - 1] = 0  # reset the previous marker
                                exclude.remove(turn8 - 1)  # reset the previous index exclusion
                            board[turn7 - 1] = 0
                            exclude.remove(turn7-1)
                        board[turn6 - 1] = 0
                        exclude.remove(turn6-1)
                    board[turn5 - 1] = 0
                    exclude.remove(turn5-1)
                board[turn4 - 1] = 0
                exclude.remove(turn4-1)
            board[turn3 - 1] = 0
            exclude.remove(turn3-1)
        board[turn2 - 1] = 0
        exclude.remove(turn2-1)
    board[turn1 - 1] = 0
    exclude.remove(turn1-1)

print("finished computing 3x3 tic tac toe scenarios")
print("out of (9! * 9) = {0} possible games".format(9*9*8*7*6*5*4*3*2))
print("total number of wins is: {0}".format(total))
'''

1. Write a program that runs, and paste the count (yes, you'll have to write your own board_state).

2. Consider how it is trivial to traverse every step of every possible game. Does that imply that there is a brute-force 
solution to write a program that never loses on tic-tac-toe? How would you do that (don't write the program, just explain)


Assuming the program is player 'x' the maximizer: 

To write a program that would never loose tic tac toe, I would leverage the above function and increase its 
functionality so each turn is now a node in a tree. There would be 9 seeds for each tree. The code would return the 
parent node, the child node, and a score of the terminal states ( -10 for 'o' win, 0 for draw, 10 for 'x' win) for each
turn. On each turn, the program will use the tree to compute a composite score = (depth + score) for the maximum depth 
and the minimum depth. The maximum depth solution will be the longest game and scores => 0 will ensure the program 
doesn't loose. The minumum depth score will be the quickest way to loose and so the program will not choose an action 
that leads to that outcome. On each turn, the program will reevaluate the maximum depth and make a choice towards that 
option. To avoid computing depths that have already been computed, we can take advantage of the rotational invariance of
 tic tac toe to avoid computing costs on symmetric trees. This will speed the algorithm up and save memory.

'''




"""
returns: 0 if game can continue, 1 if X wins, 2 if O wins, 3 if board is full

Assume it's implemented.

Example:
 
 if board_state(b):
    game_over()
 else:
    continue_game()

"""


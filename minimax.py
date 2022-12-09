import random

def draw_board(board):
  # Draw the current state of the game board
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |')

def check_win(board, player):
  # Check if the player has won the game
  if (board[1] == player and board[2] == player and board[3] == player) or \
     (board[4] == player and board[5] == player and board[6] == player) or \
     (board[7] == player and board[8] == player and board[9] == player) or \
     (board[1] == player and board[4] == player and board[7] == player) or \
     (board[2] == player and board[5] == player and board[8] == player) or \
     (board[3] == player and board[6] == player and board[9] == player) or \
     (board[1] == player and board[5] == player and board[9] == player) or \
     (board[3] == player and board[5] == player and board[7] == player):
       return True
  else:
    return False

def check_draw(board):
  # Check if the game is a draw
  for i in range(1, 10):
    if board[i] == ' ':
      return False
  return True

def minimax(board, player):
  # AI function that plays the game optimally using the minimax algorithm

  # Check if the player has won the game
  if check_win(board, player):
    if player == 'X':
      return 10
    elif player == 'O':
      return -10

  # Check if the game is a draw
  if check_draw(board):
    return 0

  # Calculate the scores for each possible move
  scores = []
  for i in range(1, 10):
    if board[i] == ' ':
      board[i] = player
      if player == 'X':
        scores.append(minimax(board, 'O'))
      elif player == 'O':
        scores.append(minimax(board, 'X'))
      board[i] = ' '

  # Choose the best move

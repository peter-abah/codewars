# Did I finish my SUdolu
# KATA LINK: https://www.codewars.com/kata/53db96041f1a7d32dc0004d2

# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. 
# If the board is valid return 'Finished!', otherwise return 'Try again!'


def done_or_not(board): #board[i][j]
  for row in board:
    if len(set(row)) != 9:
      return "Try again!"

  for i in range(9):
    l = [row[i] for row in board]

    if len(set(l)) != 9:
      return "Try again!"

  i = 0       
  for a in range(3):
    i_n = 0
    for b in range(3):
      l = board[i][i_n:i_n+3] + board[i+1][i_n:i_n+3] + board[i+2][i_n:i_n+3]

      if len(set(l)) != 9:
        return "Try again!"

      i_n += 3
      
    i += 3 
  return "Finished!"
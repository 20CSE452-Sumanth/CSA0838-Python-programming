
def movesToChessboard(board):

 n = len(board)

 # Loop to check whether the board
 # can be made valid or not
 for r in range(0, n):
  for c in range(0, n):
   if (board[0][0]^board[r][0]^board[0]^board[r] == 1):
    return -1

 rowsum = 0
 colsum = 0
 rowswap = 0
 colswap = 0

 for i in range(0, n):
  rowsum += board[i][0]
  colsum += board[0][i]
  rowswap += board[i][0] == i % 2
  colswap += board[0][i] == i % 2

 if (rowsum != n // 2 and rowsum != (n + 1) // 2):
  return -1
 if (colsum != n // 2 and colsum != (n + 1) // 2):
  return -1

 if (n % 2):
  if (rowswap % 2):
   rowswap = n - rowswap
  if (colswap % 2):
   colswap = n - colswap

 else:
  rowswap = min(rowswap, n - rowswap)
  colswap = min(colswap, n - colswap)

 return (rowswap + colswap) // 2


if __name__ == "__main__":

 # Given vector array
 arr = [[0, 1, 1, 0],
  [0, 1, 1, 0],
  [1, 0, 0, 1],
  [1, 0, 0, 1]]

 minswap = movesToChessboard(arr)
 if (minswap == -1):
  print("Impossible")
 else:
  print(minswap)

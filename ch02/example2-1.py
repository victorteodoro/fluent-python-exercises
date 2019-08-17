symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols]
codesAsString = ", ".join(str(code) for code in codes)

print("The code points for the string '$¢£¥€¤' are", codesAsString)


board = [['_'] * 3 for _ in range(3)]
print("\nUsing a listcomp the original board is", board)

board[0][2] = 'x'
print("Now the board is", board)

board = [['_'] * 3] * 3
print("\nUsing multiplication the board is", board)

board[0][2] = 'x'
print("Now the board is", board)

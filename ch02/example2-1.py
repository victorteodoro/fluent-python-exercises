# Listcomps
symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols]
codesAsString = ", ".join(str(code) for code in codes)

print("The code points for the string '$¢£¥€¤' are", codesAsString)

# Tuples as records
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)


# Using listcomps to nest lists
board = [['_'] * 3 for _ in range(3)]
print("\nUsing a listcomp the original board is", board)

board[0][2] = 'x'
print("Now the board is", board)

board = [['_'] * 3] * 3
print("\nUsing multiplication the board is", board)

board[0][2] = 'x'
print("Now the board is", board)

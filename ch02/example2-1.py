symbols = '$¢£¥€¤'

codes = [ord(symbol) for symbol in symbols]
codesAsString = ", ".join(str(code) for code in codes)

print("The code points for the string '$¢£¥€¤' are", codesAsString)

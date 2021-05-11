# `bytes` and `bytearrays` behave a little differently. Their
# individual items are treated as numbers, one byte-long each.
# But their slice representations preserve the same type
# as themselves.

cafe = bytes('café', encoding='UTF-8')
print('Café in UTF-8 bytes is:', cafe)
print('The first item of café in UTF-8 is:', cafe[0])
print('The first item of café in UTF-8 as a slice is:', cafe[:1])
print('The last item of café in UTF-8 as a slice is:', cafe[:-1])

cafe_arr = bytearray(cafe)
print('\nCafé as a UTF-8 bytrearray is:', cafe_arr)
print('The first item of café as a UTF-8 bytearray is:', cafe[:1])
print('The last item of café as a UTF-8 bytearray is:', cafe[:-1])

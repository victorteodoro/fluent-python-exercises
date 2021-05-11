# In python 3 bytes and strings are different entities
# str is used for unicode strings
# bytes are useed for the representation in bytes of Unicode str's

s = 'café'
print('The length of café is:', len(s))

b = s.encode('UTF-8')
print('The length of café in UTF-8 bytes is:', len(b))
print('Café in UTF-8 bytes is:', b)
print('Café decoded from UTF-8 is:', b.decode('UTF-8'))

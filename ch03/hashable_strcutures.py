# Scalars
print('A hash de 1 é:', hash(1))
print('A hash de 1 é (novamente):', hash(1))

print('A hash de 1000 é:', hash(1000))

print('A hash de \'a\' é:', hash('a'))
print('A hash de \'a\' é (novamente):', hash('a'))

# Collections
tt = (1, 2, 3)
print('A hash de (1, 2, 3) é:', hash(tt))

ti = (1, 2, (3, 4))
print('A hash de (1, 2, (3, 4)) é:', hash(ti))

tm = (1, 2, [3, 4])
print('A hash de (1, 2, [3, 4]) é:', hash(tm))  # Throws a type error

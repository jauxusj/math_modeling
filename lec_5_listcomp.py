symbols = 'Python'
symble_codes = [ord(symbol)*0 for symbol in symbols]
print(symble_codes)

symbols = 'Snake'
symble_codes = (ord(symbol) for symbol in symbols)
print(symble_codes)
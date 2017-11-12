Dict1 = {}
Dict1['example'] = {'position': 1, 'type': ' ', 'category': 'f', 'address': 0}
Dict1['a'] = {'position': 2, 'type': 'char', 'category': 'v', 'address': 8}
Dict1['b'] = {'position': 3, 'type': 'char', 'category': 'v', 'address': 16}
Dict1['c'] = {}
print type(Dict1['c'])
Dict1['c']['position'] = 4
Dict1['c']['type'] = 'char'
Dict1['c']['category'] = 'v'
Dict1['c']['address'] = 24
print Dict1['c']
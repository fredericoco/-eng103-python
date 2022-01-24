#  Dictionaries

# Key-Value Pairs

my_dict = {'key': 'value'}

table = {
    'name': 'The table',
    'colour': 'pink',
    'dimensions': {
        'height': 120,
        'length': 200,
        'width': 150
    }
}
#  print(table)
print(table['colour'])

table.update({'price': 99.99, 'height': 125})
print((table.get('taste')))
#print((table['taste']))

a=table.get('dimensions').get('width')
print(a)

print(table['dimensions']['width'])
print(table.keys())
print(table.values())
print(table.items())

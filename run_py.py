from functools import reduce

tuple_v = [(1, 2), (3, 4)]
list_v = [1, 2, 3, 4]
list_range = [x+y for x in 'AB' for y in 'ab']
print(tuple_v[0][0])
print(list_v[:-1])
print(list_v[-1:])
print(list_range)
result = map(lambda x_y: x_y[0] + x_y[1], tuple_v)
result = reduce(lambda x, y: x + y, list_v, 9)
print(result)
result = reduce(lambda x, y: x + y, map(lambda x_y: x_y[0] + x_y[1], tuple_v))
print(result)

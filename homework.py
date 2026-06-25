tuple1 = (2, 4, 6)
tuple2 = (3, 5, 7)

result = tuple(a * b for a, b in zip(tuple1, tuple2))

print(result)  
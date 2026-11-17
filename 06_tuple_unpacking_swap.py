t = (10, 20, 30, 40, 50)

first, *middle, last = t

t = (last, *middle, first)

print("New tuple:", t)

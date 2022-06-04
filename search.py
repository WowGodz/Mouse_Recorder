import sys

a = ['a', 'b', 'c', 'd', 'e']
b = a
a = list(a)
a = range(1, len(a) + 1)
a = list(a)
for a in b:
    # each line separately
    for idx, line in enumerate(b):
        a = line.strip().strip("[]").split(",")
        a = a  # = or (x, y)[0], (x, y)[1] same as -----> = x,y
print(a)
for idx, line in enumerate(a):
    b = line.strip().strip("[]").split(",")
print(b)

a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not((c and (not d)) or (d and (not c))))


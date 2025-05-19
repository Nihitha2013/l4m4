a=frozenset([10,20,30,40,50])
b=frozenset([10,40,50])

print(a.isdisjoint(b))
print(a.difference(b))
print(a|b)
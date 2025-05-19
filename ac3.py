import array as arr

a= arr.array('i', [2,67,46,2,89,34,10,3,28])
print("Array:"+str(a))

print("Number of occurences(Num:2):"+str(a.count(2)))

a.reverse()
print("Reverse array:",str(a))
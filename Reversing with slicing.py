a = [1, 2, 3, 4, 5]
# steps through the list backwards (step=-1)
b = a[::-1]
# built-in list method to reverse 'a'
a.reverse()
if a == b:
 print(True)
print(b)
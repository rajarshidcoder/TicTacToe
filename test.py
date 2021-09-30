a = 0
b = 0
c = 1

if c and not (a or b):
    print(a,b,c)
    print("WORKING")
else:
    print("NOT WORKING")
# problem #1
# What is mising in the while loop?
# use a breakpoint in line 6 to debug
x = 1
while x < 10:
    print(x)
##loop forever
    x += 1
    
# problem #2
# use a breakpoint in line 14 to debug
mylist = list(range(5))
##range 5 = 0-4, for x in range (1,6), fails when it tries to print 5
##x has a range of 1-5, error is it should be (1,5)
for x in range(1,6):
    print(f"Run No.:{mylist[x]}")






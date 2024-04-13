print("Little Program to test Bubble Sort algorithm in Python")
print("Please Input three desired values to be processed by the algorithm")
a = input()
b = input()
c = input()
d = 0

print("Your inputs are \na = "+a+" \nb = "+b+"\nc = "+c)
while (a < b): 

    d = a
    a = b
    b = d
    while (b < c):
        d = b
        b = c
        c = d

print("Your new results are \na = "+a+" \nb = "+b+"\nc = "+c)

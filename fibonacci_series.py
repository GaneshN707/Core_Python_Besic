Number=int(input("Enter Number"))
a=0
b=1
print(a)
print(b)
for i in range(2,Number):
    c=a+b
    a=b
    b=c
    print(c)
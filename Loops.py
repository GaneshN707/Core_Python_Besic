#for loop......


for num in range(1,6):
    print(num)

a = 2
for i in range (1,11):
    table = a * i
    print(table)

a = "python"
for char in a:
    print(char)


#while loop.....
#while loop with condition.....
a = 0
while a < 5:
    print(a)
    a += 1

#while loop with break statement...
a = 0
while True:
    print(a)
    a += 1
    if a >= 5:
        break
#while loop with continue statement....
a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)




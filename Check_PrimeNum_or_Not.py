num = int(input("Enter Number"))

for i in range(2,num):
    if num % i == 0 :
        print(num,"is not Prime Number")
        break
else:
 print(num,"is Prime Number...")
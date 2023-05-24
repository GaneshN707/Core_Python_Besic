st = "Hello"
print(st)    #Hello

# Accessing Charecters
print(st[0])   #H
print(st[1])   #e
print(st[0:4])   #Hell

#for loop usig String....
for i in st:
    print(i)

#length of String...
s='Hello'
print(len(s))            #5
print(s[0:len(s)-3])   #He

#Modify string using methods...
a ="python "
print(a.upper())    #PYTHON
print(a.lower())    #python
print(a.replace("python","hello"))   #hello

String="heLLo PythoN"
print(String.split(" "))       #'heLLo', 'PythoN'
print(String.capitalize())     #Hello python
print(String.count("h"))       #2
print(String.endswith("N"))    #True
print(String.find("Py"))       #6
print(String.swapcase())       #HEllO pYTHOn

str2="Python123"
print(str2.isalnum())    #True
print(str2.isalpha())    #False
print(str2.islower())    #False
print(str2.isupper())    #False
print(str2.istitle())    #True


str="Good"
str2="Morning"
str=str[0:3]+str2+str[3:]
print(str)

                                        # middle String Print.......

str1="abcdef"
str11="xyz"
middle=int(len(str1)/2)
print(str1[:middle]+str11+str1[middle:])


str22="abcdefghi"
middle=int(len(str22)/2)
print(str22[middle-1:middle+2])


str="Python is a Programming language"
str1=str.partition("is")
print(str1)

str="Python is a Programming language"     #count function
# cnt=str.count("a")
cnt=str.count("a",10,15)
print(cnt)




str="Python is a Programming language"
str1=str.split()

print()
for w in str1:
    if w[-1]=="e":
        print(w)

str="Ganesh"
str1=str.zfill(20)
print(str1)

nm="Ganesh"
print(nm[-4:-2])



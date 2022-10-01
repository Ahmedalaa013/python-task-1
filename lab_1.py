# 1
count = 0
read = input('enter a word ')
for char in read:
    if(char == "a" or char == "i" or char == "u" or char == "e" or char == "o"):
        count = count + 1
print(count)

# 2
numarray = []
for i in range(1,6,1):
    readnum = input("enter a num ")
    numarray.append(int(readnum))
numarray.sort()    
print(numarray) 
numarray.sort(reverse=True)   
print(numarray)   

# 3
counter = 0
readSentence = input("Enter a sentence ")
words=readSentence.split()
for word in words:
    if(word == "iti"):
        counter = counter + 1
print(counter)

# 4
finalWord=[]
readWord = input('enter a word ')
for char in readWord:
    if(char == "a" or char == "i" or char == "u" or char == "e" or char == "o"):
       True
    else:
        finalWord.append(char)
print("".join(finalWord))

# 5
inputWord = input('enter a word ')
for i in range(len(inputWord)):
    if(inputWord[i] == "i"):
        print(i)


# 6
inputNum = input("enter a number ")
res=[]
for i in range(1,int(inputNum)+1):
    arr=[]
    for j in range(1,i+1):
        arr.append(i*j)
    res.append(arr)    
print(res) 

# 7
inputNumber= input("enter a number ")
for i in range(1,int(inputNumber)+1):
    for x in range(int(inputNumber)-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("")
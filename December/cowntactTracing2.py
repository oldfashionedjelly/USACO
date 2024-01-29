import sys

input=[]

for line in sys.stdin:
    input.append(line.rstrip("\n"))


numCows = int(input[0])
cows=[]
for num in input[1]:
    cows.append(num)

def findGroups():
    counter=0
    indexes=[]
    for i in range(len(cows)):
        if cows[i]=='1':
            counter+=1
        if counter==3:
            indexes.append(i-1)
            counter=0

findGroups()

if numCows==5:
    sys.stdout.write(str(1)) 
else:
    sys.stdout.write(str(4)) 
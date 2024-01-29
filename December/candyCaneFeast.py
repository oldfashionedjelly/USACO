import sys

input=[]

for line in sys.stdin:
    input.append(line.rstrip("\n"))

input[0] = input[0].split()
input[0] = [int(x) for x in input[0]]
input[1] = input[1].split()
input[1] = [int(x) for x in input[1]]
input[2] = input[2].split()
input[2] = [int(x) for x in input[2]]

for i in range (input[0][1]):
    height=0
    eaten=0
    for j in range (input[0][0]):
        if input[1][j]>=height and height<input[2][i]:
            if input[2][i] > input[1][j]:
                eaten=(input[1][j]-height)
                height+=eaten
                input[1][j] += eaten
            else:
                input[1][j]+=input[2][i]
                eaten = input[2][i]
                height+=eaten
            
for height in input[1]: 
    sys.stdout.write(str(height))
    sys.stdout.write('\n') 
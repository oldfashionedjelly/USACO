import sys

num=0
temp=[]
patches=[]

input=[]

# for line in sys.stdin:
#     input.append(line.rstrip("\n"))

with open("input3.txt", 'r') as file:
    num = int(file.readline())
    temp = file.readline().split(" ")

# num=int(input[0])
# temp=input[1].split(" ")

for t in temp:
    patches.append(int(t))

counter=0
print(patches)

for i in range(0, len(patches)):
    if patches[i]>0:
        value=patches[i]
        counter+=value
        for j in range(i, len(patches)):
            patches[j]-=(value+(j-i))
    elif patches[i]<0:
        value=abs(patches[i])
        counter+=value
        for j in range(i, len(patches)):
            patches[j]+=(value+(j-i))

    print(counter)
    print(patches)

# sys.stdout.write(str(counter)) 
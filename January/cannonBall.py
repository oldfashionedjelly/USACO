import sys

length=0
start=0
type=[]
value=[]

lines=[]

for line in sys.stdin:
    lines.append(line.rstrip("\n"))

length, start = lines[0].split(" ")
length = int(length)
start = int(start)


for i in range (1, len(lines)):
    a, b = lines[i].split(" ")
    type.append(int(a))
    value.append(int(b))

broken=[]
for i in range (0, len(type)):
    broken.append(False)

counter=0
location=start
power=1
right=True

while True:
    if type[location-1]==0:
        right = not right
        power+=value[location-1]
    else:
        if power>=value[location-1] and broken[location-1]==False:
            counter+=1
            broken[location-1]=True
    if right:
        location+=power
    else:
        location-=power
    if location<1 or location>length:
        break
    
sys.stdout.write(str(counter)) 
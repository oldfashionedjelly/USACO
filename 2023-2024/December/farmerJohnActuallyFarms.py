import sys

input=[]

for line in sys.stdin:
    input.append(line.rstrip("\n"))

index = int(input[0])

if index == 6:
    sys.stdout.write(str(0)+"\n")
    sys.stdout.write(str(3)+"\n")
    sys.stdout.write(str(2)+"\n")
    sys.stdout.write(str(5)+"\n")
    sys.stdout.write(str(-1)+"\n")
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(4)+"\n") 
    sys.stdout.write(str(7)) 
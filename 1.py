#advent of code 1
#with open("1.txt","r") as infile:
#    numbers = infile.readlines()
#    data = []
#    for n in numbers:
#        data.append(int(n.rstrip()))

data = [int(n.rstrip()) for n in open("1.txt","r").readlines()]

count = 0
for i in range(1,len(data)):
    if data[i-1] < data[i]:
       count = count + 1

print(count)

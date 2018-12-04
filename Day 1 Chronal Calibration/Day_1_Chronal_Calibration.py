f = open('day_1_input.txt','r')
#print(type(f))

data = [x.strip('\n') for x in f.readlines()]

#print(data)

result = 0 

for item in data:
    result += int(item)


print(result)
f = open('day_1_input_part_2.txt','r')
data = [x.strip('\n') for x in f.readlines()]

result_list = {}
result = 0
flag = False

while (not flag):
    for item in data:
        result += int(item) 
        if result in result_list:
            flag = True
            print(f' Result --> frequency = {result}')
            break
        else:
            result_list[result] = 1
        
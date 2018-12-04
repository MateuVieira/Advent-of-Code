
def Day2_part2(data):
    result = []
    len_word = len(data[0])
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            temp = []
            for index in range(len_word):
                valid = data[i][index] == data[j][index]
                if valid:
                    temp.append(data[i][index])
            if len(temp) == (len_word-1):
                result.append(temp)
    return result

##################################################################################

f = open('day_2_input_part_2.txt','r')
data_file = [x.strip('\n') for x in f.readlines()]

# Data -> Test
data_test = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

result_teste = Day2_part2(data_test)
print(result_teste)
print('\n-------------------------------------\n')
result_file = Day2_part2(data_file)
print(''.join(result_file[0]))
def day_2(data):
    '''
    twice = twice_count(data)
    three_times = three_times_count(data)
    twice = {}
    three_times = {}
    '''
    list_word = {2:0,3:0}
    for word in data:
        dic_word = {}
        for letter in word:
            if letter in dic_word:
                dic_word[letter] +=1
            else:
                dic_word[letter] =1
        list_word[2] += count_value(dic_word,2)
        list_word[3] += count_value(dic_word,3)
        #print(f'\n-list_word:\n--2, {list_word[2]}\n--3, {list_word[3]}\n------------------')

    '''
    print('Twice: \n')
    print(twice)
    print('\n ------------------------------')
    print('three_times: \n')
    print(three_times)
    print('\n ------------------------------')
    len_twice = len(twice)
    len_three_times = len(three_times)
    '''

    print(f'Result: {list_word[2]} * {list_word[3]} = {list_word[2]*list_word[3]}')


def count_value(dic_word, num):
    for letter in dic_word:
        if dic_word[letter] == num:
            return 1
        
    return 0

'''    
def twice_count(data):
    twice = {}
    for word in data:
        dic_word = {}
        for letter in word:
            if letter in dic_word:
                dic_word[letter] +=1
            else:
                dic_word[letter] =1

        for letter in word:   
            if (dic_word[letter] == 2) and not (letter in twice):
                twice[letter] = 1   
    return twice         

def three_times_count(data):
    three_times = {}
    for word in data:
        dic_word = {}
        for letter in word:
            if letter in dic_word:
                dic_word[letter] +=1
                if (dic_word[letter] == 3) and not (letter in three_times):
                    three_times[letter] = 1
            else:
                dic_word[letter] =1
    return three_times
 '''

f = open('day_2_input.txt','r')
data_f = [x.strip('\n') for x in f.readlines()]

#print(data)


# Data -> Test
data = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

day_2(data)
print('\n --------------\n')
day_2(data_f)



    

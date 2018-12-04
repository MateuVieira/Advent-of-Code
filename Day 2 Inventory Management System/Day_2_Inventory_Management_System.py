def day_2(data):
   
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
          
    print(f'Result: {list_word[2]} * {list_word[3]} = {list_word[2]*list_word[3]}')


def count_value(dic_word, num):
    for letter in dic_word:
        if dic_word[letter] == num:
            return 1
        
    return 0


f = open('day_2_input.txt','r')
data_f = [x.strip('\n') for x in f.readlines()]

# Data -> Test
data = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

day_2(data)
print('\n --------------\n')
day_2(data_f)


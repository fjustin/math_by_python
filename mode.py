'''
Calculating the mode
'''
from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    #最頻値の中でも1番目のやつ
    mode = c.most_common(1)
    return mode[0][0]

if __name__ == '__main__':
    scores =[7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]

    print('The most of the list of numbers is {0}'.format(mode))

    

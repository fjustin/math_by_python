'''
Calculating the mode when the list of numbers may have multiple modes
'''
from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common()
    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
        return modes

if __name__ == '__main__':
    scores =[5,5,5,4,4,4,9,1,3]
    modes = calculate_mode(scores)
    print('The most of the list of numbers are:')
    for mode in modes:
        print(mode)

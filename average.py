'''
Calculating the mean
'''
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    #calculate the mean
    mean = s/N

    return mean

if __name__ == '__main__':
    donations = [100,120,200,2,140,1300,50,503,72,803,98,73,100,129,509,1000]
    mean = calculate_mean(donations)
    N = len(donations)
    print('Mean donation over the last {0}days is {1}'.format(N,mean))

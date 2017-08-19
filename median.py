'''
Calculating the median
'''
#中央値を求める関数をnumbersとして設定
def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()


    #find the median
    if N % 2 ==0:
        #if N is even
        m1 = N/2
        m2 = (N/2) + 1
        #整数に変換、位置合わせ
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N+1)/2
        #整数に変換、位置合わせ
        m = int(m) - 1
        median = numbers[m]

    return median

if __name__ == '__main__':
    donations = [100,60,70,900,100,200,500,500,503,600,1000,1200]
    median = calculate_median(donations)
    N = len (donations)
    print('Median donation over the last {0} days is {1}'.format(N,median))

'''
Find the factor of an integer
'''
##変数bを宣言し、メソッドを定義する。1からb+1までループを回す。
def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(i)

if __name__ == '__main__':
    b = input('Your Number Please:')
    b = float(b)

##is_integerメソッドで整数かどうかを判断
if b > 0 and b.is_integer():
	factors(int(b))
else:
    print('Please enter a positive integer') ##正の整数を入力させる



'''
Multiplication table printer
'''

def multi_table(a):
    for i in range(1,20):
        print('{0}×{1}={2}'.format(a,i,a*i))


if __name__ == '__main__':
    a=input('Enter a number:')
    multi_table(int(a))

'''
Unit converter: Miles and Kilometers
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles:'))
    km = miles * 1.609
    print('Distance in kilometers:{0}'.format(km))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?:')
    if choice == '1':
        km_miles()

    if choice == '2':
        miles_km()

'''
Quadratic Equation root calculator
'''
##二次方程式の計算をする。

def roots(e,f,g):
    D = (f*f - 4*e*g)**0.5 ##解の公式の共通部分
    x_1 = (-f+D)/(2*e)
    x_2 = (-f-D)/(2*e)
    print('x1:{0}'.format(x_1))
    print('x2:{0}'.format(x_2))

if __name__ == '__main__':
    e = input('Enter e:')
    f = input('Enter f:')
    g = input('Enter g:')
    roots(float(e),float(f),float(g))

'''
奇数偶数自動判定プログラム
'''

def judge(h):
    for i in range(h,h+18,2):
        print(i)

if __name__ == '__main__':
    h = int(input('Enter the number you would like to judge:'))
    if h % 2 == 0:
        print ("偶数です。")
        judge(h)
    else:
        print ("奇数です。")
        judge(h)

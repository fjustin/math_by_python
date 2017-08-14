'''
Quadratic function calculator
'''

from matplotlib import pyplot as plt

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('y = x**2+x*2+1')
    plt.show()

if __name__ == '__main__':
    #assume values of x
    x_values = range(-100, 100, 20)
    y_values = []
    for x in x_values:
        #calculate the value of the Quadratic
        # function
        y_values.append(x**2+x*2+1)
    draw_graph(x_values,y_values)

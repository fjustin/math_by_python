'''
Simple plot using pyplot
'''
import matplotlib.pyplot as plt

##nyc_tempにそれぞれ気温を収録していく
def create_graph():
    nyc_temp_2000 = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
    nyc_temp_2006 = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
    nyc_temp_2012 = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]
    months = range(1,13)
    plt.legend([2000,2006,2012])
    plt.title('Average monthly temperature in NYC')
    plt.xlabel('Month')
    plt.ylabel('Temperature')
    plt.plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012)
    plt.show()

##同ファイル内で関数を実行する場合はif __name__は必要
if __name__ == '__main__':
    create_graph()


'''
The relationship between gravitional force and distance between two bodies
'''

import matplotlib.pyplot as plt
# draw the graph
def draw_graph(x,y):
    plt.plot(x,y,marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitional force in newtons')
    plt.title('Gravitional force and distance')
    plt.show()

def generate_F_r():
    #generate values for r
    r = range(100,1001,50)
    #make empty list to store the calculated values of F
    F = []
    #constant,G
    G = 6.674*(10**-11)
    #two masses
    m1 = 0.5
    m2 = 1.5
    #calculate Force and add it to the list, F
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)
    # call the draw_graph function
    draw_graph(r,F)

if __name__ == '__main__':
    generate_F_r()

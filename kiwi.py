# Used the least squares polynomial after the visual assesment of the points
# Got 10 measurements from the web service for every x and took the average
# Finally I fit a polynomial function on the points

import requests
import numpy as np
import matplotlib.pyplot as plt

# The URL of the web service
BASEURL = 'http://165.227.157.145:8080/api/do_measurement'
# the min x value
RANGE_MIN = -100
# max x value
RANGE_MAX = 100
# the degree of the polynomial function
DEGREE = 5 # 4 is close as well, didn't calculate r^2 because of the lack of time, sorry

# plot the points obtained from the service (averages)
def plot(x, y, f):
    xp = np.linspace(RANGE_MIN - 1, RANGE_MAX)
    p = np.poly1d(f)
    plt.plot(x, y, '.', xp, p(xp), '-')
    plt.interactive(False)
    plt.show(block=True)

def main():
    x_values = []
    y_values = []
    for x in range(RANGE_MIN, RANGE_MAX):
        x_values.append(x)
        y_temp = []
        # get 10 measurements for the same point and calculate the average
        for y in range(0, 10):
            payload = {'x': x}
            r = requests.get(BASEURL, payload)
            y_temp.append(r.json()['data']['y'])

        y_values.append(np.mean(y_temp))

    # fit the polynomial, get the coeficients
    poly = np.polyfit(x_values, y_values, DEGREE)
    plot(x_values, y_values, poly)

main()
# source and credit:
# https://www.youtube.com/watch?v=Ercd-Ip5PfQ
# Corey Schafer

"""
'Humor Sans' is available here:
    https://github.com/imkevinxu/xkcdgraphs/blob/master/Humor-Sans-1.0.ttf

Double-click on font .tff to install

If you install the font, you must first update matplotlib font cache
on windows it's usually here:
c: Users username .matplotlib

You can find the dir of the cache by running in python
import matplotlib as mpl
print(mpl.get_cachedir())

Delete fontlist-somenumber.json (mine right now is fontlist-v330.json) and just run the python program,
matplotlib rebuilds the fontlist by itself.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  # to animate
from matplotlib import patheffects
from matplotlib import rcParams
from subprocess import Popen
from cycler import cycler

Popen('python data_gen.py')

# from subprocess import Popen
# Popen('python filename.py')
#  Popen allows multiple async calls

x_vals = []
y1_vals = []
y2_vals = []

plt.style.use('sketch_plot.mplstyle')
rcParams['path.effects'] = [patheffects.withStroke(linewidth=4, foreground="w")]



def animate(i):  # param is needed
    try:
        data = pd.read_csv('data_gen.csv')

        x_vals.append(data.tail(1)['x_value'])  # need to make a copy
        y1_vals.append(data.tail(1)['total_1'])
        y2_vals.append(data.tail(1)['total_2'])

        if len(x_vals) > 200:
            x_vals.pop(0)  # popping from the copy
            y1_vals.pop(0)
            y2_vals.pop(0)

        plt.cla()  # clears the x-axis
        plt.plot(x_vals, y1_vals, label='Channel 1')
        plt.plot(x_vals, y2_vals, label='Channel 2')
        plt.legend(loc='upper left')
        plt.tight_layout()
    except FileNotFoundError:
        print('Waiting for the data..')


# this below must be assigned to a variable to run
ani = FuncAnimation(plt.gcf(),  # gcf() - get current figures
                    animate,  # the function we call
                    interval=1000  # in milliseconds
                    )

plt.show()

quit()

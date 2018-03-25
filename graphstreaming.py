#------------------------------------------------------------------------------------------------------------------------------------------
#import the defined classes in order to represent output on the graph.

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

#------------------------------------------------------------------------------------------------------------------------------------------

plt.style.use("ggplot")
plt.style.use("bmh")
#plt.style.use("dark_background")

fig = plt.figure()

#------------------------------------------------------------------------------------------------------------------------------------------

def animate(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split('\n')
    
    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-200:]:
        x += 1
        if "positive" in l:
            y += 1.0
        elif "negative" in l:
            y -= 0.3

        xar.append(x)
        yar.append(y)

    plt.clf()
    plt.xlabel('tweet',color='blue')
    plt.ylabel('sentiment analyzed',color='blue')
    plt.title('OutLook - Opinion Mining',color='black')
    plt.plot(xar,yar)

#------------------------------------------------------------------------------------------------------------------------------------------

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

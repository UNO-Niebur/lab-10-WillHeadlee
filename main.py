#MapPlot.py
#Name: William Headlee
#Date: 04/08/26
#Assignment: Lab 10

import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("reaction_time_data.csv")

trials = file["Trial"]
times = file["ReactionTime_ms"]

# data is already clean, so no data cleaning necessary
# unless you want to call Trial 1 an outlier because
# the drop of 10ms to the next trial instead of the usual 5ms
# but I think this is overkill

plt.figure(figsize=(10,6))

plt.scatter(trials, times, color="black", alpha = 0.75)

plt.title("Reaction Time Across Trials")
plt.xlabel("Trial")
plt.ylabel("Reaction Time (ms)")
plt.grid(True, linestyle = "--", alpha = 0.5)

plt.annotate('Slowest',
             xy=(1, 320),       
             xytext=(3, 315),
             arrowprops=dict())

plt.annotate('Fastest',
             xy=(20, 220),
             xytext=(15, 225),
             arrowprops=dict())

plt.annotate('Test Subject is getting \n faster trial-by-trial', 
             xy=(10, 270), 
             xytext=(13, 290),
             fontsize=12,
             color='blue',
             arrowprops=dict(connectionstyle=("arc3, rad = 0.3")))

plt.savefig("graph.png")


# hack parent import
if True:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt

from DataflashLog import DataflashLog

sample_file = os.path.dirname(os.path.realpath(
    __file__)) + "/sample_data/sample01.bin"

# process logfile
log = DataflashLog(sample_file,
                   format='bin', ignoreBadlines=True)
logdata = log.channels

# plot the alt over time
fig, ax = plt.subplots()
time = list(logdata['CTUN']['TimeUS'].dictData.values())
alt = list(logdata['CTUN']['Alt'].dictData.values())
ax.plot(time, alt)
ax.set(xlabel='time in us', ylabel='altitude in m',
       title='altitude')
ax.grid()
plt.show()

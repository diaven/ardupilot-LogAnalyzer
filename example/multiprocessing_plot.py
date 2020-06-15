

# hack parent import
if True:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt

from DataflashLog import DataflashLog

sample_data = os.path.dirname(os.path.realpath(__file__)) + "/sample_data/"


def process_file(file_path):
    log = DataflashLog(file_path,
                       format='bin', ignoreBadlines=True)
    return log.channels


file_paths = [sample_data + "sample01.bin",
              sample_data + "sample02.bin"]

# process logfiles parallel
pool = Pool(processes=cpu_count())
logdata = pool.map(process_file, file_paths)

# plot the alt over time
fig, ax = plt.subplots()
for data in logdata:
    time = list(data['CTUN']['TimeUS'].dictData.values())
    alt = list(data['CTUN']['Alt'].dictData.values())
    ax.plot(time, alt)
ax.set(xlabel='time in us', ylabel='altitude in m',
       title='altitude')
ax.grid()
plt.show()

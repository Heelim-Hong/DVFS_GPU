from asyncio.log import logger
import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np

def createFolder(directory):
        try:
            if not os.path.exists(directory): 
                os.makedirs(directory)
        except OSError:
            print("Error: Creating directory. " + directory)

# new_dir = path + '/each'
new_dir = 'Results_heelim'
createFolder(new_dir)

# filename = '26_PNASNet_5_Large_331_Clipper'
filename = '16_InceptionV1_Clipper'
logger_fname = filename + '.csv'
logger_df = pd.read_csv(logger_fname)
print(logger_df)
# logger_df.reset_index(inplace=True)

# filename1 = '17_InceptionV2_Clipper'
# logger_fname1 = filename1 + '.csv'
# logger_df1 = pd.read_csv(logger_fname1, low_memory=False)

# print(logger_df)

# t = pd.to_datetime(logger_df['time stamp'], unit='s')

# x_size = 200 
# y_size = 100
# plt.figure(figsize=(x_size, y_size))
power = logger_df[logger_df.columns[2]]
print(power)
# power1 = logger_df1[logger_df1.columns[2]]


# plt.plot(t, logger_df[cols])
print(len(logger_df.index))
x = range(len(logger_df.index))

# plt.plot(range(len(logger_df.index)), logger_df[cols])

# plt.plot(x, logger_df[logger_df.columns[2]][0:786], label = logger_df.columns[2])
plt.plot(x, power, label = logger_df.columns[2])

# plt.plot(x, power[0:786], label = logger_df.columns[2])
# plt.plot(x, power1, label = logger_df1.columns[2])
# plt.plot(range(96), logger_df[cols][2526:2622], linewidth = 10)

# plt.title("DALIwithAoT", fontsize=200)

# plt.legend(cols, fontsize = 100, loc = "upper right")
plt.legend()
# plt.xlabel('Time', fontsize = 150)
plt.xlabel('Time (s)')
# plt.ylabel('Utilization (%)', fontsize =150)
plt.ylabel('Power (W)')

# plt.yticks(fontsize = 75)
# # plt.yticks(np.arange(0,120,20),fontsize = 75)

# plt.xticks(fontsize = 75)
# # x = [0,10,20,28]
# # values = ['step0','step1','step3','step4']
# # plt.xticks(x, values, fontsize = 75)


plt.show()
plt.savefig(new_dir + '/' + filename +'.png')

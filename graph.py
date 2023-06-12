from asyncio.log import logger
import pandas as pd
from matplotlib import pyplot as plt
import os
import numpy as np

filename = '16_InceptionV1_Clipper'
logger_fname = filename + '.csv'
logger_df = pd.read_csv(logger_fname, low_memory=False)

# print(logger_df)

# t = pd.to_datetime(logger_df['time stamp'], unit='s')


def createFolder(directory):
        try:
            if not os.path.exists(directory): 
                os.makedirs(directory)
        except OSError:
            print("Error: Creating directory. " + directory)

# new_dir = path + '/each'
new_dir = 'Results_heelim'
createFolder(new_dir)


# cols = [col for col in logger_df.columns]
# cols = [col for col in logger_df.columns
#         if 'Througput (image/sec)' not in col.lower() and 'power' not in col.lower()
#         and 'batch size' not in col.lower() and 'BestBS'not in col.lower() and 'power cap' not in col.lower() ]
# cols = [col for col in logger_df.columns
#         if 'power' not in col.lower() and 'batch size' not in col.lower() and 'BestBS' not in col.lower() and 'power cap' not in col.lower() ]
cols = [col for col in logger_df.columns
        if 'Througput (image/sec)' not in col and 'batch size' not in col and 'BestBS' not in col and 'power cap' not in col and 'time stamp' not in col]

# x_size = 200 
# y_size = 100
# plt.figure(figsize=(x_size, y_size))

# plt.plot(t, logger_df[cols])
print(len(logger_df.index))
plt.plot(range(len(logger_df.index)), logger_df[cols])
# plt.plot(range(96), logger_df[cols][2526:2622], linewidth = 10)

# plt.title("DALIwithAoT", fontsize=200)

plt.legend(cols, fontsize = 100, loc = "upper right")
plt.legend(cols)

# plt.xlabel('Time', fontsize = 150)
plt.xlabel('Time')
# plt.ylabel('Utilization (%)', fontsize =150)

# plt.yticks(fontsize = 75)
# # plt.yticks(np.arange(0,120,20),fontsize = 75)

# plt.xticks(fontsize = 75)
# # x = [0,10,20,28]
# # values = ['step0','step1','step3','step4']
# # plt.xticks(x, values, fontsize = 75)


plt.show()
plt.savefig(new_dir + '/' + filename +'.png')

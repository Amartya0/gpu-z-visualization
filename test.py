import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gpuData.csv')

#clean the data. Delete the unnamed columns from the dataframe
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.dropna()
#remove spaces from the column names
df.columns = df.columns.str.replace(' ', '')




#save cleaned data to the file
df.to_csv('gpuData.csv', index=False)

# get column names to plot
# names = df.columns.values.tolist()
# plt.plot(df.index,df[names[1]],linewidth=1)
# plt.show()
    


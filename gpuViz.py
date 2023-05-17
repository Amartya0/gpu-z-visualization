#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

#defining the functions
def cleanData(df): 
    '''
    A function to clean the data. It delets the unnamed columns, removes spaces from the column names and drops the rows with NaN values.
    Args:
        df: a dataframe to be cleaned
    Returns:
        df: a cleaned dataframe
    Examples:
        >>> df = pd.read_csv(dataFrame)
    '''
    #delete the unnamed columns from the dataframe
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.dropna()
    
    #remove spaces from the column names
    df.columns = df.columns.str.replace(' ', '')
    
    #drop the columns with all 0 values
    minidf=df.sample(n=10)
    columns = minidf.columns
    for i in columns[1:]:
        if minidf[i].sum() == 0:
            df = df.drop(i, axis=1)
    
    return df
    
    
def getFiles(path="gpuData.csv"):
    '''
    A function to read the data from a file and return a dataframe.
    Args:
        path: a string containing the path to the file
    Returns:
        df: a dataframe containing the data from the file
    Examples:
        >>> df = getFiles(path)
    '''
    
    try:
        file = open(path,"r")
        df = pd.read_csv(file)
    except FileNotFoundError:
        print('File not found')
        exit()
    
    return df
    
    
    
    
def main():
    
    df = getFiles("C:\\Users\\amart\\Downloads\\GPU-Z Sensor Log.txt")    
    df = cleanData(df)
    df.to_csv('gpuData.csv', index=False)
    # df=pd.read_csv('gpuData.csv')
    
    #create a mini df with ~1000 rows
    minidf=df[0:df.shape[0]:df.shape[0]//1000+1]
    columns = minidf.columns
    for i in columns[1:]:
        print(i,': ',minidf[i].max(),minidf[i].mean().round(2),minidf[i].min())
   
    

if __name__ == '__main__':
    main()
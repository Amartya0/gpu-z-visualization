import pandas as pd


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
    
    
    return df
    
    
def main():
    try :
        df = pd.read_csv('gpuData.csv')
        
    except FileNotFoundError:
        print('File not found')
        exit()
        
    df = cleanData(df)
    df.to_csv('gpuData.csv', index=False)
    
    

if __name__ == '__main__':
    main()
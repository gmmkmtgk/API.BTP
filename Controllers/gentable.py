import pandas as pd

def gen():
    df1 = pd.read_csv (r'./Prices/today.csv')
    df1 = df1.loc[:, 'SYMBOL':'CLOSE']


    df2 = pd.read_csv (r'./Prices/week.csv')
    df2 = df2.loc[:, 'SYMBOL':'CLOSE']

    df3 = pd.read_csv (r'./Prices/month.csv')
    df3 = df3.loc[:, 'SYMBOL':'CLOSE']

    df4 = pd.read_csv (r'./Prices/threemonth.csv')
    df4 = df4.loc[:, 'SYMBOL':'CLOSE']

    df5 = pd.read_csv (r'./Prices/sixmonth.csv')
    df5 = df5.loc[:, 'SYMBOL':'CLOSE']

    df6 = pd.read_csv (r'./Prices/year.csv')
    df6 = df6.loc[:, 'SYMBOL':'CLOSE']

    df1.drop('SERIES', inplace=True, axis=1)
    df2.drop('SERIES', inplace=True, axis=1)
    df1.drop('OPEN', inplace=True, axis=1)
    df2.drop('OPEN', inplace=True, axis=1)
    df1.drop('HIGH', inplace=True, axis=1)
    df2.drop('HIGH', inplace=True, axis=1)
    df1.drop('LOW', inplace=True, axis=1)
    df2.drop('LOW', inplace=True, axis=1)

    df3.drop('SERIES', inplace=True, axis=1)
    df3.drop('OPEN', inplace=True, axis=1)
    df3.drop('HIGH', inplace=True, axis=1)
    df3.drop('LOW', inplace=True, axis=1)

    df4.drop('SERIES', inplace=True, axis=1)
    df4.drop('OPEN', inplace=True, axis=1)
    df4.drop('HIGH', inplace=True, axis=1)
    df4.drop('LOW', inplace=True, axis=1)

    df5.drop('SERIES', inplace=True, axis=1)
    df5.drop('OPEN', inplace=True, axis=1)
    df5.drop('HIGH', inplace=True, axis=1)
    df5.drop('LOW', inplace=True, axis=1)

    df6.drop('SERIES', inplace=True, axis=1)
    df6.drop('OPEN', inplace=True, axis=1)
    df6.drop('HIGH', inplace=True, axis=1)
    df6.drop('LOW', inplace=True, axis=1)

    df1 = df1.rename(columns={'CLOSE': 'tp'}) 
    df2 = df2.rename(columns={'CLOSE': 'wp'}) 
    df3 = df3.rename(columns={'CLOSE': 'mp'}) 
    df4 = df4.rename(columns={'CLOSE': 'tmp'}) 
    df5 = df5.rename(columns={'CLOSE': 'smp'}) 
    df6 = df6.rename(columns={'CLOSE': 'yp'}) 

    df_inner = pd.merge(df1, df2, on='SYMBOL', how='inner')
    df_inner = pd.merge(df_inner,df3, on='SYMBOL', how='inner')
    df_inner = pd.merge(df_inner,df4, on='SYMBOL', how='inner')
    df_inner = pd.merge(df_inner,df5, on='SYMBOL', how='inner')
    df_inner = pd.merge(df_inner,df6, on='SYMBOL', how='inner')


    return df_inner


from typing import final
import pandas as pd
import numpy as np

df = pd.read_csv('~/Documents/Historicaldata/test_data/test.csv')

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

#define indicators
def MACD(DF,a,b,c):
    df = DF.copy()
    df['MA FAST'] = df['Close'].ewm(span=a, adjust=False, min_periods=a).mean()
    df['MA SLOW'] = df['Close'].ewm(span=b, adjust=False, min_periods=b).mean()
    df['MACD'] = df['MA FAST'] - df['MA SLOW']
    df['MACD_S'] = df['MACD'].ewm(span=c, adjust=False, min_periods=c).mean()  
    df['MACD_H'] = df['MACD'] - df['MACD_S']
    df.dropna(inplace=True)
    return df

df2 = MACD(df,12,26,9)

final_df = df2.reindex(['Date','Open','High','Low','Close',
'Adj Close','Volume','MACD','MACD_S','MACD_H','Buy Signal','Sell Signal'], axis=1)

#trading strategy
def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1
   
    for i in range(0, len(signal)):
        if signal['MACD'][i] > signal['MACD_S'][i]:
            Sell.append(np.nan)
            if flag != 1:
                Buy.append(signal['Close'][i])
                flag = 1
            else:
                Buy.append(np.nan)
        elif signal['MACD'][i] < signal['MACD_S'][i]:
            Buy.append(np.nan)
            if flag != 0:
                Sell.append(signal['Close'][i])
                flag = 0
            else:
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)
    
    return (Buy, Sell)


position = buy_sell(final_df)
final_df['Buy Signal'] = position[0]
final_df['Sell Signal'] = position[1]

print(final_df)


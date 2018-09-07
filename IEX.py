
import time
import pandas as pd
 
Ticker = 'MSFT'
Today  = int(time.strftime("%Y%m%d"))
Url = 'https://api.iextrading.com/1.0/stock/' + Ticker +'/chart/date/' + str(Today)

Data = pd.DataFrame(pd.read_json(Url))
Data = Data.dropna()
Data['date'] = Data['date'].map(str) + '-' + Data['label']
Data.set_index('date', inplace=True)
Data = Data[['open','high','low','close','volume']]


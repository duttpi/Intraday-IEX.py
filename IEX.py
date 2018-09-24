
import pandas as pd
from pandas.tseries.offsets import BDay

def IEX(Days, Ticker):
    Date = []
    today = pd.datetime.today()
    for n in range (0, Days):
        x = (today - BDay(n)).strftime('%Y%m%d')
        Date.append(x)

    global Data
    Data = pd.DataFrame()
    for n in range (0, Days):
        Url = 'https://api.iextrading.com/1.0/stock/'+Ticker+'/chart/date/'+str(Date[n])
        Df = pd.DataFrame(pd.read_json(Url))
        Df = Df.dropna()
        Df['date'] = Df['date'].map(str) + '-' + Df['label']
        Df.set_index('date', inplace=True)
        Df.index = pd.to_datetime(Df.index)
        Df = Df[['open','high','low','close','volume']]
        Df.columns = ['Open','High','Low','Close','Volume']
        Data = Data.append(Df, ignore_index=False)

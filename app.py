from config import client
from functions import get_data_since, get_file_data
import backtrader as bt
from teststrategies import SmaCross, TestStrategy
from SandD_strat import SupplyAndDemand
import datetime as dt
import pandas as pd

# Choose to download(1) or use already downloaded data(0)
download = 0

# Both in seconds
startTime = (dt.datetime(2021, 11, 20)).timestamp()
# endTime = (dt.datetime(2022, 10, 28)).timestamp()
endTime = dt.datetime.now().timestamp()

stop = 0.02
target = 0.04

ticker = "MATICUSDT"
tf = "1m"

#---------------------#

df = get_data_since(ticker, tf, startTime, endTime) if download else get_file_data('price_data.csv')

print(df)

cerebro = bt.Cerebro()
feed = bt.feeds.PandasData(dataname=df)
cerebro.adddata(feed)
cerebro.addstrategy(SupplyAndDemand)

cerebro.broker.setcash(1000)

cerebro.addsizer(bt.sizers.PercentSizer, percents=10)

cerebro.run()
cerebro.plot(style="candlestick", fmt_x_data = '%Y-%b-%d %H:%M')

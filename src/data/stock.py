

# ID是申请时所填写的手机号；Password为聚宽官网登录密码
# 上海证券交易所	.XSHG	600519.XSHG	贵州茅台
# 深圳证券交易所	.XSHE	000001.XSHE	平安银行
import time
import pandas as pd
from jqdatasdk import *
auth('15950505889', 'Wq85807012')

# 设置行列不忽略,为了展示打印的数据列不隐藏
pd.set_option('display.max_rows',100000)
pd.set_option('display.max_columns',10)

# 获取股票行情数据
# df = get_price('000001.XSHE', end_date='2021-02-22', count=30, frequency='daily',fq='none')
# df = get_price('000001.XSHE', end_date='2021-02-22', count=30, frequency='1m',fq='none')
# print(df)

#将所有股票列表转换成数组
# stocks = list(get_all_securities(['stock']).index)

# 获取所有股票数据
# df = get_all_securities(types=['stock'], date=None)

# 获取所有A股的行情数据,将 types:stock 替换成stocks变量也行
# df = get_price(['000001.XSHE','600519.XSHG'], end_date='2021-02-22', count=30, frequency='daily',fq='none')
# for stockCode in stocks:
#   print('正在获取股票行情数据，股票代码：',stockCode)
#   df = get_price(stockCode, end_date='2021-02-22', count=10, frequency='daily',fq='none')
#   print(df)
#   time.sleep(3)

'''resample函数的使用'''
# 转换周期: 日K转换为周K, weekday 0 是周一的意思
# df = get_price('000001.XSHE', end_date='2021-02-22', count=20, frequency='daily',fq='none') #获取日K
# df['weekday'] = df.index.weekday
# print(df)

# 获取周K(当周的)：开盘价（当周第一天） 、 收盘价（当周最后一天）、最高价（当周）、最低价（当周）
# df_week = pd.DataFrame()
# df_week['open'] = df['open'].resample('W').first()
# df_week['close'] = df['close'].resample('W').last()
# df_week['high'] = df['high'].resample('W').max()
# df_week['low'] = df['low'].resample('W').min()

#汇总统计：统计一下成交量、成交额(sum)
# df_week['volume(sum)'] = df['volume'].resample('W').sum()
# df_week['money(sum)'] = df['money'].resample('W').sum()
# print(df_week)

'''获取股票财务指标'''
df = get_fundamentals(query(indicator),statDate='2020')
# print(df)
df.to_csv('src/data/finance/finance2020.csv')

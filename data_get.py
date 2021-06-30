# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@E-mail: chenmx19@mails.tsinghua.edu.cn
@description:
@revise log:
"""

import pandas as pd
import numpy as np
import os,re
from WindPy import *
w.start()
import datetime
import time
import inspect
import warnings
warnings.filterwarnings('ignore')

#%%
def relationship_nav(data):
    data.reset_index(inplace=True)
    data.drop(['基金代码', '基金名称'], axis=1, inplace=True)
    data = data.apply(lambda x: x.replace('--', np.nan))
    data['净值日期'] = data['净值日期'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))
    # data['净值日期']=pd.to_datetime(data['净值日期'])
    # data['净值日期']=data['净值日期'].dt.strftime("%Y-%m-%d")
    data.set_index('净值日期', inplace=True)
    data = data.sort_index()
    def Ifequal(a, b):
        if a == b:
            return 1
        else:
            return np.nan

    data['if_equal'] = data.apply(lambda x: Ifequal(x['单位净值(元)'], x['累计净值(元)']), axis=1)
    print('单位净值与累计净值不同的日期为'%data['if_equal'].isnull().sum()+'天')
    df = data.copy()
    df.drop(['日涨跌', '累计净值(元)', '资产净值(元)', 'if_equal'], axis=1, inplace=True)
    df.reset_index(inplace=True)
    df.columns = ['date', 'net_value']
    df.set_index('date', inplace=True)
    return df

#%%
def function_gen(Index):
    functions = inspect.getmembers(Index, lambda x: inspect.isfunction(x))
    functions = list(filter(lambda x: not x[0].startswith('__'), functions))
    functions = list(functions[x][0] for x in range(len(functions)))
    for i in ['case_to_function','case_fun_other','YearProcess','calcHurst2']:
        if i in functions:
            functions.remove(i)
    print(functions)
    return functions

#%%
def data_load(index,begin_date,end_date):
    fundid = index[:-3]
    df=pd.read_excel('./data/%s'%fundid+'_netvalue.xls',index_col=0)
    df.reset_index(inplace=True)
    df.drop(['基金代码','基金名称'],axis=1,inplace=True)
    df=df.apply(lambda x:x.replace('--',np.nan))
    df['净值日期']=df['净值日期'].apply(lambda x:datetime.datetime.strptime(str(x),"%Y-%m-%d"))
    df.sort_values(by='净值日期',inplace=True)
    df.drop(['日涨跌','累计净值(元)','资产净值(元)'],axis=1,inplace=True)
    df.columns=['date','net_value']
    df['year'] = df.apply(lambda x: x.date.year,axis=1)
    df['month'] = df.apply(lambda x: x.date.month,axis=1)
    df['no'] = range(len(df.index))

    isExists_benchmark = os.path.exists('./data/benchmark_df.csv')
    isExists_ben = os.path.exists('./data/ben.csv')
    if not isExists_benchmark:


        if not isExists_ben:
            nav = w.wsd(index, "nav", begin_date, end_date, "")
            fund_benchmark = w.wsd(index, "fund_benchmark", begin_date, end_date, "")
            fund_changeofbenchmark = w.wsd(index, "fund_changeofbenchmark", begin_date, end_date, "")
            fund_benchindexcode = w.wsd(index, "fund_benchindexcode", begin_date, end_date, "")
            nav = pd.DataFrame(np.array(nav.Data).T, columns=nav.Codes, index=nav.Times)
            fund_benchmark = pd.DataFrame(np.array(fund_benchmark.Data).T, columns=fund_benchmark.Codes, index=fund_benchmark.Times)
            fund_changeofbenchmark = pd.DataFrame(np.array(fund_changeofbenchmark.Data).T, columns=fund_changeofbenchmark.Codes, index=fund_changeofbenchmark.Times)
            fund_benchindexcode = pd.DataFrame(np.array(fund_benchindexcode.Data).T, columns=fund_benchindexcode.Codes, index=fund_benchindexcode.Times)
            ben = pd.concat([nav, fund_benchmark, fund_changeofbenchmark, fund_benchindexcode], axis=1)
            ben.columns = ['nav', 'fund_benchmark', 'fund_changeofbenchmark', 'fund_benchindexcode']
        else:
            ben = pd.read_csv('./data/ben.csv', index_col=0)
        ben_final=ben.drop_duplicates(subset=['fund_benchmark'],keep='first')
        close = w.wsd(index, "close", begin_date, end_date, "")
        benchmark = w.wsd(ben_final['fund_benchindexcode'].iloc[0], "nav", begin_date, end_date, "")
        close = pd.DataFrame(np.array(close.Data).T, columns=close.Codes, index=close.Times)
        benchmark = pd.DataFrame(np.array(benchmark.Data).T, columns=benchmark.Codes, index=benchmark.Times)
        benchmark_df = pd.concat([close, benchmark], axis=1)
        benchmark_df.columns = ['close', 'benchmark']
        if  benchmark_df['benchmark'].iloc[-1]==None:
            print(ben_final['fund_benchmark'].iloc[0])
            ben_name = ben_final['fund_benchmark'].iloc[0].split('+')
            ben_1 = w.wsd('000942.CSI', "close", begin_date, end_date, "")    #  中证内地消费主题指数收益率*85%
            ben_2 = w.edb("M0051553", begin_date, end_date,"Fill=Previous")  #   +中债总指数收益率*15%
            ben_1 = pd.DataFrame(np.array(ben_1.Data).T, columns=ben_1.Codes, index=ben_1.Times)
            ben_1 = ben_1.apply(lambda x: x/x.iloc[0])

            ben_2 = pd.DataFrame(np.array(ben_2.Data).T, columns=ben_2.Codes, index=ben_2.Times)
            ben_2 = ben_2.apply(lambda x: x/x.iloc[0])
            benchmark_df = pd.concat([ben_1, ben_2], axis=1)
            benchmark_df.reset_index(inplace=True)
            benchmark_df.columns = ['date','ben_1', 'ben_2']
            benchmark_df.fillna(method='ffill',inplace=True)
            benchmark_df['benchmark'] =  benchmark_df['ben_1']*float(ben_name[0].split('*')[1][:-1])/100+\
                                         benchmark_df['ben_2']*float(ben_name[1].split('*')[1][:-1])/100

            benchmark_df.to_csv('./data/benchmark_df.csv', encoding='utf8')
    else:
        benchmark_df = pd.read_csv('./data/benchmark_df.csv', index_col=0)

    isExists_rf = os.path.exists('./data/rf.csv')
    if not isExists_rf:

        rf = w.edb("M0325687",begin_date, end_date,"Fill=Previous") # MM0325687 从wind宏观数据库中提取十年期国债收益率数据
        rf = pd.DataFrame(np.array(rf.Data).T, columns=rf.Codes, index=rf.Times)
        rf = rf.apply(lambda x: x/100, axis=1)
        rf.reset_index(inplace=True)
        rf.columns=['date','rf']
        rf.to_csv('./data/rf.csv', encoding='utf8')
    else:
        rf = pd.read_csv('./data/rf.csv', index_col=0)


    isExists_market = os.path.exists('./data/market.csv')
    if not isExists_market:

        market = w.wsd('000985.CSI', "close", begin_date, end_date, "") # 中证全指 # 万得全A '881001.WI'
        market = pd.DataFrame(np.array(market.Data).T, columns=market.Codes, index=market.Times)
        market.reset_index(inplace=True)
        market.columns=['date','market']
        # 给出的市场组合的净值数据
        # market['cumret'] = market['market'].apply(lambda x: (x- market.iloc[0, 1]) / market.iloc[0, 1])
        market.to_csv('./data/market.csv', encoding='utf8')
    else:
        market = pd.read_csv('./data/market.csv', index_col=0)


    rf['date'] = rf['date'].apply(lambda x:datetime.datetime.strptime(str(x),"%Y-%m-%d"))
    benchmark_df['date'] = benchmark_df['date'].apply(lambda x:datetime.datetime.strptime(str(x),"%Y-%m-%d"))
    benchmark_df.drop(['ben_1', 'ben_2'], axis=1, inplace=True)
    market['date'] = market['date'].apply(lambda x:datetime.datetime.strptime(str(x),"%Y-%m-%d"))

    df_with_rf = pd.merge(df,rf,on='date')
    df_with_rf['net_value'] = df_with_rf['net_value'].apply(lambda x: x / df_with_rf['net_value'].iloc[0])

    df_with_ben = pd.merge(df,benchmark_df,on='date')
    df_with_ben['net_value'] = df_with_ben['net_value'].apply(lambda x: x / df_with_ben['net_value'].iloc[0])
    df_with_ben['benchmark'] = df_with_ben['benchmark'].apply(lambda x: x / df_with_ben['benchmark'].iloc[0])

    df_with_rf_ben = pd.merge(df_with_rf,benchmark_df,on='date')
    df_with_rf_ben['net_value'] = df_with_rf_ben['net_value'].apply(lambda x: x / df_with_rf_ben['net_value'].iloc[0])
    df_with_rf_ben['benchmark'] = df_with_rf_ben['benchmark'].apply(lambda x: x / df_with_rf_ben['benchmark'].iloc[0])

    df_with_rf_market = pd.merge(df_with_rf,market,on='date')
    df_with_rf_market['net_value'] = df_with_rf_market['net_value'].apply(lambda x: x / df_with_rf_market['net_value'].iloc[0])
    df_with_rf_market['market'] = df_with_rf_market['market'].apply(lambda x: x / df_with_rf_market['market'].iloc[0])


    df_with_rf_market_ben = pd.merge(df_with_rf_market,benchmark_df,on='date')
    df_with_rf_market_ben['net_value'] = df_with_rf_market_ben['net_value'].apply(lambda x: x / df_with_rf_market_ben['net_value'].iloc[0])
    df_with_rf_market_ben['market'] = df_with_rf_market_ben['market'].apply(lambda x: x / df_with_rf_market_ben['market'].iloc[0])
    df_with_rf_market_ben['benchmark'] = df_with_rf_market_ben['benchmark'].apply(lambda x: x/df_with_rf_market_ben['benchmark'].iloc[0])


    return df, df_with_rf,df_with_ben, df_with_rf_market,df_with_rf_ben, df_with_rf_market_ben, rf, market, benchmark_df




#%%
def holding_data(index,report_date):
    data = w.wset("allfundhelddetail","rptdate=%s"%report_date+";windcode=%s"%index).Data
    df = pd.DataFrame([data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]]).T
    df.index = data[0]
    df.columns = ['rpt_date','stock_code','stock_name','marketvalueofstockholdings','hold_number','proportiontototalstockinvestment','proportiontonetvalue',
                  'proportiontoshareholdtocirculation','quarter_changing']
    # 名称、报告期、股票代码、股票简称、持股市值（万元）、持股数量（万股）、占股票投资市值比、占净值比、持股占流通股比、半年度持股变动（万股）
    df['proportiontototalstockinvestment'] = df['proportiontototalstockinvestment'].apply(lambda x: x/100)
    df['proportiontonetvalue'] = df['proportiontonetvalue'].apply(lambda x: x / 100)
    df['proportiontoshareholdtocirculation'] = df['proportiontoshareholdtocirculation'].apply(lambda x: x / 100)
    # df.sort_values(by='proportion',ascending=False)
    return df

# hold2020 = holding_data('110022.OF','2020-06-30')
# holding_detail = pd.read_excel('./data/holding_detail.xlsx',index_col=0,sheet_name='20201231')
# holding_detail = holding_detail.iloc[5:]
# holding_detail.columns=['报告期','股票代码','股票简称','持股市值(万元)','持股数量(万股)','占股票投资市值比(%)','占净值比(%)',
#                         '持股占流通股比(%)','半年度持股变动(万股)','所属申万行业名称','所属申万行业代码','半年期涨跌幅']

#%%
def holding_class_data(index,report_date):
    data = w.wss("%s"%index, "prt_stocktonav,prt_bondtonav,prt_cashtonav,prt_othertonav","rptDate=%s"%report_date).Data
    df = pd.DataFrame([data[0], data[1], data[2], data[3]]).T
    df.index = [report_date]
    df.columns = ['股票投资市值占基金资产净值比', '债券投资市值占基金资产净值比', '银行存款占基金资产净值比', '其他资产占基金资产净值比']
    return df
def holding_class_data2(index,report_date):
    data2 = w.wss("%s" % index, "prt_stockvalue,prt_bondvalue,prt_cash,prt_other",
                 "rptDate=%s" % report_date).Data
    df2 = pd.DataFrame([data2[0], data2[1], data2[2], data2[3]]).T
    df2.index = [report_date]
    df2.columns = ['股票投资市值', '债券投资市值', '银行存款', '其他资产']
    return df2

holding_class_df = pd.concat([holding_class_data('110022.OF', '2010-12-31'),
           # holding_class_data('110022.OF', '2011-03-31'),
           holding_class_data('110022.OF', '2011-06-30'),
           # holding_class_data('110022.OF', '2011-09-30'),
           holding_class_data('110022.OF', '2011-12-31'),
           # holding_class_data('110022.OF', '2012-03-31'),
           holding_class_data('110022.OF', '2012-06-30'),
           # holding_class_data('110022.OF', '2012-09-30'),
           holding_class_data('110022.OF', '2012-12-31'),
           # holding_class_data('110022.OF', '2013-03-31'),
           holding_class_data('110022.OF', '2013-06-30'),
           # holding_class_data('110022.OF', '2013-09-30'),
           holding_class_data('110022.OF', '2013-12-31'),
           # holding_class_data('110022.OF', '2014-03-31'),
           holding_class_data('110022.OF', '2014-06-30'),
           # holding_class_data('110022.OF', '2014-09-30'),
           holding_class_data('110022.OF', '2014-12-31'),
           # holding_class_data('110022.OF', '2015-03-31'),
           holding_class_data('110022.OF', '2015-06-30'),
           # holding_class_data('110022.OF', '2015-09-30'),
           holding_class_data('110022.OF', '2015-12-31'),
           # holding_class_data('110022.OF', '2016-03-31'),
           holding_class_data('110022.OF', '2016-06-30'),
           # holding_class_data('110022.OF', '2016-09-30'),
           holding_class_data('110022.OF', '2016-12-31'),
           # holding_class_data('110022.OF', '2017-03-31'),
           holding_class_data('110022.OF', '2017-06-30'),
           # holding_class_data('110022.OF', '2017-09-30'),
           holding_class_data('110022.OF', '2017-12-31'),
           # holding_class_data('110022.OF', '2018-03-31'),
           holding_class_data('110022.OF', '2018-06-30'),
           # holding_class_data('110022.OF', '2018-09-30'),
           holding_class_data('110022.OF', '2018-12-31'),
           # holding_class_data('110022.OF', '2019-03-31'),
           holding_class_data('110022.OF', '2019-06-30'),
           # holding_class_data('110022.OF', '2019-09-30'),
           holding_class_data('110022.OF', '2019-12-31'),
           # holding_class_data('110022.OF', '2020-03-31'),
           holding_class_data('110022.OF', '2020-06-30'),
           # holding_class_data('110022.OF', '2020-09-30'),
           holding_class_data('110022.OF', '2020-12-31'),
           # holding_class_data('110022.OF', '2021-03-31'),
           ])
#%%
holding_class_df2 = pd.concat([holding_class_data2('110022.OF', '2010-12-31'),
                              # holding_class_data2('110022.OF', '2011-03-31'),
                              holding_class_data2('110022.OF', '2011-06-30'),
                              # holding_class_data2('110022.OF', '2011-09-30'),
                              holding_class_data2('110022.OF', '2011-12-31'),
                              # holding_class_data2('110022.OF', '2012-03-31'),
                              holding_class_data2('110022.OF', '2012-06-30'),
                              # holding_class_data2('110022.OF', '2012-09-30'),
                              holding_class_data2('110022.OF', '2012-12-31'),
                              # holding_class_data2('110022.OF', '2013-03-31'),
                              holding_class_data2('110022.OF', '2013-06-30'),
                              # holding_class_data2('110022.OF', '2013-09-30'),
                              holding_class_data2('110022.OF', '2013-12-31'),
                              # holding_class_data2('110022.OF', '2014-03-31'),
                              holding_class_data2('110022.OF', '2014-06-30'),
                              # holding_class_data2('110022.OF', '2014-09-30'),
                              holding_class_data2('110022.OF', '2014-12-31'),
                              # holding_class_data2('110022.OF', '2015-03-31'),
                              holding_class_data2('110022.OF', '2015-06-30'),
                              # holding_class_data2('110022.OF', '2015-09-30'),
                              holding_class_data2('110022.OF', '2015-12-31'),
                              # holding_class_data2('110022.OF', '2016-03-31'),
                              holding_class_data2('110022.OF', '2016-06-30'),
                              # holding_class_data2('110022.OF', '2016-09-30'),
                              holding_class_data2('110022.OF', '2016-12-31'),
                              # holding_class_data2('110022.OF', '2017-03-31'),
                              holding_class_data2('110022.OF', '2017-06-30'),
                              # holding_class_data2('110022.OF', '2017-09-30'),
                              holding_class_data2('110022.OF', '2017-12-31'),
                              # holding_class_data2('110022.OF', '2018-03-31'),
                              holding_class_data2('110022.OF', '2018-06-30'),
                              # holding_class_data2('110022.OF', '2018-09-30'),
                              holding_class_data2('110022.OF', '2018-12-31'),
                              # holding_class_data2('110022.OF', '2019-03-31'),
                              holding_class_data2('110022.OF', '2019-06-30'),
                              # holding_class_data2('110022.OF', '2019-09-30'),
                              holding_class_data2('110022.OF', '2019-12-31'),
                              # holding_class_data2('110022.OF', '2020-03-31'),
                              holding_class_data2('110022.OF', '2020-06-30'),
                              # holding_class_data2('110022.OF', '2020-09-30'),
                              holding_class_data2('110022.OF', '2020-12-31'),
                              # holding_class_data2('110022.OF', '2021-03-31'),
                              ])


#%%

# def report_date_list_gen(start_date,end_date):
#     start_date = datetime.datetime.strptime(str(start_date),"%Y-%m-%d")
#     end_date = datetime.datetime.strptime(str(end_date), "%Y-%m-%d")
#     start_date_quarter = (start_date.month-1)/3+1
#     if start_date_quarter == 1:
#         begin = datetime.datetime(start_date.year,3,1),datetime.datetime(start_date.year,3,31)
#     elif start_date_quarter == 2:
#         begin = datetime.datetime(start_date.year,6,1),datetime.datetime(start_date.year,6,30)
#     elif start_date_quarter == 3:
#         begin = datetime.datetime(start_date.year,9,1),datetime.datetime(start_date.year,9,30)
#     else:
#         begin = datetime.datetime(start_date.year,12,1),datetime.datetime(start_date.year,12,31)
#     end_date_quarter = (end_date.month-1)/3+1
#     if end_date_quarter == 1:
#         end = datetime.datetime(end_date.year,3,1),datetime.datetime(end_date.year,3,31)
#     elif end_date_quarter == 2:
#         end = datetime.datetime(end_date.year,6,1),datetime.datetime(end_date.year,6,30)
#     elif end_date_quarter == 3:
#         end = datetime.datetime(end_date.year,9,1),datetime.datetime(end_date.year,9,30)
#     else:
#         end = datetime.datetime(end_date.year,12,1),datetime.datetime(end_date.year,12,31)
#
#     year_list = []
#     for i in [start_date.year,end_date.year]:
#         year_list.append(i)
#
#     report_date_list = []
#     while begin < end:
#         report_date_list.append
#
#     while begin < end:
#         # 日期叠加一天
#         datestart += datetime.timedelta(days=+1)
#         # 日期转字符串存入列表
#         date_list.append(datestart.strftime('%Y-%m-%d'))
#     print(date_list)


#%%
def getq(day):
    '''
    收入一个日期，得到其所处的报告期的日期
    :param day:
    :return:
    '''
    quarter = (day.month-1)/3+1
    if quarter == 1:
        return datetime.datetime(day.year,3,1),datetime.datetime(day.year,3,31)
    elif quarter == 2:
        return datetime.datetime(day.year,6,1),datetime.datetime(day.year,6,30)
    elif quarter == 3:
        return datetime.datetime(day.year,9,1),datetime.datetime(day.year,9,30)
    else:
        return datetime.datetime(day.year,12,1),datetime.datetime(day.year,12,31)

# getq(datetime.datetime.strptime("2016-07-01","%Y-%m-%d"))
# start_date = str(getq(datetime.datetime.strptime("2016-07-01","%Y-%m-%d"))[0])[:10]
# end_date =  str(getq(datetime.datetime.strptime("2016-07-01","%Y-%m-%d"))[1])[:10]

#%%


def holding_load(para,df):
    isExists_holding = os.path.exists('./data/holding.csv')
    if not isExists_holding:
        holding_list = []
        holding_arr = np.array()
        df['holding_report_date'] = df['date'].apply(lambda x: str(getq(x)[1])[:10])
        holding_report_date = df['holding_report_date'].drop_duplicates().tolist()
        for end_date in holding_report_date[:-2]:

            print(end_date)
            holding_arr = np.vstack((holding_arr,np.array(holding_data(para, end_date))))
            # holding_list.append(holding_data(para, end_date))
        holding = np.array(holding_list)
        np.save('./data/holding.npy',holding)
    else:
        holding = np.load('./data/holding.npy')
    return holding


# holding_list = []
# for date_i in df.date:
#     print(date_i)
#     end_date = str(getq(date_i)[1])[:10]
#     holding_list.append(holding_data(para, end_date))
# holding = np.array(holding_list)
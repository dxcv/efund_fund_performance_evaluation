# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@E-mail: chenmx19@mails.tsinghua.edu.cn
@description:
@revise log:
"""

import pandas as pd
import numpy as np
import os, re
from WindPy import *

w.start()
import datetime
import time
import inspect
import warnings

warnings.filterwarnings('ignore')


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

def china_bond_ret(begin_date,end_date):
    ben_2 = w.edb("M0051553", begin_date, end_date, "Fill=Previous").Data[0]
    return (ben_2[-1]-ben_2[0])/ben_2[0]

def bench_index_ret(begin_date,end_date):
    ben_1 = w.wsd('000942.CSI', "close", begin_date, end_date, "").Data[0]
    return (ben_1[-1]-ben_1[0])/ben_1[0]


#%%
def Brinson(holding, bench_holding, method='simple'):
    rp_stock = holding['半年期涨跌幅'].iloc[:-1]
    rp_cash = bench_holding[bench_holding['股票代码']=='M0051553']['半年期涨跌幅'].iloc[0]
    wp_stock = holding['占净值比(%)'].iloc[:-1]
    wp_cash = holding['占净值比(%)'].iloc[-1]
    rb_stock = holding['基准的半年涨跌幅'].iloc[:-1]
    rb_cash = bench_holding[bench_holding['股票代码']=='M0051553']['半年期涨跌幅'].iloc[0]
    wb_stock = holding['wb'].iloc[:-1]
    wb_cash = holding['wb'].iloc[-1]
    if method == 'simple':
        ben_ret = (rb_stock*wb_stock).sum()+rb_cash*wb_cash
        select_ret = ((rp_stock-rb_stock)*wb_stock).sum() + (rp_cash-rb_cash)*wb_cash
        alloca_ret = ((wp_stock-wb_stock)*rb_stock).sum() + (wp_cash-wb_cash)*rb_cash
        interse_ret = ((rp_stock-rb_stock)*(wp_stock-wb_stock)).sum() + ((rp_cash-rb_cash)*(wp_cash-wb_cash))
        print(ben_ret, select_ret, alloca_ret, interse_ret)
        return pd.Series([ben_ret, select_ret, alloca_ret, interse_ret])
    elif method == 'multiple':
        factor_stock = holding['Ft'].iloc[:-1]
        ben_ret = (factor_stock*(rb_stock*wb_stock)).sum()+rb_cash*wb_cash
        select_ret = ((rp_stock-rb_stock)*wb_stock*factor_stock).sum() + (rp_cash-rb_cash)*wb_cash
        alloca_ret = ((wp_stock-wb_stock)*rb_stock*factor_stock).sum() + (wp_cash-wb_cash)*rb_cash
        interse_ret = ((rp_stock-rb_stock)*(wp_stock-wb_stock)*factor_stock).sum() + ((rp_cash-rb_cash)*(wp_cash-wb_cash))
        print(ben_ret, select_ret, alloca_ret, interse_ret)
        return pd.Series([ben_ret, select_ret, alloca_ret, interse_ret])



#%%
def Brinson_stock(holding, method='simple'):
    rp_stock = holding['半年期涨跌幅'].iloc[:-1]
    wp_stock = holding['占净值比(%)'].iloc[:-1]
    rb_stock = holding['基准的半年涨跌幅'].iloc[:-1]
    wb_stock = holding['wb'].iloc[:-1]
    factor_stock = holding['Ft'].iloc[:-1]

    if method == 'simple':
        ben_ret = (rb_stock * wb_stock).sum()
        select_ret = ((rp_stock - rb_stock) * wb_stock).sum()
        alloca_ret = ((wp_stock - wb_stock) * rb_stock).sum()
        interse_ret = ((rp_stock - rb_stock) * (wp_stock - wb_stock)).sum()
    elif method == 'multiple':
        factor_stock = holding['Ft'].iloc[:-1]
        ben_ret = (factor_stock * (rb_stock * wb_stock)).sum()
        select_ret = ((rp_stock - rb_stock) * wb_stock * factor_stock).sum()
        alloca_ret = ((wp_stock - wb_stock) * rb_stock * factor_stock).sum()
        interse_ret = ((rp_stock - rb_stock) * (wp_stock - wb_stock) * factor_stock).sum()
    else:
        pass
    return pd.Series([ben_ret, select_ret, alloca_ret, interse_ret])

#%%
def cal_k(stock_id,report_date_last,report_date):
    data = w.wsd(stock_id, "pct_chg", report_date_last, report_date, "").Data[0]
    industry_id = w.wss("%s"%stock_id, "indexcode_sw","tradeDate=%s"%report_date+";industryType=1").Data[0][0]
    data2 = w.wsd("%s" % industry_id, "pct_chg", report_date_last, report_date, "").Data[0]
    df = pd.DataFrame([data,data2]).T
    df.columns=['rp','rb']
    df['rp'] = df['rp'].apply(lambda x: x / 100)
    df['rb'] = df['rb'].apply(lambda x: x / 100)
    df['ft'] = df.apply(lambda x: (np.log(1+x.rp)-np.log(1+x.rb))/(x.rp-x.rb),axis=1)
    RP = w.wss("%s"%stock_id, "pct_chg_per","startDate=%s"%report_date_last+";endDate=%s"%report_date).Data[0][0]/100
    if type(industry_id) == str:
        RB = w.wss("%s" % industry_id, "pct_chg_per","startDate=%s" % report_date_last + ";endDate=%s" % report_date).Data[0][0]/100
    else:
        RB = bench_index_ret(report_date_last,report_date)
    if type(RP)==float and type(RB)==float:
        Ft = (np.log(1+RP) - np.log(1+RB))/(RP-RB)
        if df['ft'].dropna().mean() ==np.nan:
            return 1
        else:
            return df['ft'].dropna().mean()/Ft
    else:
        return 1
# cal_k('600519.SH', '20200630', '20201231')

#%%
def holding_gen(index,report_date,report_date_last):
    holding_class = pd.concat([holding_class_data(index,report_date),
                               holding_class_data2(index,report_date)],axis=1)

    holding_detail = pd.read_excel('./data/holding_detail.xlsx',index_col=0,sheet_name=report_date_last)
    holding_detail = holding_detail.iloc[5:]
    holding_detail.columns=['报告期','股票代码','股票简称','持股市值(万元)','持股数量(万股)','占股票投资市值比(%)','占净值比(%)',
                            '持股占流通股比(%)','半年度持股变动(万股)','所属申万行业名称','所属申万行业代码','半年期涨跌幅','基准的半年涨跌幅']

    holding = pd.concat([holding_detail['股票代码'],holding_detail['占净值比(%)'],holding_detail['所属申万行业代码'],
                         holding_detail['半年期涨跌幅'],holding_detail['基准的半年涨跌幅']],axis=1)
    holding['占净值比(%)'] = holding['占净值比(%)'].apply(lambda x: x / 100)
    holding['半年期涨跌幅'] = holding['半年期涨跌幅'].apply(lambda x: x / 100)
    holding['基准的半年涨跌幅'] = holding['基准的半年涨跌幅'].apply(lambda x: x / 100)
    holding['基准的半年涨跌幅'].replace(0,china_bond_ret(report_date_last, report_date),inplace=True)
    holding['wb'] = holding['占净值比(%)']/holding['占净值比(%)'].sum()*0.85
    holding['Ft'] = holding.apply(lambda x: cal_k(x['股票代码'], report_date_last, report_date), axis=1)

    bond = pd.DataFrame(['M0051553',
                         1-holding_class['股票投资市值占基金资产净值比'].iloc[0]*0.01,
                         china_bond_ret('20200630', '20201231'),
                         china_bond_ret('20200630', '20201231'),
                         0.15,1],
                        index=['股票代码','占净值比(%)','半年期涨跌幅','基准的半年涨跌幅','wb','Ft']).T
    holding = holding.append(bond)

    bench1 = pd.DataFrame(['M0051553',0.2,china_bond_ret(report_date_last, report_date)],
                        index=['股票代码','占净值比(%)','半年期涨跌幅']).T
    bench2 = pd.DataFrame(['000942.CSI',0.85,bench_index_ret(report_date_last, report_date)],
                        index=['股票代码','占净值比(%)','半年期涨跌幅']).T
    bench_holding = bench1.append(bench2)
    return holding, bench_holding

#%%
result_class = pd.DataFrame()
result_stock = pd.DataFrame()
time_list = ['20110630','20111231','20120630','20121231','20130630','20131231','20140630','20141231','20150630','20151231',
          '20160630','20161231','20170630','20171231','20180630','20181231','20190630','20191231','20200630','20201231']
for i in range(1,len(time_list)):
    print(time_list[i],time_list[i-1])
    holding, bench_holding = holding_gen('110022.OF', time_list[i], time_list[i-1])
    result_class = result_class.append(Brinson(holding, bench_holding,method='multiple'),ignore_index=True)

    result_stock_i = holding.groupby(['所属申万行业代码']).apply(lambda x: Brinson_stock(x,method='multiple'))
    result_stock_i.columns = ['ben_ret', 'select_ret', 'alloca_ret', 'interse_ret']
    result_stock_i['report_date'] = [time_list[i]] *len(result_stock_i)
    result_stock = result_stock.append(result_stock_i)
result_class.index = time_list[1:].copy()
result_class.columns = ['ben_ret', 'select_ret', 'alloca_ret', 'interse_ret']
result_class.to_csv('./result/result_class.csv',encoding='utf_8_sig')
result_stock.to_csv('./result/result_stock.csv',encoding='utf_8_sig')



#%%
# 柱状堆叠图
import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts import options as opt
def stack_bar_plot(df):
    date = df['report_date'].iloc[0]
    df.iloc[:,1:5] = df.iloc[:,1:5].apply(lambda x: round(x,4))
    bar = (
    Bar(init_opts=opts.InitOpts(theme = 'westeros' ))#维斯特洛大陆 # https://www.cnblogs.com/shanger/p/12873645.html
    .add_xaxis(df.iloc[:,0].tolist())
    .add_yaxis('基准收益', df['基准收益'].tolist(), stack='stack1')
    .add_yaxis('选择收益', df['选择收益'].tolist(), stack='stack1')
    .add_yaxis('配置收益', df['配置收益'].tolist(), stack='stack1')
    .add_yaxis('交互收益', df['交互收益'].tolist(), stack='stack1')
    # .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    # 设置标签属性
    .set_series_opts(
        label_opts=opts.LabelOpts(position="inside", color="black", font_size=9, font_style="normal",
                              font_weight='normal', font_family='Times New Roman', formatter="{c}%"))
    .set_global_opts(title_opts=opts.TitleOpts(title='Brinson分解%s'%date),
                     xaxis_opts=opts.AxisOpts(name='申万行业分类'),
                     yaxis_opts=opts.AxisOpts(name='%'))
        )


    bar.render('./result/%s'%date+'_brinson.html')
    make_snapshot(snapshot, bar.render(), './result/%s'%date+'_brinson.png')
#%%
result_class = pd.read_excel('./result/底稿.xlsx',sheet_name = '单期Brinson_final')
stack_bar_plot(result_class)
#%%
result_class2 = pd.read_excel('./result/底稿.xlsx',sheet_name = '多期Brinson_final')
stack_bar_plot(result_class2)
#%%
result_stock = pd.read_excel('./result/底稿.xlsx',sheet_name = '单期Brinson_stock_final')
result_stock.groupby(['报告日']).apply(stack_bar_plot)

#%%
result_stock2 = pd.read_excel('./result/底稿.xlsx',sheet_name = '多期Brinson_stock_final')
result_stock2.groupby(['report_date']).apply(stack_bar_plot)




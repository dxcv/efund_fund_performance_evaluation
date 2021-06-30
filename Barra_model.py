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
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from statsmodels.api import add_constant
import datetime
import time
import inspect
import warnings

warnings.filterwarnings('ignore')

fund_id='110022.OF'
#%%
def shift(df):
    df['ret'].iloc[:-1] = df['ret'].iloc[1:]
    return df
# factor_final2.groupby(['stocknames']).apply(shift)
#%%

def fund_ret(fund_id):
    df=pd.read_excel('./data/%s'%fund_id[:-3]+'_netvalue.xls',index_col=0)
    df.reset_index(inplace=True)
    df.drop(['基金代码','基金名称'],axis=1,inplace=True)
    df=df.apply(lambda x:x.replace('--',np.nan))
    df['净值日期']=df['净值日期'].apply(lambda x:datetime.datetime.strptime(str(x),"%Y-%m-%d"))
    df.sort_values(by='净值日期',inplace=True)
    df.drop(['累计净值(元)','资产净值(元)'],axis=1,inplace=True)
    df.columns=['date','net_value','ret']
    df['ret'] = df['ret'].apply(lambda x: float(x)/100)
    return df

#%%
def factor_gen(stock_id,start_date,end_date):
    gen = w.wsd("%s"%stock_id,
          "windcode,pct_chg, industry_sw, val_pe_deducted_ttm,val_pbindu_sw,ps_ttm, pcf_ocflyr,ev2_to_ebitda,fa_dps, yoy_or,  yoyocf  , yoyprofit ,yoyeps_basic , yoyroe,  grossprofitmargin,netprofitmargin,roe_exdiluted,roa,tech_revs60, val_lnfloatmv, tech_revs120, stdevr,  free_turn_n, risk_beta60,  debttoassets,current,quick,cashtocurrentdebt ",
          # 涨跌幅,申万行业,PE, PB, PS,                                    市现率, 企业价值倍数,每股股利, 营业收入增长率,经营性现金流量增长率,净利润增长率,EPS增长率,ROE增长率,销售毛利率,销售净利率,ROE,ROA,                                     对数流通市值, 过去3个月动量, 收益率标准差,换手率,       beta,       资产负债率、流动比率、速动比率、现金比率
          start_date, end_date, "industryType=1;period=2;returnType=1")
    data = gen.Data
    print(gen)
    df = pd.DataFrame([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],
                       data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18],data[19],
                       data[20], data[21], data[22], data[23], data[24], data[25],data[26]
                       ]).T
    df.columns = ['证券代码','涨跌幅','申万行业','PE', 'PB', 'PS',  '市现率', '企业价值倍数','每股股利', '营业收入增长率','经营性现金流量增长率','净利润增长率','EPS增长率','ROE增长率','销售毛利率','销售净利率','ROE','ROA', '对数流通市值', '过去3个月动量', '收益率标准差','换手率',  'beta', '资产负债率','流动比率','速动比率','现金比率']
    df.index = gen.Times
    df.replace('None', np.nan, inplace=True)
    df.fillna(method='ffill', inplace=True)
    df['涨跌幅'] = df['涨跌幅'].apply(lambda x: float(x)/100)
    return df


#%%
def stocks_gen(fund_id,rptdate):
    data = w.wset("allfundhelddetail", "rptdate="+rptdate+";windcode=%s"%fund_id+";field=,stock_code").Data[0]
    return data


#%%
isExists_factor = os.path.exists('./data/factor.csv')
if not isExists_factor:
    from WindPy import *

    w.start()
    time_list = [
        # '20110630','20111231','20120630','20121231','20130630','20131231','20140630','20141231','20150630','20151231',
        #       '20160630','20161231','20170630','20171231',

                 '20180630','20181231','20190630','20191231','20200630','20201231']
    factor = pd.DataFrame()
    for i in range(1,len(time_list)):
        print(time_list[i],time_list[i-1])
        stock_set = stocks_gen(fund_id,time_list[i-1])
        factor_df = pd.DataFrame()
        for stock_i in stock_set:
            factor_df_i = factor_gen(stock_i,time_list[i-1],time_list[i])
            factor_df = factor_df.append(factor_df_i)
            factor_df.sort_index(inplace=True)
        factor = factor.append(factor_df)
    factor.fillna(0,inplace=True)
    factor.loc[:,'PE':] = StandardScaler().fit_transform(factor.loc[:,'PE':])
    factor['value'] = factor.loc[:,'PE':'每股股利'].apply(lambda x:x.mean(),axis=1)
    factor['growth'] = factor.loc[:,'营业收入增长率':'ROE增长率'].apply(lambda x:x.mean(),axis=1)
    factor['profit'] = factor.loc[:,'销售毛利率':'ROA'].apply(lambda x:x.mean(),axis=1)
    factor['size'] = factor.loc[:,'对数流通市值'].copy()
    factor['mom'] = factor.loc[:,'过去3个月动量'].copy()
    factor['volitility'] = factor.loc[:,'收益率标准差'].copy()
    factor['liquidity'] = factor.loc[:,'换手率'].copy()
    factor['beta'] = factor.loc[:,'beta'].copy()
    factor['leverage'] = factor.loc[:,'资产负债率':'现金比率'].apply(lambda x:x.mean(),axis=1)

    factor_final = pd.concat([factor['证券代码'],factor['涨跌幅'],factor['申万行业'],factor['size'],factor['beta'],
                                factor['mom'],factor['value'],factor['growth'],factor['profit'],factor['volitility'],
                              factor['liquidity'],factor['leverage']],axis=1)
    factor_final.index=factor.index.copy()
    factor_final.to_csv('./data/factor.csv')
else:
    factor_final = pd.read_csv('./data/factor.csv')

#%%
factor_final = pd.read_csv('./data/factor.csv',index_col=0)
factor_final = factor_final.dropna(how='all',axis=0)
industry_info = (factor_final['申万行业'].drop_duplicates())
industry = np.array([1 * (factor_final['申万行业'].values == x) for x in industry_info.values]).T
industry = pd.DataFrame(industry, columns=list(industry_info.values))
industry.index = factor_final.index.copy()
industry.sort_index(inplace=True)
factor_final.sort_index(inplace=True)
data = pd.concat([factor_final.iloc[:, :4], industry, factor_final.iloc[:, 5:]], axis=1)

#%%
def style_factor_norm(factors, capital):
    '''
    使用市值进行标准化
    '''
    from statsmodels.stats.weightstats import DescrStatsW
    w_stats = DescrStatsW(factors, weights = capital)
    w_mu = w_stats.mean      # 加权平均
    w_std = np.std(factors)        # 等权标准差
    return((factors - w_mu) / w_std)

class CrossSection():
    '''
    base_data: DataFrame
    column1: date
    colunm2: stocknames
    colunm3: capital
    column4: ret
    style_factors: DataFrame
    industry_factors: DataFrame
    '''

    def __init__(self, base_data, style_factors=pd.DataFrame(), industry_factors=pd.DataFrame()):
        self.date = list(base_data.date)[0]  # 日期
        self.stocknames = list(base_data.stocknames)  # 股票名
        self.capital = base_data.capital.values  # 市值
        self.ret = base_data.ret.values  # t+1期收益率
        self.style_factors_names = list(style_factors.columns)  # 风格因子名
        self.industry_factors_names = list(industry_factors.columns)  # 行业因子名

        self.N = base_data.shape[0]  # 股票数
        self.Q = style_factors.shape[1]  # 风格因子数
        self.P = industry_factors.shape[1]  # 行业因子数
        self.style_factors = style_factor_norm(style_factors.values, self.capital)  # 风格因子值
        self.industry_factors = industry_factors.values  # 行业因子值
        self.country_factors = np.array(self.N * [[1]])  # 国家因子

        self.W = np.sqrt(self.capital) / sum(np.sqrt(self.capital))  # 加权最小二乘法的权重

        print('\rCross Section Regression, ' + 'Date: ' + str(self.date) + ', ' + \
              str(self.N) + ' Stocks, ' + str(self.P) + ' Industry Facotrs, ' + str(self.Q) + ' Style Facotrs', end='')

    def reg(self):

        factors = np.matrix(np.hstack([self.country_factors, self.industry_factors, self.style_factors]))
        X = add_constant(factors)
        model = sm.WLS(self.ret, X, weights=self.W)
        results = model.fit()
        factor_ret = results.params
        specific_ret =( self.ret - model.predict(X.T))[0]
        pure_factor_portfolio_exposure = ( (results.params) * factors.T) [0]
        R2 = results.rsquared
        summary=results.summary()

        return ((factor_ret, specific_ret, pure_factor_portfolio_exposure, R2))


class MFM():
    '''
    data: DataFrame
    column1: date
    colunm2: stocknames
    colunm3: capital
    column4: ret
    style_factors: DataFrame
    industry_factors: DataFrame
    '''

    def __init__(self, data, P, Q):
        self.Q = Q  # 风格因子数
        self.P = P  # 行业因子数
        self.dates = pd.to_datetime(data.date.values)  # 日期
        self.sorted_dates = pd.to_datetime(np.sort(pd.unique(self.dates)))  # 排序后的日期
        self.T = len(self.sorted_dates)  # 期数
        self.data = data  # 数据
        self.columns = ['country']  # 因子名
        self.columns.extend((list(data.columns[4:])))

        self.last_capital = None  # 最后一期的市值
        self.factor_ret = None  # 因子收益
        self.specific_ret = None  # 特异性收益
        self.R2 = None  # R2

    def reg_by_time(self):
        '''
        逐时间点进行横截面多因子回归
        '''
        factor_ret = []
        R2 = []
        pure_factor_portfolio_expo = []
        specific_ret = []

        print('===================================逐时间点进行横截面多因子回归===================================')
        for t in range(self.T):
            data_by_time = self.data.iloc[self.dates == self.sorted_dates[t], :]
            data_by_time = data_by_time.sort_values(by='stocknames')

            cs = CrossSection(data_by_time.iloc[:, :4], data_by_time.iloc[:, -self.Q:],
                              data_by_time.iloc[:, 4:(4 + self.P)])
            factor_ret_t, specific_ret_t, pure_factor_portfolio_expo_t, R2_t = cs.reg()
            pure_factor_portfolio_expo.append(pure_factor_portfolio_expo_t.tolist()[0])
            factor_ret.append(factor_ret_t)
            specific_ret.append(pd.DataFrame(specific_ret_t, columns=cs.stocknames, index=[self.sorted_dates[t]]))

            R2.append(R2_t)
            self.last_capital = cs.capital

        factor_ret = pd.DataFrame(factor_ret, columns=self.columns, index=self.sorted_dates)
        pure_factor_portfolio_expo = pd.DataFrame(pure_factor_portfolio_expo, index=self.sorted_dates)
        R2 = pd.DataFrame(R2, columns=['R2'], index=self.sorted_dates)

        self.factor_ret = factor_ret  # 因子收益
        self.specific_ret = specific_ret  # 特异性收益
        self.R2 = R2  # R2
        return ((factor_ret, pure_factor_portfolio_expo, specific_ret, R2))



model = MFM(data, len(industry_info), 9)
(factor_ret, pure_factor_portfolio_expo, specific_ret, R2) = model.reg_by_time()

#%%
# 柱状堆叠图
import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from pyecharts.charts import Grid, Boxplot, Scatter
from snapshot_selenium import snapshot
from pyecharts import options as opt
def plot_bar_html(df):

    bar = (Bar(init_opts=opts.InitOpts(theme = 'westeros' ))
            .add_xaxis(range(0,4))# df.index)
            .add_yaxis("R2", df['R2'])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                pos_left="center", title="Michelson-Morley Experiment"
            ),
            tooltip_opts=opts.TooltipOpts(trigger="item", axis_pointer_type="shadow"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=True,
                splitarea_opts=opts.SplitAreaOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(formatter="expr {value}"),
                splitline_opts=opts.SplitLineOpts(is_show=False),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ))
    ))

    bar.render("./result/r2.html")
    make_snapshot(snapshot, bar.render(), "./result/r2_e.png")
plot_bar_html(R2)

#%%
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.charts import Bar
from pyecharts.charts import Line
factor_ret = pd.read_csv('./result/factor_ret.csv',index_col=0)
factor_ret = factor_ret.apply(lambda x: round(x,4))
factor_ret.drop(['0'],axis=1,inplace=True)

#%%
def plot_heatmap(factor_ret,year):
    data = np.array(factor_ret)
    list_ = []
    for i in range(len(factor_ret.index)):
        for j in range(len(factor_ret.columns)):
            list_.append([i, j, factor_ret.iloc[i, j]])

    heatmap = (
        HeatMap(init_opts=opts.InitOpts(theme = 'westeros' ))
        .add_xaxis(factor_ret.index.tolist())
        .add_yaxis("", factor_ret.columns.tolist(), list_)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Barra factor ret heatmap for %s"%year),
            visualmap_opts=opts.VisualMapOpts(
                min_=min(list_)[2], max_=max(list_)[2], is_calculable=True, orient="horizontal", pos_left="center")
        ))
    heatmap.render("./result/barra_factor_ret_heatmap.html")
    make_snapshot(snapshot, heatmap.render(), './result/barra_factor_ret_heatmap%s'%year+'.png')

plot_heatmap(factor_ret.iloc[:123,:],'2018')
plot_heatmap(factor_ret.iloc[123:367,:],'2019')
plot_heatmap(factor_ret.iloc[367:,:],'2020')

#%%
R2 = pd.read_csv('./result/R2.csv',index_col=0)
R2 = R2.apply(lambda x: round(x,4))
def plot_bar(R2):

    BAR = (
        Bar(init_opts=opts.InitOpts(theme = 'westeros' ))
        .add_xaxis(R2.index.tolist())
        .add_yaxis("", R2['R2'].values.tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Barra R2"),
             ))
    make_snapshot(snapshot, BAR.render(), './result/barra_r2.png')
plot_bar(R2)
#%%
def plot_line_(arr):
    input = pd.Series(arr['R2']).apply(lambda x : round(x,4)).tolist()
    line = (
        Line(init_opts=opts.InitOpts(theme = 'westeros' ))
        .add_xaxis(arr.index.tolist())
        .add_yaxis(
            series_name="R2",
            y_axis= input ,
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均值")]
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="R2"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
    )

    make_snapshot(snapshot, line.render(), "./result/barra_r2.png")

plot_line_(R2.iloc[1:,:])



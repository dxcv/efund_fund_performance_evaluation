# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@E-mail: chenmx19@mails.tsinghua.edu.cn
@description:
    #易方达金融科技部数据平台爱工程师远程实习：基金收益与风险指标计算
    # 计算易方达消费行业股票基金（110022）的累计收益率和历史最大回测等指标，并对计算结果进行可视化展示。基金净值数据可从公司官网下载，编程语言不限，需要提交源代码和课题报告。
@revise log:
    2021.06.09 创建程序 载整理数据计算累积收益率 maxdd,wind数据库基金没有pe pb分位数，无法分组计算，计算maxdd  maxll 分年和年投资期限,计算克莱默指标，历史var cvar，
    2021.06.10 取了benchmark rf market的数据,debug，加了一堆指标
    2021.06.11 整理文档，整理代码，查bug
    2021.06.13  写了rolling函数，以及计算函数封装为类,debug,seaborn可视化
    2021.06.14  可视化
    2021.06.15  整理指标公式到md，计算整个区间内的指标，计算分年的指标，画出所有指标的滚动投资的图,年化收益率指标净值归一化
    2021.06.16   参数写成常数参数（改例子和所有代码） 整理文档
    2021.06.17   改代码改报告图片和结论
                对指标的分类对比、理解、如何使用、物理意义、对选基金的时候正向还是负向的判断、适用的基金类型，注意事项等进行总结成结论，以及对110022的总结
    2021.06.18  PPT50%
    2021.06.19 PPT50% Brinson model单期代码部分
    2021.06.20  debug 单期部分文档 多期部分
"""

#%%
import pandas as pd
import numpy as np
import datetime
import os,re
import inspect
# import warnings
# warnings.filterwarnings('ignore')
import time
import datetime
from tqdm import tqdm


from data_get import *
from index_cal import *
from index_plot import *
starttime = datetime.datetime.now()

index = '110022.OF'
begin_date = '2010-08-20'
end_date = '2021-06-08'



df, df_with_rf,df_with_ben, df_with_rf_market,df_with_rf_ben, df_with_rf_market_ben, rf, market, benchmark_df = data_load(index,begin_date,end_date)

index = Index()
functions=inspect.getmembers(Index,lambda x: inspect.isfunction(x))
functions=list(filter(lambda x: not x[0].startswith('__'),functions))
functions=list(functions[x][0] for x in range(len(functions)))
functions.remove('case_to_function')
functions.remove('case_fun_other')
functions.remove('YearProcess')
functions.remove('calcHurst2')
functions.remove('Ret')
column_name = functions.copy()
print(column_name)

#%%
# 1. 整个投资期内所有指标的表现
index_list_all = []
index_list_all.append(index.Cumret(df))
index_list_all.append(index.Compoundedret(df))
index_list_all.append(index.Stats(df,method='mean'))
index_list_all.append(index.Stats(df,method='max'))
index_list_all.append(index.Stats(df,method='min'))
index_list_all.append(index.Stats(df,method='std'))
index_list_all.append(index.Annulstd(df))
index_list_all.append(index.Skew(df))
index_list_all.append(index.Kurtosis(df))
index_list_all.append(index.Downsiderisk(df))
index_list_all.append(index.MaxDrawdown(df))
index_list_all.append(index.MaxLoss(df))
index_list_all.append(index.Winfreq(df))
index_list_all.append(index.AR1T(df))
index_list_all.append(index.his_VaR(df))
index_list_all.append(index.his_CVaR(df))
index_list_all.append(index.Sharp(df_with_rf))
index_list_all.append(index.Sortino(df_with_rf))
index_list_all.append(index.Calmar(df_with_rf))
index_list_all.append(index.Omega(df_with_rf))
index_list_all.append(index.Trackingerror(df_with_ben))
index_list_all.append(index.Information(df_with_ben))
index_list_all.append(index.Beta(df_with_rf_market))
index_list_all.append(index.Jasens(df_with_rf_market))
index_list_all.append(index.Treynor(df_with_rf_market))
index_list_all.append(index.M2(df_with_rf_market))
index_list_all.append(index.TM_beta2(df_with_rf_market))
index_list_all.append(index.HM_beta2(df_with_rf_market))
index_list_all.append(index.Manipulationprood(df_with_rf_ben))
index_df_all = pd.DataFrame(index_list_all)
index_df_all.index=['Cumret',
                    'Compoundedret',
                    'mean',
                    'max',
                    'min',
                    'std',
                    'Annulstd',
                    'Skew',
                    'Kurtosis',
                    'Downsiderisk',
                    'MaxDrawdown',
                    'MaxLoss',
                    'Winfreq',
                    'AR1T',
                    'his_VaR',
                    'his_CVaR',
                    'Sharp',
                    'Sortino',
                    'Calmar',
                    'Omega',
                    'Trackingerror',
                    'Information',
                    'Beta',
                    'Jasens',
                    'Treynor',
                    'M2',
                    'TM_beta2',
                    'HM_beta2',
                    'Manipulationprood'
                                        ]
index_df_all.to_csv('./result/index_df_all.csv')

#%%
# 2. 指标分年度表现
list_2010 = []
list_2011 = []
list_2012 = []
list_2013 = []
list_2014 = []
list_2015 = []
list_2016 = []
list_2017 = []
list_2018 = []
list_2019 = []
list_2020 = []
index_list1=[]
for function_i in tqdm(functions):
    if function_i in ['Cumret','Compoundedret','Annulstd','Downsiderisk','MaxDrawdown','MaxLoss'
                      ,'Winfreq','AR1T','his_VaR','his_CVaR','Trackingerror', 'Information']:
        arr = rolling(df_with_ben, index.case_to_function(function_i), method='year')
        index_list1.append(function_i)
        list_2010.append(arr[58-1])
        list_2011.append(arr[303-1])
        list_2012.append(arr[546-1])
        list_2013.append(arr[784-1])
        list_2014.append(arr[1029-1])
        list_2015.append(arr[1273-1])
        list_2016.append(arr[1518-1])
        list_2017.append(arr[1763-1])
        list_2018.append(arr[2007-1])
        list_2019.append(arr[2251-1])
        list_2020.append(arr[2494-1])
index_df_year1 = pd.concat([pd.Series(list_2010),pd.Series(list_2011),pd.Series(list_2012),pd.Series(list_2013),pd.Series(list_2014),pd.Series(list_2015),pd.Series(list_2016),pd.Series(list_2017),pd.Series(list_2018),pd.Series(list_2019),pd.Series(list_2020)],axis=1)
index_df_year1.index = index_list1
index_df_year1.columns=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
index_df_year1.to_csv('./result/index_df_year1.csv')


list_2015_ = []
list_2016_ = []
list_2017_ = []
list_2018_ = []
list_2019_ = []
list_2020_ = []
index_list2=[]
for function_i in tqdm(functions):
    if function_i in ['Sharp', 'AnnulSharp', 'Sortino', 'Calmar', 'Omega',
                      'Beta', 'Jasens', 'Treynor','M2','TM_beta2','HM_beta2','Manipulationprood']:
        arr = rolling(df_with_rf_market_ben, index.case_to_function(function_i), method='year')
        index_list2.append(function_i)
        list_2015_.append(arr[243-1])
        list_2016_.append(arr[487-1])
        list_2017_.append(arr[731-1])
        list_2018_.append(arr[974-1])
        list_2019_.append(arr[1218-1])
        list_2020_.append(arr[1461-1])


index_df_year2 = pd.concat([pd.Series(list_2015_),pd.Series(list_2016_),pd.Series(list_2017_),pd.Series(list_2018_),pd.Series(list_2019_),pd.Series(list_2020_)],axis=1)
index_df_year2.index=index_list2
index_df_year2.columns=['2015','2016','2017','2018','2019','2020']
index_df_year2.to_csv('./result/index_df_year2.csv')

#%%
# 3.
index_list_1 = []
index_list_2 = []
index_list_3 = []
index_list_4 = []
index_list_5 = []
for function_i in tqdm(functions):
    print(function_i)
    if function_i in ['Dayret','Cumret','Compoundedret','Annulstd','Skew','Downsiderisk','MaxDrawdown','MaxLoss'
                      ,'Winfreq','AR1T','his_VaR','his_cVaR']:
        arr = rolling(df, index.case_to_function(function_i), method='begin_end')
        date_1 = df.date[1:].apply(lambda x: str(x))
        ret = rolling(df, index.Dayret, method='begin_end')
        plot_line(arr, date, function_i)
        plot_box(arr, function_i)
        plot_dist(arr, function_i)
        plot_relat_ret(arr, ret, function_i)
        print(arr)
        index_list_1.append(arr)
    if function_i in ['Sharp','AnnulSharp','Sortino','Calmar','Omega']:
        arr = rolling(df_with_rf, index.case_to_function(function_i), method='begin_end')
        date_2 = df_with_rf.date[1:].apply(lambda x: str(x))
        ret = rolling(df_with_rf, index.Dayret, method='begin_end')
        plot_line(arr, date, function_i)
        plot_box(arr, function_i)
        plot_dist(arr, function_i)
        plot_relat_ret(arr, ret, function_i)
        print(arr)
        index_list_2.append(arr)
    if function_i in ['Trackingerror', 'Information']:
        arr = rolling(df_with_ben, index.case_to_function(function_i), method='begin_end')
        date_3 = df_with_ben.date[1:].apply(lambda x: str(x))
        ret = rolling(df_with_ben, index.Dayret, method='begin_end')
        plot_line(arr, date, function_i)
        plot_box(arr, function_i)
        plot_dist(arr, function_i)
        plot_relat_ret(arr, ret, function_i)
        print(arr)
        index_list_3.append(arr)
    if function_i in ['Beta', 'Jasens', 'Treynor','M2','TM_beta2','HM_beta2']:
        arr = rolling(df_with_rf_market, index.case_to_function(function_i), method='begin_end')
        date_4 = df_with_rf_market.date[1:].apply(lambda x: str(x))
        ret = rolling(df_with_rf_market, index.Dayret, method='begin_end')
        plot_line(arr, date, function_i)
        plot_box(arr, function_i)
        plot_dist(arr, function_i)
        plot_relat_ret(arr, ret, function_i)
        print(arr)
        index_list_4.append(arr)
    if function_i in ['Manipulationprood']:
        arr = rolling(df_with_rf_ben, index.case_to_function(function_i), method='begin_end')
        date_5 = df_with_rf_ben.date[1:].apply(lambda x: str(x))
        ret = rolling(df_with_rf_ben, index.Dayret, method='begin_end')
        plot_line(arr, date, function_i)
        plot_box(arr, function_i)
        plot_dist(arr, function_i)
        plot_relat_ret(arr, ret, function_i)
        print(arr)
        index_list_5.append(arr)

index_1 = pd.DataFrame(index_list_1,index=['Dayret','Cumret','Compoundedret','Annulstd','Downsiderisk','MaxDrawdown','MaxLoss'
                      ,'Winfreq','AR1T','his_VaR','his_cVaR'],columns=date_1)
index_2 = pd.DataFrame(index_list_2,index=['Sharp','AnnulSharp','Sortino','Calmar','Omega'],columns=date_2)
index_3 = pd.DataFrame(index_list_3,index=['Trackingerror', 'Information'],columns=date_3)
index_4 = pd.DataFrame(index_list_4,index=['Beta', 'Jasens', 'Treynor','M2','TM_beta2','HM_beta2'],columns=date_4)
index_5 = pd.DataFrame(index_list_5,index=['Manipulationprood'],columns=date_5)

index_1.to_csv('./result/index_1.csv',encoding='utf_8_sig')
index_2.to_csv('./result/index_2.csv',encoding='utf_8_sig')
index_3.to_csv('./result/index_3.csv',encoding='utf_8_sig')
index_4.to_csv('./result/index_4.csv',encoding='utf_8_sig')
index_5.to_csv('./result/index_5.csv',encoding='utf_8_sig')

#%%
# 6.
others = pd.read_excel('./data/others.xlsx')
others_index = pd.DataFrame()
fundnamelist = []
for i in range(0,521):
    df_i = others.iloc[3:,i*5:i*5+3]
    if len(df_i.columns) <1:
        pass
    else:
        fundname=df_i.columns[1]
        fundnamelist.append(fundname)
        df_i = df_i.dropna(subset=[fundname])
        df_i.columns = ['date','net_value','benchmark']
        index_list_i = []
        index_list_i.append(index.Cumret(df_i))
        index_list_i.append(index.Compoundedret(df_i))
        index_list_i.append(index.Stats(df_i,method='mean'))
        index_list_i.append(index.Stats(df_i,method='max'))
        index_list_i.append(index.Stats(df_i,method='min'))
        index_list_i.append(index.Stats(df_i,method='std'))
        index_list_i.append(index.Annulstd(df_i))
        index_list_i.append(index.Skew(df_i))
        index_list_i.append(index.Kurtosis(df_i))
        index_list_i.append(index.Downsiderisk(df_i))
        index_list_i.append(index.MaxDrawdown(df_i))
        index_list_i.append(index.MaxLoss(df_i))
        index_list_i.append(index.Winfreq(df_i))
        index_list_i.append(index.AR1T(df_i))
        index_list_i.append(index.his_VaR(df_i))
        index_list_i.append(index.his_CVaR(df_i))

        index_i = pd.DataFrame(index_list_i).T
        index_i.index=[fundname]

        others_index = others_index.append(index_i,ignore_index=True)
others_index.index=fundnamelist
others_index.columns  = ['Cumret',
                         'Compoundedret',
                         'mean',
                         'max',
                         'min',
                         'std',
                         'Annulstd',
                         'Skew',
                         'Kurtosis',
                         'Downsiderisk',
                         'MaxDrawdown',
                         'MaxLoss',
                         'Winfreq',
                         'AR1T',
                         'his_VaR',
                         'his_CVaR']
others_index.to_csv('./result/others_index.csv',encoding='utf_8_sig')



#%%
# 计算程序运行时间
endtime = datetime.datetime.now()


def timeStr(s):
    if s < 10:
        return '0' + str(s)
    else:
        return str(s)


print("程序开始运行时间：" + timeStr(starttime.hour) + ":" + timeStr(starttime.minute) + ":" + timeStr(starttime.second))
print("程序结束运行时间：" + timeStr(endtime.hour) + ":" + timeStr(endtime.minute) + ":" + timeStr(endtime.second))
runTime = (endtime - starttime).seconds
runTimehour = runTime // 3600  # 除法并向下取整，整除
runTimeminute = (runTime - runTimehour * 3600) // 60
runTimesecond = runTime - runTimehour * 3600 - runTimeminute * 60
print("程序运行耗时：" + str(runTimehour) + "时" + str(runTimeminute) + "分" + str(runTimesecond) + "秒")
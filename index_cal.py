# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@E-mail: chenmx19@mails.tsinghua.edu.cn
@description:
@revise log:
"""
from __future__ import division
import pandas as pd
import numpy as np
from collections import Iterable
from statsmodels.regression import linear_model
from statsmodels.api import add_constant


#%%
def status(x) :
    return pd.Series([x.count(),x.min(),x.idxmin(),x.quantile(.25),x.median(),
                      x.quantile(.75),x.mean(),x.max(),x.idxmax(),x.mad(),x.var(),
                      x.std(),x.skew(),x.kurt()],index=['总数','最小值','最小值位置','25%分位数',
                    '中位数','75%分位数','均值','最大值','最大值位数','平均绝对偏差','方差','标准差','偏度','峰度'])

#%%
def rolling(df,func,method='begin_end',tw=63):
    if len(df) < 1:
        raise ('dataframe is not a time series!')
    list_ = []
    for i in range(len(df.index) - 1):
        if i == 0:
            list_.append(np.nan)
        else:
          if method=='begin_end':
                list_.append(func(df.iloc[:int(i) + 1, :], colname='net_value', period='all'))
          elif method == 'year':
                list_.append(func(df.iloc[:int(i) + 1, :], colname='net_value', period=df.iloc[int(i)+1]['year']))
          elif method =='rolling':
                list_.append(func(df.iloc[int(i)-tw:int(i)+1, :], colname='net_value', period='all'))
          else:
                raise ('method is not definded!')
    return np.array(list_)

#%%
class Index():
    def __init__(self):
        pass

    def case_to_function(self,fun_name):
        '''

        :param fun_name:
        :return:
        '''
        method = getattr(self, str(fun_name), self.case_fun_other)
        return method

    def case_fun_other(self):
        print('this function is not defined yet!')

    def YearProcess(self, portfolio, period='all'):
        '''
        Splite the data by year for calculating
        :param portfolio: DataFrame
        :param period: period:str(all,2010-2021)
        :return: DataFrame
        '''
        if period !='all':
            return portfolio[portfolio['year'] == period]
        else:
            return portfolio

    def Ret(self,portfolio,colname='net_value',period='all'):
        '''

        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        return portfolio[colname].pct_change(1)


    # 日收益率序列$R_t$
    def Dayret(self, portfolio, colname='net_value', period='all'):
        '''

        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1)
        if len(RET) == 0:
            return np.nan
        else:
            return RET.iloc[-1]



    # 累积收益率Cumret
    def Cumret(self, portfolio,colname='net_value',period='all'):
        '''
        calculate cumulative return of the portfolio
        :param portfolio:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        portfolio_p = portfolio[colname].values
        if len(portfolio_p)<1:
            return np.nan
        return (portfolio_p[-1]-portfolio_p[0])/portfolio_p[0]


    # ### 年均复利收益率Compoundedret
    def Compoundedret(self, portfolio,colname='net_value',period='all',year_day=251):
        '''

        :param portfolio:
        :param colname:
        :param period:
        :param year_day:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        portfolio_p = portfolio[colname].values
        if len(portfolio_p)<1:
            return np.nan
        return (portfolio_p[-1]/portfolio_p[0])**(year_day/len(portfolio_p))-1


    # 净值最高点最低点均值标准差Stats
    def Stats(self, portfolio,method='mean',colname='net_value',period='all'):
        '''

        :param portfolio:
        :param method:
        :param colname:
        :param period:
        :param year_day:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        portfolio_p = portfolio[colname].values
        if len(portfolio_p)<1:
            return np.nan
        if method=='mean':
            return np.mean(portfolio_p)
        elif method=='std':
            return np.std(portfolio_p)
        elif method=='max':
            return np.max(portfolio_p)
        elif method=='min':
            return np.min(portfolio_p)
        else:
            return 'method not defined, check!'

    #  收益率年化标准差Annulstd
    def Annulstd(self, portfolio,colname='net_value',period='all',year_day=251):
        '''

        :param portfolio:
        :param colname:
        :param period:
        :param year_day:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        return np.std(RET) * np.sqrt(year_day)

    ## 日收益率分布的峰度Skew
    def Skew(self, portfolio,colname='net_value',period='all'):
        '''

        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        if ((len(portfolio)-1)*np.std(RET)**3)==0:
            return np.nan
        else:
            return np.sum(RET - np.mean(RET))**3 / ((len(portfolio)-1)*np.std(RET)**3)

    # 日收益率分布的偏度 Kurtosis
    def Kurtosis(self, portfolio,colname='net_value',period='all'):
        '''

        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        if ((len(portfolio)-1)*np.std(RET)**4)==0:
            return np.nan
        else:
            return np.sum(RET - np.mean(RET))**4 / ((len(portfolio)-1)*np.std(RET)**4)


    # 下行风险 Downsiderisk
    def Downsiderisk(self, portfolio,colname = 'net_value',period = 'all'):
        '''

        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        if len(RET)<=1:
            return np.nan
        else:
            sigma_d_2=(np.sum(min(0,RET[-1]-RET[0])**2))/(len(RET)-1)
            return sigma_d_2**0.5


    # 最大回撤MaxDrawdown
    def MaxDrawdown(self, portfolio,colname='net_value',period = 'all'):
        '''
        Calculate MDD
        :param portfolio: DataFrame
        :param colname: str
        :param period: str(all,2010-2015)
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        portfolio_p = portfolio[colname].values
        if len(portfolio_p)<1:
            return np.nan
        end = np.argmax((np.maximum.accumulate(portfolio_p)-portfolio_p))
        if end == 0:
            return np.nan
        begin = np.argmax(portfolio_p[:end])
        return (portfolio_p[end] - portfolio_p[begin])/portfolio_p[begin] # ,begin,end


    # ### 最大亏损(Max Loss)
    def MaxLoss(self, portfolio,colname = 'net_value',period = 'all'):
        '''
        Calculate maxloss
        :param portfolio: DataFrame
        :param colname: str
        :param period: str(all,2010-2015)
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        portfolio_p = portfolio[colname].values
        if len(portfolio_p)<1:
            return np.nan
        end = np.argmin(np.minimum.accumulate(portfolio_p))
        begin = np.argmin(portfolio_p[0])
        return (portfolio_p[end] - portfolio_p[begin])/portfolio_p[begin] #, begin, end


    # 盈利频率Winfreq
    def Winfreq(self,portfolio, colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        win_time = []
        for i in range(len(RET)):
            if RET.iloc[i] >0:
                win_time.append(1)
            else:
                win_time.append(0)
        return np.sum(win_time)/len(RET)
    

    # 自回归系数T AR1T
    def AR1T(self,portfolio, colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        if len(RET)<=1:
            return np.nan
        else:
            X = add_constant(range(len(RET[1:])))
            model = linear_model.OLS(RET[1:], X)
            return model.fit().pvalues[1]
    
    
    def calcHurst2(self, ts):
    
        if not isinstance(ts, Iterable):
            print('error')
            return
    
        n_min, n_max = 2, len(ts)//3
        RSlist = []
        for cut in range(n_min, n_max):
            children = len(ts) // cut
            children_list = [ts[i*children:(i+1)*children] for i in range(cut)]
            L = []
            for a_children in children_list:
                Ma = np.mean(a_children)
                Xta = pd.Series(map(lambda x: x-Ma, a_children)).cumsum()
                Ra = max(Xta) - min(Xta)
                Sa = np.std(a_children)
                rs = Ra / Sa
                L.append(rs)
            RS = np.mean(L)
            RSlist.append(RS)
        if len(RSlist) <=1:
            return np.nan
        else:
            return np.polyfit(np.log(range(2+len(RSlist),2,-1)), np.log(RSlist), 1)[0]
    
    
    # def Hurst(self, portfolio, colname='net_value',period = 'all'):
    #     '''
    #
    #     :param portfolio:
    #     :param colname:
    #     :param period:
    #     :return:
    #     '''
    #     portfolio = self.YearProcess(portfolio, period=period)
    #     if len(portfolio) <= 1:
    #         return np.nan
    #     else:
    #         return self.calcHurst2(portfolio[colname])

    # VaR
    
    def his_VaR(self,portfolio, colname = 'net_value',period = 'all', alpha=0.99):
        '''
        # 99%置信水平，历史收益率法计算VaR
        :param portfolio:
        :param colname:
        :param period:
        :param alpha:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        if len(portfolio)<1:
            return np.nan
        else:
            RET = portfolio[colname].pct_change(1).fillna(0)
            return abs(np.sort(RET)[int(alpha * len(np.sort(RET)))])
    

    def his_CVaR(self,portfolio, colname='net_value',period = 'all', alpha=0.99):
        '''
         # 99%置信水平，历史收益率法计算CVaR
        :param portfolio:
        :param colname:
        :param period:
        :param alpha:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        if len(portfolio)<1:
            return np.nan
        else:
            RET = portfolio[colname].pct_change(1).fillna(0)
            if len(RET)==0:
                return np.nan
            else:
    
                sorted_Returns = np.sort(RET)
                index = int(alpha * len(sorted_Returns))
                sum_var = sorted_Returns[0]
                for i in range(1, index):
                    sum_var += sorted_Returns[i]
                    CVaR = abs(sum_var / index)
                return abs(sum_var / int(alpha * len(np.sort(RET))))
    

    #  夏普比率Sharp
    def Sharp(self,portfolio, colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x+1)**(1/365)-1)
        if np.std(RET) == 0 :
            return np.nan
        if len(portfolio) <= 1:
            return np.nan
        else:
            return (np.mean(RET)-portfolio['rf'].iloc[-1])/np.std(RET)
    

    # 年化夏普比率AnnulSharp
    def AnnulSharp(self, portfolio, colname = 'net_value',period = 'all',annulday=250):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        if len(RET)<=1:
            return np.nan
        else:
            return (np.mean(RET)-portfolio['rf'].iloc[-1])* annulday/(np.std(RET)*np.sqrt(len(RET)))
    
    # AnnulSharp(df,colname='net_value',period='all')
    

    ################################################################
    # 双夏普比率 DoubleSharp
    def Doublesharp(self, portfolio,  colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        sharp_list=[]
        for i in range(len(RET)):
            if np.std(RET[i:])==0:
                return np.nan
            else:
                sharp_i  =(np.mean(RET[i:])-portfolio['rf'].iloc[i])/np.std(RET[i:])
                if sharp_i == np.inf:
                    sharp_list.append(0)
                else:
                    sharp_list.append(sharp_i)
        if len(RET) <= 1:
            return np.nan
        else:
            sharp = (np.mean(RET)-portfolio['rf'].iloc[-1])/np.std(RET)
            sharp_list = [0 if x == np.inf else x for x in sharp_list]
            return sharp/np.std(sharp_list)
    
    # Doublesharp(df,colname='net_value',period='all')
    # E:\anaconda\lib\site-packages\numpy\core\_methods.py:229: RuntimeWarning: invalid value encountered in subtract
    #   x = asanyarray(arr - arrmean)

    ################################################################
    
    #### 概率夏普比率 ProbabilisticSharp
    
    

    # #### 索提诺比率Sortino
    def Sortino(self, portfolio, colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        if self.Downsiderisk(portfolio) == 0:
            return np.nan
        if len(RET) <= 1:
            return np.nan
        else:

            return (np.mean(RET)-portfolio['rf'].iloc[-1])/self.Downsiderisk(portfolio)
    

    # 卡玛Calmar
    
    def Calmar(self, portfolio,colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        if len(RET)<=1:
            return np.nan
        else:
            return (np.mean(RET)-portfolio['rf'].iloc[-1])/self.MaxDrawdown(portfolio)
    

    #### **欧米伽Omega
    # https://github.com/quantopian/empyrical/blob/master/empyrical/stats.py
    def Omega(self, portfolio, colname = 'net_value',period = 'all',required_return=0.0):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0)
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        returns_less_thresh = RET - portfolio['rf'] - required_return
        numer = sum(returns_less_thresh[returns_less_thresh > 0.0])
        denom = -1.0 * sum(returns_less_thresh[returns_less_thresh < 0.0])
    
        if denom > 0.0:
            return numer / denom
        else:
            return np.nan
    
    # Omega(df)
    

    #######################################################
    ## 晨星风险调整收益(Morningstar Risk-Adjusted Return)
    # def MRAR(self, portfolio,rf=0,required_r = 0,colname = 'net_value',period = 'all'):
    #     '''
    # 
    #     :param portfolio:
    #     :param colname:
    #     :param period:
    #     :return:
    #     '''
    #     portfolio = self.YearProcess(portfolio, period=period)
    #     RET = portfolio[colname].pct_change(1).fillna(0)
    
    
    # MRAR(df)
    

    # **Stutzer指数
    # def Stutzer(self, portfolio, rf=0, colname = 'net_value',period = 'all'):
    #     '''
    #
    #     :param portfolio:
    #     :param colname:
    #     :param period:
    #     :return:
    #     '''
    #     portfolio = self.YearProcess(portfolio, period=period)
    #     RET = portfolio[colname].pct_change(1).fillna(0)
    #
    #     opt = {}
    #     for theta in np.arange(0,1,0.01):
    #         opt[theta] = abs(-1 * np.log(1 / len(RET) * np.sum(np.exp(theta) * (RET - rf))))
    #     opt_thta = max(opt,key=opt.get)
    #     stutzer = abs(RET.iloc[-1]-rf)/np.mean(RET-rf) * np.sqrt(2*abs(opt_thta))
    #     return stutzer
    #
    #
    # #  **Kalpan Lambda统计量
    # def Kalpanlambda(self, portfolio, colname = 'net_value',period = 'all'):
    #     '''
    #
    #     :param portfolio:
    #     :param colname:
    #     :param period:
    #     :return:
    #     '''
    #     portfolio = self.YearProcess(portfolio, period=period)
    #     RET = portfolio[colname].pct_change(1).fillna(0).values
    #     portfolio['rf'] = portfolio['rf'].apply(lambda x: (x+1)**(1/365)-1)
    #     if len(RET)<1:
    #         return np.nan
    #         opt = {}
    #         for theta in np.arange(0,1,0.01):
    #             numerator1 =np.sum((RET-portfolio['rf'])*theta)
    #             numerator2 =np.exp(-max(-theta*(RET[-1]-portfolio['rf'].iloc[-1]),0))
    #             numerator3 =max(-theta*(RET[-1]-portfolio['rf'].iloc[-1]),0)
    #             opt[theta] = (numerator1-numerator2-numerator3-1)/len(RET)
    #         return max(opt,key=opt.get)


    # 跟踪误差Trackingerror
    def Trackingerror(self, portfolio, colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        r_ben = portfolio['benchmark'].pct_change(1).fillna(0).values
        if len(RET)==1:
            return np.nan
        else:
            tr_2=np.sum(RET-r_ben)**2/(len(RET)-1)
            return tr_2**0.5
    
    # 信息比率Information
    def Information(self, portfolio,colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param benchmark:
        :param colname:
        :param period:
        :return:
        '''
        TE = self.Trackingerror(portfolio, colname='net_value', period='all')
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        r_ben = portfolio['benchmark'].pct_change(1).fillna(0).values
        if len(r_ben)<1:
            return np.nan
        else:
            return (np.mean(RET)-r_ben[-1])/TE
    
    
    # 相对基准的胜率Upmarketcapture
    # https://www.investopedia.com/terms/u/up-market-capture-ratio.asp
    # def Upmarketcapture(self, portfolio,colname='net_value',period = 'all'):
    #     '''
    #
    #     :param portfolio:
    #     :param benchmark:
    #     :param market:
    #     :param colname:
    #     :param period:
    #     :return:
    #     '''
    #     portfolio = self.YearProcess(portfolio,period=period)
    #
    #     if len(portfolio)<1:
    #         return np.nan
    #     if self.Compoundedret(portfolio,colname='benchmark', period='all') ==0:
    #         return np.nan
    #     return self.Compoundedret(portfolio,colname='net_value', period='all') / self.Compoundedret(portfolio,colname='benchmark', period='all')
    
    
    ###################################################################
    # Beta
    
    
    def Beta(self, portfolio,colname = 'net_value',period = 'all', tw = 5):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
    
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        MRT = portfolio['market'].pct_change(1).fillna(0).values
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        rr_p = RET - portfolio['rf'].values
        rr_m = MRT - portfolio['rf'].values
        if len(rr_p) <=1:
            return np.nan
        else:
            reg = linear_model.OLS(rr_p[-tw:],rr_m[-tw:].reshape(-1, 1)).fit()
            return reg.params[0]
    
    # 詹森alpha Jasens
    ###################################################################
    def Jasens(self, portfolio,colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        MKT = portfolio['market'].pct_change(1).fillna(0).values
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        rr_p = RET - portfolio['rf'].values
        rr_m = MKT - portfolio['rf'].values
        if len(rr_p) <=1:
            return np.nan
        else:
            return rr_p[-1]-self.Beta(portfolio,colname = 'net_value')* rr_m[-1]
    

    # 特雷诺比率Treynor
    def Treynor(self, portfolio,colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
    
        beta = self.Beta(portfolio,colname='net_value')
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        if len(RET)==0 :
            return np.nan
        else:
            return (np.mean(RET)-portfolio['rf'].iloc[-1])/  beta
    

    # M2
    def M2(self, portfolio ,colname = 'net_value',period = 'all'):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio,period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        MKT = portfolio['market'].pct_change(1).fillna(0).values
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        if len(RET)==0 :
            return np.nan
        else:
            gamma = np.std(MKT) / np.std(RET)
        return gamma * (np.mean(RET)-portfolio['rf'].iloc[-1])+portfolio['rf'].iloc[-1]



    
    # T-M model中的beta2
    def TM_beta2(self, portfolio,  colname='net_value',period = 'all',tw=5):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        MKT = portfolio['market'].pct_change(1).fillna(0).values
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        rr_p = RET - portfolio['rf'].values
        rr_m = MKT - portfolio['rf'].values
        rr_m2 = ( MKT - portfolio['rf'].values) **2
        X = np.column_stack((rr_m2,rr_m))
        if len(rr_p) <=1:
            return np.nan
        else:
            reg = linear_model.OLS(rr_p[-tw:],X[-tw:]).fit()
            return reg.params[0]
    


    # H-M model中的beta2
    def HM_beta2(self, portfolio, colname='net_value',period = 'all',tw=5):
        '''
    
        :param portfolio:
        :param colname:
        :param period:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        MKT = portfolio['market'].pct_change(1).fillna(0).values
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        rr_p = RET - portfolio['rf'].values
        rr_m = MKT - portfolio['rf'].values
        if len(rr_p) <=1:
            return np.nan
        else:
            rr_m_d = []
            for i in range(len(RET)):
                if rr_p[i]>rr_m[i]:
                    rr_m_d.append(1)
                else:
                    rr_m_d.append(0)
            X = np.column_stack((rr_m_d,rr_m))
            reg = linear_model.OLS(rr_p[-tw:],X[-tw:]).fit()
            return reg.params[0]
    

    #  Manipulation-Proof 统计量
    def Manipulationprood(self, portfolio, colname='net_value',period = 'all', gamma=0.8):
        # 风险厌恶系数越大，越厌恶风险
        '''

        :param portfolio:
        :param colname:
        :param period:
        :param gamma:
        :return:
        '''
        portfolio = self.YearProcess(portfolio, period=period)
        RET = portfolio[colname].pct_change(1).fillna(0).values
        n_year = len(portfolio['year'].drop_duplicates())
        r_ben = portfolio['benchmark'].pct_change(1).fillna(0).values
        portfolio['rf'] = portfolio['rf'].apply(lambda x: (x + 1) ** (1 / 365) - 1)
        rr_p = RET - portfolio['rf'].values
        rr_b = r_ben - portfolio['rf'].values

        if  pd.Series(RET/r_ben).fillna(0).sum() ==0:
            return np.nan
        else:
            return  1/((1-gamma)*n_year) * np.log(1/len(RET) * pd.Series(RET/r_ben).fillna(0).sum()**(1-gamma))

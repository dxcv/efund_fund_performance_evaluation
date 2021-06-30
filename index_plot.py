# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@E-mail: chenmx19@mails.tsinghua.edu.cn
@description:
@revise log:
"""

#%%
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.charts import Grid, Boxplot, Scatter
import pandas as pd
import numpy as np
from index_cal import rolling
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 步骤一（替换sans-serif字体） Microsoft YaHei SimHei
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
import seaborn as sns

import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts import options as opt
import sys
from IPython.display import IFrame


#%%
def plot_line_html(date,arr,name,para):
    input = pd.Series(arr).apply(lambda x : round(x,4)).tolist()
    line = (
        Line(init_opts=opts.InitOpts(theme = 'westeros' ))
        .add_xaxis(xaxis_data=date)
        .add_yaxis(
            series_name="%s"%name,
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
            title_opts=opts.TitleOpts(title="%s"%para.index+"_%s"%name),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
    )
    line.render("./result/%s"%para.index+"_%s"%name+"_line.html")

    make_snapshot(snapshot, line.render(), "./result/%s"%para.index+"_%s"%name+"_line_e.png")

# date =  df.date.apply(lambda x: str(x)[:10]).tolist()
# arr = rolling(df, index.case_to_function('Cumret'), method='begin_end')
# plot_line_html(date,arr,'Cumret',para)

#%%
def plot_box_html(arr,name,para):
    box = (Boxplot(init_opts=opts.InitOpts(theme = 'westeros' ))
            .add_xaxis(xaxis_data=["name"])
            .add_yaxis(series_name="", y_axis=arr)
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

    box.render("./result/%s"%para.index+"_%s"%name+"_box.html")
    make_snapshot(snapshot, box.render(), "./result/%s"%para.index+"_%s"%name+"_box_e.png")
# plot_box_html(arr,'cumret',para)

#%%

def plot_line(arr,date, name):
    plt.figure(figsize=(10, 8),dpi=200)
    plt.xlabel("date")
    plt.ylabel("%s" % name)
    data = pd.DataFrame(np.vstack((arr,date))).T
    data.columns = ['%s'%name, 'time']
    data = data.sort_values(by='time', ascending=True)
    t = pd.to_datetime(data['time'])
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # 設置x軸主刻度顯示格式（日期）
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=20))  # 設置x軸主刻度間距
    plt.plot(t, arr)
    plt.savefig('./result/%s' % name + '_line.png')
    plt.show()
# plot_line(rolling(df, index.Dayret, method='begin_end'),df.date[1:].apply(lambda x: str(x)),'Dailyret')

#%%
def plot_box(arr,name):
    plt.figure(figsize=(10, 8),dpi=200)
    plt.ylabel("%s" % name)
    sns.set(style="whitegrid", font_scale=1.5)  # 设置主题，文本大小
    sns.boxplot(x="%s" % name, data=pd.DataFrame(arr,columns=["%s" % name]))
    plt.savefig('./result/%s'%name+'_box.png')
    plt.show()
# plot_box(rolling(df, index.Dayret, method='begin_end'),'Dailyret')
#%%
def plot_dist(arr,name):
    plt.figure(figsize=(10, 8),dpi=200)
    plt.xlabel("%s"%name)
    plt.ylabel("frequency")
    sns.set(style="whitegrid", font_scale=1.5)  # 设置主题，文本大小
    sns.distplot(arr,kde=True, bins=30,kde_kws={'bw': 0.1}) #
    plt.savefig('./result/%s'%name+'_dist.png')
    plt.show()
# plot_dist(rolling(df, index.Dayret, method='begin_end'),'Dailyret')

#%%
def plot_relat_ret(arr,ret,name):
    data = pd.DataFrame(np.vstack((ret, arr))).T
    data.columns = ['daily_return', "%s" % name]
    sns.set(style="whitegrid", font_scale=1.5)  # 设置主题，文本大小
    g = sns.jointplot(data=data,x="daily_return", y="%s" % name)
    g.fig.set_size_inches(10, 8)  # 设置图尺寸
    plt.savefig('./result/%s'%name+'_relat_ret.png')
    plt.show()

# plot_relat_ret(rolling(df_with_rf_market, index.Sharp, method='begin_end'),rolling(df_with_rf_market, index.Dayret, method='begin_end'),'Sharpe')


#%%
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts import options as opt
import pandas as pd
import numpy as np
import json
from pyecharts import options as opts
from pyecharts.charts import WordCloud
data = pd.read_excel('./20210622v3/答辩/可视化.xlsx',sheet_name='词云图2')

cloud = (
    WordCloud()
    .add(series_name="", data_pair= [tuple(x) for x in data.values], word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Barra风格因子", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
)
make_snapshot(snapshot, cloud.render(), 'cloud2.png')
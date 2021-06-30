<center> <font size=6><b>  易方达远程实习课题：基金收益与风险指标计算</b> </font></center>

---------
<center>@author: Mengxuan Chen 陈梦玄</center>

<center>@E-mail: chenmx19@mails.tsinghua.edu.cn</center>

 <font size=5><b> 摘要</b> </font>

<p style = "text-align: justify;">本课题旨在以易方达消费行业股票基金（代码：110022.OF）为例进行计算和可视化展示基金收益和风险相关指标，包括<b>收益指标、风险指标、风险调整收益指标和其他（业绩持续性、择时）四个大类</b>，并利用<b>Brinson</b>单期和多期模型进行业绩归因，用<b>Barra</b>模型对基金中的股票组合进行风格分析。

<p style = "text-align: justify;">计算基金的收益和风险指标对<b>基金选择、基金业绩评价、基金择时、基金风险控制</b>都有着指导性的意义。不同的指标有自身的优势和缺陷，在使用时需要综合考虑。

<p style = "text-align: justify;">基金的投资收益是持有基金需要关注的第一个指标，常见的有日收益率、累积收益率、年化收益率、最大净值和最小净值。这些指标都可以根据投资时段进行相应的调整计算。易方达消费行业股票基金成立期初持有至今的累计收益率为<b>430%</b>，年化收益率为<b>17.45%</b>。基金稳定运行三年后除2018年年化收益率和累计收益率均为正值。
<p style = "text-align: justify;">最低净值、净值的波动是描述基金风险的直观指标，根据马科维茨模型，收益的波动率也是表述风险的基本指标，但是收益率分布的尖峰厚尾的特点，收益率分布的高阶矩比如峰度和偏度也会在考察的范围内。由于收益率波动率存在没有区分正向和负向波动的特点，下行风险对其进行了补充。最大回撤是常用的风险衡量指标，但也受时间段的约束。针对指数基金等被动型投资产品，跟踪误差是主要衡量指标。VaR和CVaR衡量的是组合在尾部的损失情况，常用于风险的计量。beta来源于CAPM模型，用回归的方式计量组合相对于市场组合的系统性风险。<b>这些风险指标的计算会受到不同时间窗口长度的影响</b>，采用<b>滚动的方式计算</b>时间序列的比较上更有意义。从这些风险指标上看，易方达消费行业股票基金在2014、2015、2017、2018年的风险较大。


<p style = "text-align: justify;">风险调整收益是应用于投资的风险评估计算的数值。投资产生的收益与投资的风险进行比较，得出一个比率。风险调整收益可应用于单个证券、证券组合，不同形式的风险度量为投资者提供了评估风险调整后收益的不同方法。以下列举的都是常见的风险调整收益指标，其中<b>夏普比率、特雷诺比率和詹森alpha</b>是最常用的风险调整收益指标。在此可以得出以下相关结论：

- 如果**滚动窗口采取三个月**，易方达消费行业股票基金的**詹森Alpha分布更接近于正态分布**

- 如果**滚动窗口采取三个月，信息比率的均值更加接近0**，与我们的预期相符合：投资期限越长，主动基金获取额外信息取得收益更能够在市场上实现

- 因为索提诺比率衡量的是单位下行风险获得的超额收益，其分布比较接近与幂律分布，在滚动时间窗口下形态更接近正态分布
  滚动时间窗口下，**右偏卡玛比率和左偏的欧米伽比率**表明基金的表现较好，易方达消费行业基金均呈现了这样的特点。
  
- **特雷诺比率**假设非系统性风险完全被分散，其分子分母的错配导致其**适用于基金的比较和选择，不适用于不同市场状况的分析**

- $M^2$主要解决了夏普比率是序数统计量的缺陷.比夏普比率，其分布更接近正态分布
  **Manipulation-Proof 统计量**衡量的是考虑到基金尽量操纵业绩评价指标的一种风险调整收益，其取值范围存在**明显的周期性**，即每年年底的时候会迅速升高，表明基金在年底的时候存在业绩压力

为了更好地使用指标，可以从wind数据库提取了市场上521支股票型基金的净值数据对其相关指标进行计算，并计算其均值，与易方达消费行业基金的数据进行对比。结果发现，**易方达消费行业基金的累计收益率、收益率年化标准差、最大回撤、盈利频率这几个指标均好于同类型基金**。

<p style = "text-align: justify;">本课题采用“BHB”方案的Brinson单期业绩归因，将基金组合的收益分解为基准收益（Bechmark Return BR）、配置收益（Allocation Return，AR）、选择收益（Selection Return，SR）、交互收益（Interaction Return，IR）。由于基金的全部持仓为每半年披露一次，假设每季度的持仓数据都保持不变，发现<b>易方达消费行业基金设立以来基金的平均的基准收益为7.66%，平均的选择收益为8.07%，平均的配置收益为-0.41%，平均的交互收益为-0.90%</b>。按照申万行业分类，可以计算分析每一期所投资行业的基准收益、选择收益、配置收益和交互收益。多期的Brinson模型主要考虑到了投资的复利效应，本课题采用Carino复利因子的计算方式，结论和单期模型类似。
<p style = "text-align: justify;">本课题的Barra风格分析采用了<b>行业、价值、成长、盈利、规模、动量、波动率、流动性、Beta、杠杆</b>十大类因子，对每个指标进行归一化处理，每大类因子中<b>指标采用简单加权平均，采用市值加权的最小二乘法，对行业因子采用0-1变量进行处理</b>，计算得到纯因子组合的收益，横截面回归的R2等数据。其中<b>回归的R2平均值在80%左右，该模型能较好的解释易方达消费行业基金的收益</b>。使用2019-2020年两年的日度数据进行建模发现，食品饮料、家用电器、汽车、轻工制造、电子、农林牧渔、商业贸易、医药生物、计算机这几个行业因子收益率显著不为0，规模因子、beta因子、动量因子、盈利性因子、波动率因子、流动性因子和杠杆因子这几个因子收益率显著不为0。
<img src="./result/基金收益与风险指标体系.jpg" alt="&quot;基金收益与风险指标体系&quot;" style="zoom:100%;" />


<center> <font size=2><b> 图1：基金收益与风险指标体系</b> </font></center>

通过导入相关计算模块`index_cal.py` 可以实现基金不同投资期限、不同投资方式的风险收益相关指标的计算，通过导入相关模块`index_plot.py`可以实现相关指标的时间序列图、箱线图、经验分布图、与日收益率数的两两分布图等图形的绘制。通过导入相关计算模型`Brinson_model.py`和连接Wind API可以获得基金持仓数据等，实现单期和多期Brinson模型。通过导入相关计算模型`Barra_model.py` 可以获得基金持仓股票因子数据等，实现Barra模型进行风格分析。



<div STYLE="page-break-after: always;"></div>

<font size=5><b> 目录</b> </font>

<div class="toc"><ul class="toc-item"><li><span><a href="#数据来源" data-toc-modified-id="数据来源-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>数据来源</a></span><ul class="toc-item"><li><span><a href="#原始数据" data-toc-modified-id="原始数据-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>原始数据</a></span></li><li><span><a href="#基金单位净值和累计净值" data-toc-modified-id="基金单位净值和累计净值-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>基金单位净值和累计净值</a></span></li><li><span><a href="#补充数据" data-toc-modified-id="补充数据-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>补充数据</a></span></li></ul></li><li><span><a href="#基金收益指标" data-toc-modified-id="基金收益指标-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>基金收益指标</a></span><ul class="toc-item"><li><span><a href="#日收益率序列" data-toc-modified-id="日收益率序列-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>日收益率序列</a></span></li><li><span><a href="#累计收益率" data-toc-modified-id="累计收益率-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>累计收益率</a></span></li><li><span><a href="#年化收益率" data-toc-modified-id="年化收益率-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>年化收益率</a></span></li></ul></li><li><span><a href="#基金风险指标" data-toc-modified-id="基金风险指标-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>基金风险指标</a></span><ul class="toc-item"><li><span><a href="#收益率波动率" data-toc-modified-id="收益率波动率-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>收益率波动率</a></span></li><li><span><a href="#下行风险" data-toc-modified-id="下行风险-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>下行风险</a></span></li><li><span><a href="#最大回撤" data-toc-modified-id="最大回撤-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>最大回撤</a></span></li><li><span><a href="#跟踪误差" data-toc-modified-id="跟踪误差-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>跟踪误差</a></span></li><li><span><a href="#VaR" data-toc-modified-id="VaR-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>VaR</a></span></li><li><span><a href="#CVaR" data-toc-modified-id="CVaR-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>CVaR</a></span></li><li><span><a href="#贝塔Beta" data-toc-modified-id="贝塔Beta-3.7"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>贝塔Beta</a></span></li></ul></li><li><span><a href="#风险调整收益指标" data-toc-modified-id="风险调整收益指标-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>风险调整收益指标</a></span><ul class="toc-item"><li><span><a href="#詹森Alpha" data-toc-modified-id="詹森Alpha-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>詹森Alpha</a></span></li><li><span><a href="#夏普比率" data-toc-modified-id="夏普比率-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>夏普比率</a></span></li><li><span><a href="#信息比率" data-toc-modified-id="信息比率-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>信息比率</a></span></li><li><span><a href="#索提诺比率" data-toc-modified-id="索提诺比率-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>索提诺比率</a></span></li><li><span><a href="#卡玛比率" data-toc-modified-id="卡玛比率-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>卡玛比率</a></span></li><li><span><a href="#欧米伽比率" data-toc-modified-id="欧米伽比率-4.6"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>欧米伽比率</a></span></li><li><span><a href="#特雷诺比率" data-toc-modified-id="特雷诺比率-4.7"><span class="toc-item-num">4.7&nbsp;&nbsp;</span>特雷诺比率</a></span></li><li><span><a href="#M2" data-toc-modified-id="M2-4.8"><span class="toc-item-num">4.8&nbsp;&nbsp;</span>M2</a></span></li><li><span><a href="#Manipulation-Proof-统计量" data-toc-modified-id="Manipulation-Proof-统计量-4.9"><span class="toc-item-num">4.9&nbsp;&nbsp;</span>Manipulation-Proof 统计量</a></span></li></ul></li><li><span><a href="#其他指标" data-toc-modified-id="其他指标-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>其他指标</a></span><ul class="toc-item"><li><span><a href="#业绩持续性" data-toc-modified-id="业绩持续性-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>业绩持续性</a></span></li><li><span><a href="#选股择时能力" data-toc-modified-id="选股择时能力-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>选股择时能力</a></span></li></ul></li><li><span><a href="#与其他基金对比" data-toc-modified-id="与其他基金对比-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>与其他基金对比</a></span></li><li><span><a href="#Brinson业绩归因" data-toc-modified-id="Brinson业绩归因-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Brinson业绩归因</a></span><ul class="toc-item"><li><span><a href="#单期Brinson模型" data-toc-modified-id="单期Brinson模型-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>单期Brinson模型</a></span></li><li><span><a href="#多期Brinson模型" data-toc-modified-id="多期Brinson模型-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>多期Brinson模型</a></span></li></ul></li><li><span><a href="#Barra风险收益归因" data-toc-modified-id="Barra风险收益归因-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Barra风险收益归因</a></span><ul class="toc-item"><li><span><a href="#Barra风格因子" data-toc-modified-id="Barra风格因子-8.1"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>Barra风格因子</a></span></li><li><span><a href="#Barra风格分解结果" data-toc-modified-id="Barra风格分解结果-8.2"><span class="toc-item-num">8.2&nbsp;&nbsp;</span>Barra风格分解结果</a></span></li></ul></li><li><span><a href="#参考文献" data-toc-modified-id="参考文献-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>参考文献</a></span></li><li><span><a href="#附录" data-toc-modified-id="附录-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>附录</a></span><ul class="toc-item"><li><span><a href="#附录1：代码使用指南" data-toc-modified-id="附录1：代码使用指南-10.1"><span class="toc-item-num">10.1&nbsp;&nbsp;</span>附录1：代码使用指南</a></span></li><li><span><a href="#附录2：同类型基金指标计算结果（排名前十）" data-toc-modified-id="附录2：同类型基金指标计算结果（排名前十）-10.2"><span class="toc-item-num">10.2&nbsp;&nbsp;</span>附录2：同类型基金指标计算结果（排名前十）</a></span></li><li><span><a href="#附录3：Brinson行业分解结果" data-toc-modified-id="附录3：Brinson行业分解结果-10.3"><span class="toc-item-num">10.3&nbsp;&nbsp;</span>附录3：Brinson行业分解结果</a></span></li></ul></li></ul></div>

<div STYLE="page-break-after: always;"></div>

# 数据来源

## 原始数据

原始数据官网来自[易方达消费行业股票110022](http://www.efunds.com.cn/html/fund/110022_fundvalue.htm)，下载从基金成立期初`2010/8/20`到`2021/6/8`的数据。

## 基金单位净值和累计净值

- 基金单位净值：是指每份基金份额的净值，它等于基金净资产除以基金总份额。
- 基金资产净值：基金累计净值：是指基金单位净值与成立以来的基金分红之和，体现了基金从成立以来所取得的累计收益。
- 累计净值=单位净值+累计基金分红。
- 据统计，易方达消费行业股票基金基金单位净值=基金资产净值，在后续的处理中保留一个即可。

参考链接：[彻底搞懂基金单位净值和累计净值](https://xueqiu.com/6320156356/144924785)

## 补充数据

- 无风险收益率数据采用的是从wind宏观数据库中提取十年期国债收益率数据（代码：`MM0325687` ），起始日期为`2015/1/4`
- 市场组合数据采用的是从wind API中提取的中证全指收盘价数据（代码：`000985.CSI`）,起始日期为`2010/8/20`
- 据统计，易方达消费行业股票基金基准不曾发生变化（`fund_changeofbenchmark`）
- 基准数据采用的是中证内地消费主题指数（代码：`000942.CSI`）收益率* 85 + 中债总指数（Wind宏观经济数据库，代码：`M0051553`）收益率 * 15%，起始日期为`2010/8/20`

所有指标需要用到的外部数据情况如下图所示。

![](result/指标所需外部数据.jpg)

<center> <font size=2><b> 图2：课题计算的指标所需外部数据</b> </font></center>
<div STYLE="page-break-after: always;"></div>

# 基金收益指标

基金的投资收益是持有基金需要关注的第一个指标，常见的有日收益率、累积收益率、年化收益率、最大净值和最小净值。这些指标都可以根据投资时段进行相应的调整计算。

<center> <font size=2><b> 表1：基金收益指标含义与公式</b> </font></center>

| 名称                           | 含义                                                         | 公式                                                         |
|------------------------------ |------------------------------------------------------------ |------------------------------------------------------------ |
| 日收益率`Dayret`               | 投资组合的日度收益率序列                                     | $R_t=\frac{nav_t-nav_{t-1}}{nav_{t-1}}$                      |
| 累积收益率`Cumret`             | 投资组合从期初持有到期末的收益占本金的比例                   | $R_{t}^{cum}=\frac{nav_t-nav_0}{nav_0}$                      |
| 年化收益率`Compoundedret`      | 投资期内收益率按照年进行复利计算调整                         | $R_t^{annul}={nav_t}^{\frac{N}{t}}-1$                        |
| 净值的最高点`Stats`            | 期初持有起的最大净值                                         | $max_{i=1}^{t}(nav_i)$                                       |
| 净值的均值`Stats` | 期初持有起的净值的均值 | $sum_{i=1}^{t}\frac{nav_i}{t}$ |
注：

- 每日的投资组合净值为$nav_t$；$nav_0$一般归一化为1

- $N$为$s_i$的周期对应的天数，比如一年的天数

易方达消费行业股票基金成立期初持有至今的累计收益率为**430%**，年化收益率为**17.45%**。基金稳定运行三年后除2018年年化收益率和累计收益率均为正值。

<center> <font size=2><b> 表2：基金收益指标分年表现</b> </font></center>

|      | 年化收益率                              | 累计收益率                              |
| ---- | --------------------------------------- | --------------------------------------- |
| 2010 | <font color=#FF0000>-0.13903</font>     | <font color=#FF0000>-0.034</font>       |
| 2011 | <font color=#FF0000>-0.15717</font>     | <font color=#FF0000>-0.15314</font>     |
| 2012 | <font color=#FF0000>-0.00384</font>     | <font color=#FF0000>-0.0037</font>      |
| 2013 | 0.187664                                | 0.176326                                |
| 2014 | 0.077801                                | 0.075551                                |
| 2015 | 0.224722                                | 0.216834                                |
| 2016 | 0.150474                                | 0.145985                                |
| 2017 | 0.657851                                | 0.634642                                |
| 2018 | <font color=#FF0000>   -0.24505 </font> | <font color=#FF0000>   -0.23826 </font> |
| 2019 | 0.759284                                | 0.727891                                |
| 2020 | 0.731252                                | 0.697515                                |

<div STYLE="page-break-after: always;"></div>

## 日收益率序列

日收益率序列的时间序列分析是分析资产收益的第一步，也是后续业绩评价指标的基础。分为简单收益率和对数收益率两种。其收益率分布的特点会影响后续指标的计算，比如夏普比率假设资产组合收益率服从正态分布。

**分析**：因为偏度小于0，收益率序列存在一定程度的左偏，峰度大于3，相比正态分布更加陡峭，存在一定程度的尖峰厚尾的现象。

<img src="result/Dailyret_line.png" div align=center style="zoom:20%;" />

<center><font size=2><b> 图3：易方达消费行业基金日收益率序列</b> </font></center>


| <img src="result/Dailyret_dist.png" style="zoom:20%;" /> <br><center><font size=2><b> 图4：易方达消费行业基金日收益率分布</b> </font></center> | <img src="result/Dailyret_box.png" style="zoom:20%;" /><br/><center><font size=2><b> 图5：易方达消费行业基金日收益率箱线图</b> </font></center> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

<div STYLE="page-break-after: always;"></div>

<center> <font size=2><b> 表3：易方达消费行业基金日收益率统计指标</b> </font></center>


| 指标         | 数值               |
| ------------ | ------------------ |
| 总数         | 2600               |
| 最小值       | -0.080162          |
| 最小值位置   | 2272（2020-01-23） |
| 25%分位数    | -0.006993          |
| 中位数       | 0.000969           |
| 75%分位数    | 0.009058           |
| 均值         | 0.000766           |
| 最大值       | 0.081425           |
| 最大值位数   | 1157（2015-07-09） |
| 平均绝对偏差 | 0.010718           |
| 方差         | 0.000220           |
| 标准差       | 0.014824           |
| 偏度         | -0.378354          |
| 峰度         | 3.347741           |

<div STYLE="page-break-after: always;"></div>

## 累计收益率

累计收益率的计算公式如下，其中$nav_0$一般为1
$$
R_{t}^{cum}=\frac{nav_t-nav_0}{nav_0}\\
$$
画出整个基金存续期间的累计收益率情况如图6所示：

<img src="result/Cumret_line.png" style="zoom:20%;" />

<center><font size=2><b> 图6：易方达消费行业基金累计收益率</b> </font></center>

## 年化收益率

年化收益率的计算公式如下，其中$N$为一年的天数，在计算中取251天：
$$
R_t^{annul}={nav_t}^{\frac{N}{t}}-1\\
(R_t^{annul}+1)^t={nav_t}^N
$$
**分析**：从基金成立期初开始的年化收益率如图7所示，其从期初持有的年化收益率从第三年开始平稳增加。投资三个月的滚动收益率时间序列图如图8所示、分布图如图9所示，可以看出大部分时间呈现正的收益。

<img src="result/Compoundedret_line.png" style="zoom:20%;" />

<center><font size=2><b> 图7：易方达消费行业基金从期初开始的年化收益率</b> </font></center>

| <img src="result/rolling/Compoundedret_line.png" style="zoom:20%;" /><br><font size=2><b> 图8：易方达消费行业基金3个月滚动投资的年化收益率</b> </font> | <img src="result/rolling/Compoundedret_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图9：易方达消费行业基金3个月滚动投资的年化收益率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

  

<div STYLE="page-break-after: always;"></div>

# 基金风险指标

最低净值、净值的波动是描述基金风险的直观指标，根据马科维茨模型，收益的波动率也是表述风险的基本指标，但是收益率分布的尖峰厚尾的特点，收益率分布的高阶矩比如峰度和偏度也会在考察的范围内。由于收益率波动率存在没有区分正向和负向波动的特点，下行风险对其进行了补充。最大回撤是常用的风险衡量指标，但也受时间段的约束。针对指数基金等被动型投资产品，跟踪误差是主要衡量指标。VaR和CVaR衡量的是组合在尾部的损失情况，常用于风险的计量。$\beta$来源于CAPM模型，用回归的方式计量组合相对于市场组合的系统性风险。这些风险指标的计算会受到不同时间窗口长度的影响，采用滚动的方式计算在时间序列的比较上更有意义。

<center> <font size=2><b> 表4：基金风险指标含义与公式</b> </font></center>

| 名称                           | 含义                                                         | 公式                                                         |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 净值的最低点`Stats`            | 期初持有起的最小净值                                         | $min_{i=1}^{t}(nav_i)$                                       |
| 净值的标准差`Stats`            | 期初持有起的净值的波动率                                     | $\sqrt{\frac{\sum_{i=1}^t (nav_{i}-\overline{nav_i})^2}{(t-1)}}$ |
| 收益率年化标准差`Annulstd`     | 日度收益率数据的年化波动率                                   | $S_i=\sqrt{\frac{\sum_{t=1}^T (R_{it}-\overline{R_i})^2}{(T-1)}}×\sqrt{N}$ |
| 日收益率分布的峰度`Skew`       | 日度收益率数据的三阶矩                                       | $Skew_i=\frac{\sum_{t=1}^T (R_{it}-\overline{R_i})^3}{(T-1)s_i^3}$ |
| 日收益率分布的偏度`Kutrosis`   | 日度收益率数据的四阶矩                                       | $Kutrosis_i=\frac{\sum_{t=1}^T (R_{it}-\overline{R_i})^4}{(T-1)s_i^4}$ |
| 下行风险`Downsiderisk`         | 衡量投资组合向下波动的风险                                   | $Downsiderisk = \sqrt{\frac{\sum_{t=1}^T (min(0,(R_{it}-\overline{R_i})))^2}{T-1}}$ |
| 最大回撤`MaxDrawdown`          | 历史区间内的最大跌幅                                         | $MaxD_t=max(0,min_{s<t}({\frac{nav_t}{nav_s}-1)})$           |
| 最大亏损`MaxLoss`              | 投资期内的最大亏损额                                         | $MaxL_t=max(0,min_{t}({\frac{nav_t}{nav_0}-1)})$             |
| 跟踪误差`Trackingerror`        | 投资组合收益率与基准组合收益率之间的偏差                     | $TE=\sqrt{\frac{\sum_{t=1}^T (R_{it}-\overline{R_{bent}})^2}{T-1}}$ |
| VaR`VaR`                       | 在概率水平$C$下，投资组合在未来特定时期内的最大可能损失      | $P(△nav_{△t}\leq VaR)=C$ <br>$ VaR=-\frac{1}{2}(X_{(n\alpha +1)}+X_{(n\alpha )})$ |
| CVaR/ Expected shortfall`CVaR` | 在投资组合的损失超过某个给定VaR值的条件下，该投资组合的平均损失值 | $CVaR=-\frac{1}{n\alpha}\sum_{i=1}^{n\alpha}X_{(i)}$         |
| 贝塔`Beta`                     | 投资组合相对于市场组合的系统性风险                           | $\beta=\frac{cov(R_p,R_m)}{\sigma_m^2}=\rho_{pm}\frac{\sigma_p}{\sigma_m}$ |

<div STYLE="page-break-after: always;"></div>

针对易方达消费行业股票基金计算的结果：

<center> <font size=2><b> 表5：基金风险指标分年表现</b> </font></center>

| 年份 | 收益率年化标准差 | 下行风险 | 最大回撤 | 最大亏损 | 在险价值 | 条件的VaR | 跟踪误差 | 贝塔     |
| ---- | ---------------- | -------- | -------- | -------- | -------- | --------- | -------- | -------- |
| 2010 | 1.228%           | 0        | -10.019% | -4.800%  | 2.157%   | 0.093%    | 1.228%   | -        |
| 2011 | 0.064%           | 0        | -19.189% | -17.140% | 2.397%   | 0.095%    | 0.064%   | -        |
| 2012 | 0.186%           | 0        | -19.978% | -10.111% | 2.709%   | 0.033%    | 0.186%   | -        |
| 2013 | 0.724%           | 0        | -11.284% | 0.000%   | 2.373%   | 0.040%    | 0.724%   | -        |
| 2014 | 0.379%           | 0.099%   | -12.802% | -12.802% | 2.301%   | 0.002%    | 0.379%   | -        |
| 2015 | 0.395%           | 9.65E-05 | -36.730% | -4.666%  | 5.952%   | 0.019%    | 0.395%   | 86.529%  |
| 2016 | 0.800%           | 0        | -16.640% | -15.085% | 3.325%   | 0.020%    | 0.800%   | 113.616% |
| 2017 | 0.974%           | 8.25E-05 | -9.284%  | -0.351%  | 2.777%   | 0.171%    | 0.974%   | 125.661% |
| 2018 | 0.048%           | 0        | -33.164% | -26.857% | 3.948%   | 0.152%    | 0.048%   | 86.432%  |
| 2019 | 0.999%           | 0        | -8.992%  | -1.587%  | 4.098%   | 0.182%    | 0.999%   | 117.240% |
| 2020 | 0.676%           | 0        | -17.879% | -15.435% | 3.889%   | 0.182%    | 0.676%   | 86.799%  |

<div STYLE="page-break-after: always;"></div>

## 收益率波动率

收益率年化标准差即波动率，衡量的是基金收益的波动幅度。其思想来源于马科维兹的组合优化模型，用方差和标准差来衡量组合的风险。其公式如下，其中N为$s_i$的周期对应的天数，在计算中使用一年251天：
$$
s_i=\sqrt{
\frac{\sum_{t=1}^T (R_{it}-\overline{R_i})^2}
{(T-1)}}\\
S_i=s_i ×\sqrt{N}\\
$$
**分析：**随着基金存续期的延长，易方达消费行业股票基金的年化波动率逐渐提高，并呈现两个平台期的情况，近三年来稳定在23%左右。从基金成立期初开始的年化收益率波动率如下图10所示。如果滚动窗口采取三个月，能更好的反映固定投资期内基金表现的情况，其时间序列和分布情况如图11、图12。

<img src="result/Annulstd_line.png" style="zoom:20%;" />

<center><font size=2><b> 图10：易方达消费行业基金从期初开始的收益率波动率</b> </font></center>

| <img src="result/rolling/Annulstd_line.png" style="zoom:20%;" /><br/><font size=2><b> 图11：易方达消费行业基金3个月滚动投资的收益率波动率</b> </font> | <img src="result/rolling/Annulstd_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图12：易方达消费行业基金3个月滚动投资的收益率波动率</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



<div STYLE="page-break-after: always;"></div>

## 下行风险

下行风险对波动率进行改进，即只考虑亏损时的波动情况，公式如下：
$$
Downsiderisk = \sqrt{\frac{\sum_{t=1}^T (min(0,(R_{it}-\overline{R_i})))^2}{T-1}}
$$
**分析：**易方达消费行业股票基金的下行风险随着时间的延长在逐渐降低，从基金成立期初开始的下行风险如下图所示：

<img src="result/Downsiderisk_line.png" style="zoom:20%;" />

<center><font size=2><b> 图13：易方达消费行业基金下行风险</b> </font></center>

## 最大回撤

最大回撤是指统计周期内的最大投资净值的时点往后推，当资产净值回落到最低点时，资产收益率的回撤幅度。其公式如下：
$$
MaxD_t=max(0,min_{s<t}({\frac{nav_t}{nav_s}-1)})
$$
从基金成立期初开始的最大回撤如下图所示：

<img src="result/MaxDrawdown_line.png" style="zoom:20%;" />

<center><font size=2><b> 图14：易方达消费行业基金最大回撤</b> </font></center>

**分析：**最大回撤并非一定是特定时间段内最大值减最小值，其计算还要考虑划定的时间范围和极值情况。最大回撤并不是一个完美的衡量风险的指标，因为其受时间段的约束。在此基础上，提出了最大回撤率、平均回撤、条件期望回撤等衍生指标。如果固定时间窗口为三个月，最大回撤的情况如下图所示,，其分布呈现左偏情况。

| <img src="result/rolling/MaxDrawdown_line.png" style="zoom:20%;" /><br/><font size=2><b> 图15：易方达消费行业基金3个月滚动投资的年化收益率</b> </font> | <img src="result/rolling/MaxDrawdown_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图16：易方达消费行业基金3个月滚动投资的最大回撤</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



## 跟踪误差

跟踪误差是指组合收益率与基准收益率之间的差异的收益率标准差，反映了基金管理的风险。其公式为：
$$
TE=\sqrt{\frac{\sum_{t=1}^T (R_{it}-\overline{R_{bent}})^2}{T-1}}
$$
**分析：**跟踪误差越大，说明基金的净值率与基准组合收益率之间的差异越大，并且基金经理主动投资的风险越大。通常认为指数基金的跟踪误差在2％以上意味着差异比较显著。由于易方达消费行业基金属于主动投资基金，其跟踪误差并不是描述其风险的主要指标。

<img src="result/Trackingerror_line.png" style="zoom:20%;" />

<center><font size=2><b> 图17：易方达消费行业基金跟踪误差</b> </font></center>



<div STYLE="page-break-after: always;"></div>

## VaR

在险价值VaR(Value at Risk)指：在一定概率水平下，资产或组合价值在未来特定时期内的最大可能损失。置信水平反映了金融资产管理者的风险厌恶程度，可根据不同的投资者对风险的偏好程度和承受能力来确定。其表达式如下：
$$
P(△nav_{△t}\leq VaR)=C
$$
**分析：**VaR的计量分为参数法、历史法和蒙特卡洛模拟法。下图为采用历史法计量的5%的VaR从期初开始的情况。可见，当前，易方达消费行业基金在5%的可能下会达到最大损失4%。如果滚动窗口采取三个月，可以明显观察到$VaR$在2015年9月达到峰值，存在严重的尾部效应。

<img src="result/his_VaR_line.png" style="zoom:20%;" />

<center><font size=2><b> 图18：易方达消费行业基金VaR</b> </font></center>

| <img src="result/rolling/his_VaR_line.png" style="zoom:20%;" /><br/><font size=2><b> 图19：易方达消费行业基金3个月滚动投资的VaR</b> </font> | <img src="result/rolling/his_VaR_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图20：易方达消费行业基金3个月滚动投资的VaR</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

<div STYLE="page-break-after: always;"></div>

## CVaR

条件风险价值CVaR(Conditional Value-at-Risk)，又称average value at risk（AVaR), 和expected tail loss (ETL)。
CVaR是是在$ \alpha$%置信水平下的低于$ \alpha$%的损失平均值。它对损失的分布的尾部风险的敏感度更高。ES对估计投资风险来说相对比较有说服力，它主要聚焦在投资的非盈利部分。可以通过调整置信水平$ \alpha$%来改变其关注点。
当使用历史法计算VaR和CVaR时，设$X_1, X_2,...,X_n$是来自资产收益率的一个样本。当样本容量较大时，对样本进行排序得到次序统计量$X_{(1)}<X_{(2)}<...<X_{(n)} $, 样本-a分位数为$X_{(n\alpha)}$或$X_{(n\alpha +1)}$.
$$
VaR=-\frac{1}{2}(X_{(n\alpha +1)}+X_{(n\alpha )})\\
CVaR=-\frac{1}{n\alpha}\sum_{i=1}^{n\alpha}X_{(i)}
$$

**分析：**历史法计量的基金期初成立至今的CVaR如下图所示，在5%的置信水平下低于5%的损失平均值均小于0.2%。

<img src="result/his_CVaR_line.png" style="zoom:20%;" />

<center><font size=2><b> 图21：易方达消费行业基金CVaR</b> </font></center>

<div STYLE="page-break-after: always;"></div>

## 贝塔Beta

贝塔系数用于评估证券系统性风险，反映了组合相对市场变化的敏感性，通过资产收益率与市场组合收益率回归的方式计算可得。其公式为：
$$
\beta=\frac{cov(R_p,R_m)}{\sigma_m^2}=\rho_{pm}\frac{\sigma_p}{\sigma_m}
$$

**分析：**通过市场风险溢价$R_m-r_f$与超额收益$R_p-r_f$进行线性回归可以得到从2015年开始的$\beta$的时间序列图和分布图，如下图所示。从趋势上看，$\beta$从2019年年中开始有增加的趋势，从分布上看，$\beta$存在尖峰厚尾的情况。

| <img src="result/Beta_line.png" style="zoom:20%;" /><br/><font size=2><b> 图22：易方达消费行业基金3个月滚动投资的BETA</b> </font> | <img src="result/Beta_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图23：易方达消费行业基金3个月滚动投资的BETA</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

<div STYLE="page-break-after: always;"></div>

# 风险调整收益指标

风险调整收益是应用于投资的风险评估计算的数值。投资产生的收益与投资的风险进行比较，得出一个比率。风险调整收益可应用于单个证券、证券组合，不同形式的风险度量为投资者提供了评估风险调整后收益的不同方法。以下列举的都是常见的风险调整收益指标，其中夏普比率、特雷诺指数和詹森指数是最常用的风险调整收益指标。

<center> <font size=2><b> 表6：风险调整收益指标含义与公式</b> </font></center>

| 名称                      | 含义                                                         | 公式                                                         |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 詹森`alpha Jasens`        | 剥离市场风险后的超额收益                                     | $\alpha=R_t-(r_f+\beta(R_m-r_f))$                            |
| 夏普比率`Sharp`           | 单位总风险获得的超额收益                                     | $Sharp=\frac{E(R_t)-R_{f}}{s_i}$                             |
| 信息比率`information`     | 单位主动风险获得的超额收益                                   | $Infor=\frac{E(R_t)-R_{ben}}{TE}$                            |
| 索提诺比率`Sortino`       | 单位下行风险获得的超额收益                                   | $Sortino=\frac{E(R_t)-R_f}{Downsiderisk}$                    |
| 卡玛比率`Calmar`          | 单位最大回撤获得的超额收益                                   | $Calmar=\frac{R_t-R_{f}}{MaxD_t}$                            |
| 欧米伽比率`Omega`         | 加权收益比上加权损失                                         | $\Omega(R_{goal})=\frac{\int_{R_{goal}}^{\infty}(1-F(R_t-r_f))d(R_t-r_f)}{\int_{-\infty }^{R_{goal}}(F(R_t-r_f))d(R_t-r_f)}$ |
| Manipulation-Proof 统计量 | 采用Cornish Fisher框架来纠正尾部风险对收益进行调整           | $MPPM=\frac{1}{(1-\gamma)△t}ln(\frac{1}{T}\sum_{t=1}^T[\frac{1+R_t-r_f}{1+R_{ben}-r_f}]^{1-\gamma})$ |
| 特雷诺比率`Treynor`       | 单位系统性风险获得的超额收益                                 | $Treynor=\frac{R_t-R_{f}}{\beta}$                            |
| $M^2$                     | 让投资者评价资产的风险相对于市场风险的补偿收益，$\gamma$可以理解为杠杆系数 | $M^2=\gamma *(E(R_t)-r_f)+rf$<br>$\gamma=\frac{\sigma_{mkt}}{\sigma_{R_t}}$ |

<div STYLE="page-break-after: always;"></div>

以下是针对易方达消费行业股票基金计算的结果，其中索提诺比率的缺失值是因为分母下行风险为0所导致的。



<center> <font size=2><b> 表7：风险调整收益指标分年表现</b> </font></center>

|                          | 2015     | 2016     | 2017     | 2018     | 2019     | 2020     |
| ------------------------ | -------- | -------- | -------- | -------- | -------- | -------- |
| 年化夏普比率             | 0.6910   | 0.6186   | 2.9928   | -1.0422  | 2.5074   | 2.1799   |
| 夏普比率                 | 0.0431   | 0.0386   | 0.1866   | -0.0649  | 0.1563   | 0.1356   |
| 索提诺比率               | 10.4158  | -        | -        | -4.3542  | -        | -        |
| 卡玛比率                 | -0.0027  | -0.0033  | -0.0213  | 0.0033   | -0.0253  | -0.0125  |
| 欧米伽比率               | 1.1274   | 1.1177   | 1.6368   | 0.8437   | 1.5378   | 1.4374   |
| 信息比率                 | 0.0397   | -0.1424  | 0.0661   | -0.1919  | -0.1607  | -0.2710  |
| 詹森                     | -0.0075  | 0.0027   | 0.0174   | 0.0038   | 0.0133   | 0.0042   |
| 特雷诺比率               | 0.0013   | 0.0005   | 0.0017   | -0.0012  | 0.0020   | 0.0027   |
| M2                       | 0.0012   | 0.0007   | 0.0014   | -0.0008  | 0.0021   | 0.0021   |
| Manipulation-Proof统计量 | -21.9423 | -21.8568 | -22.2252 | -22.0903 | -21.5967 | -21.8612 |

<div STYLE="page-break-after: always;"></div>

## 詹森Alpha

Jensen alpha是资产超额收益与CAPM模型预测收益的差。资产的理论收益一般由市场模型确定比如最常用的资本资产定价模型。**CAPM模型使用$\beta$系数将市场风险进行调整**，其得到的理论预期收益称为“已经过风险调整”的收益。其公式如下：
$$
\alpha=R_t-(r_f+\beta(R_m-r_f))
$$
$\beta$越高，说明风险越高，理论预期收益率越高。如果一个资产的实际收益率高于风险调整后的理论预期收益率，这样的资产就被称为有“正的α”或者“超额收益”。 

詹森指数有以下几个缺点：

- 衡量的是投资组合的选择收益，未对市场择时能力做出评价
- 以SML为研究的基点，假设,即基金的非系统风险已通过投资组合彻底的分散掉，与实际不一定相符，尤其是采用积极管理策略的投资基金
- 忽略了基金投资组合中所含证券的数目，即基金投资组合的广度,而只考虑了获得超额收益的大小，也就是基金投资组合的深度

**分析**：从2015年开始的詹森指数的时间序列图和分布图如下图所示，可以看出，$\alpha$的均值在0的附近，从长期来看主动基金在CAPM的框架下无法获得超额收益。如果滚动窗口采取三个月，可以明显观察到$\alpha$的趋势，且其分布更接近与正态分布。

| <img src="result/Jasens_line.png" style="zoom:20%;" /><br/><font size=2><b> 图24：易方达消费行业基金从期初开始的詹森alpha</b> </font> | <img src="result/Jasens_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图25：易方达消费行业基金从期初开始的詹森alpha分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

| <img src="result/rolling/Jasens_line.png" style="zoom:20%;" /><br/><font size=2><b> 图26：易方达消费行业基金3个月滚动投资的詹森alpha</b> </font> | <img src="result/rolling/Jasens_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图27：易方达消费行业基金3个月滚动投资的詹森alpha分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



## 夏普比率

夏普比率定义为投资收益的期望收益率与无风险收益率的差与投资收益的标准差的比率，衡量的是**每单位总风险所带来的的超额收益**。其公式如下：
$$
Sharp=\frac{E(R_t)-R_{f}}{s_i}
$$
年化夏普比率的计算需要对分子分母分别进行年化，公式如下：
$$
Sharp=\frac{E(R_t^{annul})-R_{f}^{annul}}{S_i}
=\frac{{nav_t}^{\frac{N}{t}}-{nav_{f}}^{\frac{N}{t}}}{S_i}\\
s_i=\sqrt{
\frac{\sum_{t=1}^T (R_{it}-\overline{R_i})^2}
{(T-1)}}\\
S_i=s_i ×\sqrt{N}\\
$$

夏普比率基本上是最常用的投资性能评价指标，它非常直观，可解释性很强。但是它有如下缺点：

- 用标准差定义风险并不是非常合理，因为标准差对上下行波动的权重是一样的。
- 不能捕捉一些风险资产的流动性问题。
- 不能完全表示不同的投资者对待风险的态度。
- 假设无风险利率的借入和借出是一样的。
- 依赖一阶和二阶统计量的估算的稳定性。
- 是一个序数统计量。即绝对数值的大小不可比，$M^2$测度弥补了这个缺陷。
- 对于非正态分布数据或者高频数据结果不稳定。Bailey和López de Prado（2012）提出了概率夏普比率以应对收益分布的不对称性和肥尾效应。
- 对于较好的投资技巧所呈现的正偏度和负向超额峰度会收缩；对于不好的投资显示的负偏度和正向超额峰度会放大。

**分析**：从2015年开始的夏普比率如下图所示，基金成立期初由于受到基金新发行溢价的影响，其夏普比率比较异常，后来保持相对稳定，在0.1左右。如果滚动窗口采取三个月，可以明显观察到夏普比率的趋势，在基金盈利大于无风险收益率的时候，夏普都为正值，固定时间窗口时其分布更分散。

| <img src="result/Sharp_line.png" style="zoom:20%;" /><br/><font size=2><b> 图28：易方达消费行业基金从期初开始的夏普比率</b> </font> | <img src="result/Sharp_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图29：易方达消费行业基金从期初开始的夏普比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

| <img src="result/rolling/Sharp_line.png" style="zoom:20%;" /><br/><font size=2><b> 图30：易方达消费行业基金3个月滚动投资的夏普比率</b> </font> | <img src="result/rolling/Sharp_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图31：易方达消费行业基金3个月滚动投资的夏普比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

## 信息比率

$IR_i$表示基金$i$的信息比率，其中分子表示基金$i$的跟踪偏离度的样本均值，分母$TE_i$为基金$i$的跟踪误差。信息比率是从**主动管理的角度描述风险调整后收益**，而夏普比率描述的是单位总风险带来的绝对超额收益。信息比率越大，说明基金经理单位跟踪误差所获得的超额收益越高，因此，信息比率较大的基金的表现要优于信息比率较低的基金。其公式如下：

$$
IR_i=\frac{R_t-R_{ben}}{TE}
$$
**分析：**从基金期初开始的信息比率如下图所示，可以看出除了基金成立期初信息比率波动较大，后期存在少数异常值外，信息比率的均值在1左右。如果滚动窗口采取三个月，信息比率的均值更加接近0，与我们的预期相符合：投资期限越长，主动基金获取额外信息取得收益更能够在市场上实现。

| <img src="result/Information_line.png" style="zoom:20%;" /><br/><font size=2><b> 图32：易方达消费行业基金从期初开始的信息比率</b> </font> | <img src="result/Information_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图33：易方达消费行业基金从期初开始的信息比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

| <img src="result/rolling/Information_line.png" style="zoom:20%;" /><br/><font size=2><b> 图34：易方达消费行业基金3个月滚动投资的信息比率</b> </font> | <img src="result/rolling/Information_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图35：易方达消费行业基金3个月滚动投资的信息比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



## 索提诺比率

索提诺比率衡量的是**单位下行风险获得的超额收益**，主要针对夏普比率没有区分上行风险和下行风险这个缺点提出的。
$$
Sortino=\frac{E(R_t)-R_f}{Downsiderisk}
$$

**分析：**从2015年开始的索提诺比率如下图所示，其分布比较接近与幂律分布（power law distribution）。如果滚动窗口采取三个月，其分布更接近于尖峰厚尾的“正态分布”。

| <img src="result/Sortino_line.png" style="zoom:20%;" /><br/><font size=2><b> 图36：易方达消费行业基金从期初开始的索提诺比率</b> </font> | <img src="result/Sortino_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图37：易方达消费行业基金从期初开始的索提诺比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

| <img src="result/rolling/Sortino_line.png" style="zoom:20%;" /><br/><font size=2><b> 图38：易方达消费行业基金3个月滚动投资的索提诺比率</b> </font> | <img src="result/rolling/Sortino_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图39：易方达消费行业基金3个月滚动投资的索提诺比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



## 卡玛比率

夏普比率和卡玛比率的唯一不同之处就是分母不同，一个使用标准差作为风险，一个使用最大回撤作为风险，本质上都是衡量基金的风险-回报关系。
$$
Calmar=\frac{R_t-R_{f}}{MaxD_t}\\
MaxD_t=max(0,min_{s<t}({\frac{nav_t}{nav_s}-1)})
$$

**分析：**从2015年开始的滚动时间窗口为三个月的卡玛比率如下图所示。根据定义，右偏的卡玛比率意味着基金表现较好。

| <img src="result/rolling/Calmar_line.png" style="zoom:20%;" /><br/><font size=2><b> 图40：易方达消费行业基金3个月滚动投资的卡玛比率</b> </font> | <img src="result/rolling/Calmar_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图41：易方达消费行业基金3个月滚动投资的卡玛比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



## 欧米伽比率

2002年，Shadwick和Keating提出了一个新的业绩衡量指标，Omega比率。该指标**考虑了收益率的整个分布信息**，因此包括了所有高阶矩的信息。作为投资绩效主要的评级依据，Omega比率在国外已经受到业界认可。其定义如下：
$$
\Omega(R_{goal})=\frac{\int_{R_{goal}}^{\infin}(1-F(R_t-r_f))d(R_t-r_f)}{\int_{-\infin }^{R_{goal}}(F(R_t-r_f))d(R_t-r_f)}
$$

其中，r为指定的临界收益率，F(x)为收益率的累计分布函数。Omega比率利用了收益率分布的所有信息，考虑了所有的高阶矩，刻画了收益率风险的所有特征。取不同的临界收益率，可以得到关于r 递减的Omega 函数。在临界收益率等于均值的时候，Omega 比率等于1。在相同的临界收益率下，对于不同的投资选择，Omega比率值越高，投资绩效也就越好。Omega比率同时捕捉了资产的上下行潜在收益，它描述了在目标收益以上的收益的潜在概率和目标收益以下收益的比率。

**分析：**从2015年开始的滚动时间窗口为三个月米伽比率如下图所示，可以看出欧米伽比率呈现左偏，基金在这个指标上表现较好。

| <img src="result/rolling/Omega_line.png" style="zoom:20%;" /><br/><font size=2><b> 图42：易方达消费行业基金3个月滚动投资的欧米茄比率</b> </font> | <img src="result/rolling/Omega_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图43：易方达消费行业基金3个月滚动投资的欧米茄比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



## 特雷诺比率

特雷诺比率衡量的是**单位系统性风险带来的超额收益**。特雷诺认为,基金管理者通过投资组合应消除所有的非系统性风险,因此特雷诺用单位系统性风险系数所获得的超额收益率来衡量投资基金的业绩。足够分散化的组合没有非系统性风险，仅有与市场变动差异的系统性风险。因此，他采用基金投资收益率的βp系数作为衡量风险的指标。
$$
Treynor=\frac{E(R_t)-R_{f}}{\beta}
$$

特雷诺比率的缺陷主要有以下两点：

- 在特雷诺比率中，仅适用组合的系统性风险衡量风险，即**假设已经将非系统风险完全分散掉**，但在实际操作过程中，基金的风险并非完全分散化的，除非组合的权重已经得到了优化，否则可能存在较大误差。
- 比率的分子和分母口径不匹配，分子是基金投资组合的总超额收益，分母是基金管理人承担的系统风险水平，分子没有剔除市场风险带来的收益，即同一支基金在牛市时，特雷诺指数也会比在熊市时大，因为市场风险的单位价格较高，而并不能反映基金管理人的经营能力强。如果市场的状况不同，用特雷诺比率进行绩效评价就变得没有意义了。所以，**特雷诺比率适用于基金的比较和选择，不适用于不同市场状况的分析**。

**分析**：从2015年开始的滚动时间窗口为三个月雷诺比率如下图所示，其数值较小。

| <img src="result/rolling/Treynor_line.png" style="zoom:20%;" /><br/><font size=2><b> 图44：易方达消费行业基金3个月滚动投资的特雷诺比率</b> </font> | <img src="result/rolling/Treynor_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图45：易方达消费行业基金3个月滚动投资的特雷诺比率分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



## $M^2$

$M^2$即Modigliani风险调整绩效指标，由JP Morgan公司的Leah Modigliani及其祖父诺贝尔经济学奖得主Franco Modigliani对夏普测度进行改进后引入的。其表达式如下：
$$
M^2=\gamma *(E(R_t)-r_f)+r_f\\
\gamma=\frac{\sigma_{mkt}}{\sigma_{R_t}}
$$
M2测度也是对总风险进行调整的，它反映资产组合同相应的无风险资产混合以达到同市场组合具有同样的风险水平时，混合组合的收益高出市场收益的大小。它**主要解决了夏普比率是序数统计量的缺陷**，即按照夏普比率排序和按照$M^2$测度排序的结果是一样的。

**分析：**从2015年开始的滚动时间窗口为三个月下图所示，相比夏普比率，其分布更接近正态分布。

| <img src="result/rolling/M2_line.png" style="zoom:20%;" /><br/><font size=2><b> 图46：易方达消费行业基金3个月滚动投资的M2</b> </font> | <img src="result/rolling/M2_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图47：易方达消费行业基金3个月滚动投资的M2分布图</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



## Manipulation-Proof 统计量

Manipulation-Proof 是2006年William Goetzmann, Jonathan Ingersoll提出的，他们**认为基金经理有操纵已有的业绩评价指标的“博弈”倾向**，所以提出了MPPM这个新的评价指标。表达式如下：
$$
MPPM=\frac{1}{(1-\gamma)△t}ln(\frac{1}{T}\sum_{t=1}^T[\frac{1+R_t-r_f}{1+R_{ben}-r_f}]^{1-\gamma})
$$
其中，$\Delta t$是投资时间，以年来计算；$\gamma$是风险厌恶度。
MPPM主要采用Cornish Fisher框架来纠正尾部风险，主要是负偏度和峰度的影响。

从2015年开始的滚动时间窗口为三个月nipulation-Proof 如下图所示，可以看出其取值范围存在**明显的周期性**，即每年年底的时候会迅速升高，表明基金在年底的时候存在业绩压力。

| <img src="result/rolling/Manipulationprood_line.png" style="zoom:20%;" /><br/><font size=2><b> 图48：易方达消费行业基金3个月滚动投资的Manipulation-Proof </b> </font> | <img src="result/rolling/Manipulationprood_dist.png" style="zoom:20%;" /><br/><font size=2><b> 图49：易方达消费行业基金3个月滚动投资的Manipulation-Proof 分布图率</b> </font> |
| ------------------------------------------------------------ | ------------------------------------------------------------ |




<div STYLE="page-break-after: always;"></div>

# 其他指标

## 业绩持续性

除了基金的收益和风险，业绩持续性和平稳性也是重要的衡量指标，常见的有盈利频率以及一阶自回归系数。

<center> <font size=2><b> 表8：业绩持续性指标含义与公式</b> </font></center>

| 名称                            | 含义                                     | 公式                                                         |
| ------------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| 盈利频率`Winfreq` | 衡量盈利的持续性 | $W=\frac{\sum_{t=1}^Tmax(0,sign(R_t))}{n}$ |
| 自回归系数T`AR1T` | 衡量盈利的持续性 | $R_t=a+bR_{t-1}$ $b$的$T$检验统计量的p值     |





针对易方达消费行业股票基金计算的结果如下：

<center> <font size=2><b> 表9：业绩持续性指标分年表现</b> </font></center>

|      | AR1T     | Winfreq  |
| ---- | -------- | -------- |
| 2010 | 0.17696  | 0.482759 |
| 2011 | 0.492062 | 0.471311 |
| 2012 | 0.495894 | 0.46281  |
| 2013 | 0.79142  | 0.514768 |
| 2014 | 0.170489 | 0.512295 |
| 2015 | 0.555507 | 0.559671 |
| 2016 | 0.743806 | 0.487705 |
| 2017 | 0.922713 | 0.540984 |
| 2018 | 0.479625 | 0.444444 |
| 2019 | 0.057937 | 0.518519 |
| 2020 | 0.182301 | 0.619835 |

<div STYLE="page-break-after: always;"></div>

## 择时能力

基金的择时能力和选股能力是衡量基金经理的两个维度的指标。T-M模型和H-M模型是对CAPM模型的改进进而衡量择时能力。如果要更加精确的衡量择时能力可以加入持仓数据使用单期或者多期的Brinson模型进行计算。

<center> <font size=2><b> 表10：择时指标含义与公式</b> </font></center>

| 名称                    | 含义                              | 公式                                                         |
| ----------------------- | --------------------------------- | ------------------------------------------------------------ |
| T-M模型beta2 `TM_beta2` | $beta_2$用于判断基金的择时能力    | $R_t-r_f=\alpha +\beta_1(R_m-r_f)+\beta_2(R_m-r_f)^2$        |
| H-M模型beta2 `HM_beta2` | $beta_2$大于0代表基金具有择时能力 | $R_t-r_f=\alpha +\beta_1(R_m-r_f)+\beta_2(R_m-r_f)D$<br>$D=\left\{\begin{matrix}0,R_m<r_f & \\1,R_m>r_f & \end{matrix}\right.$ |

针对易方达消费行业股票基金计算的结果，可以看出易方达消费行业基金的**择时能力在近四年表现较好**。

<center> <font size=2><b> 表11：业绩持续性指标分年表现</b> </font></center>

|          | 2015     | 2016     | 2017     | 2018     | 2019     | 2020     |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| HM_beta2 | 0.002314 | 0.002455 | 0.015496 | 0.004002 | 0.010848 | 0.012    |
| TM_beta2 | -2.51895 | -47.9944 | 25.13715 | 35.56743 | 214.502  | 4.082392 |

<div STYLE="page-break-after: always;"></div>

# 与其他基金对比

本课题从wind数据库提取了市场上521支股票型基金的净值数据对其相关指标进行计算，并计算其均值，与易方达消费行业基金的数据进行对比。结果发现，**易方达消费行业基金的累计收益率、收益率年化标准差、最大回撤、盈利频率这几个指标均好于同类型基金**。

<center> <font size=2><b> 表12：与同类型基金指标均值对比</b> </font></center>

| 指标             | 股票型基金均值 | 易方达消费行业 |
| ---------------- | -------------- | -------------- |
| 累计收益率       | 0.894629       | 4.3000         |
| 年化收益率       | 0.219978       | 0.1745         |
| 收益率年化标准差 | 0.232561       | 0.2350         |
| 下行风险         | 0              | 0.0007         |
| 最大回撤         | -0.26986       | -0.2586        |
| 最大亏损         | -0.13603       | -0.2710        |
| 盈利频率         | 0.494354       | 0.5142         |
| 自回归系数       | 0.430929       | 0.0427         |
| 在险价值         | 0.036552       | 0.0389         |
| 条件的VaR        | 0.000511       | 0.0003         |

<div STYLE="page-break-after: always;"></div>

# Brinson业绩归因

Brinson etal.,(1985,1986)认为，持有资产类别不变的情况下，组合通过改变各类资产权重而产生的超过基准的收益率，体现了组合在各类资产间的配置能力；保持各类资产权重不变的情况下，组合通过选择具体标的而产生的超越基准的收益率，体现了组合在各类资产的标的选择能力。简而言之，Brinson模型的核心思想就是基于组合和基准在样本期内的持仓数据，将组合的超额收益拆分到个股（券）选择能力（以下简称“选择能力”）和配置能力的测度指标上，从而达到对超额收益来源归因和对基金经理能力进行评价的目的。

实际上，Brinson模型可用于各类基金产品的绩效归因分析。如果用于混合型基金（即组合会配置股票、债券、商品、现金等多种大类资产），模型可以衡量基金经理在大类资产上的配置能力和在每种大类资产中选择具体标的的能力。如果用在股票型基金上（即组合主要配置的是股票资产），模型可以衡量基金经理在行业上的配置能力与每个行业内选股的能力。

## 单期Brinson模型

1986年Brinson，Hood和Beebower提出一种基于Brinson模型的超额收益拆分方案（简称“BHB方案”），该方案目前在业界应用较为广泛。BHB方案通过构建资产配置组合与标的选择组合这两个虚拟组合，将基金组合的超额收益分解为三个部分——配置收益（Allocation Return，AR）、个股（券）选择收益（简称“选择收益”，Selection Return，SR）、交互收益（Interaction Return，IR）。

假设基金经理在某一段期间内保持组合权重不变， 且组合没有现金流入和流出。 设$w_i^p$和$w_i^b$分别表示基金组合与基准组合中第$i$项资产的权重，$r_i^p$和$r_i^b$分别表示基金组合与基准组合中第$i$项资产的收益率，那么基金组合和基准组合的收益率分别为：  
$$
\begin{align}
R^p&=\sum_{i=1}^N w_i^pr_i^p\\
R^b&=\sum_{i=1}^N w_i^br_i^b
\end{align}
$$
对于资产配置，由于基金经理的目标是增持表现良好的资产类别，减持表现不佳的资产类别，那么如果我们固定基准组合里各类资产的收益率$r_i^b$不变，而将基准组合里各资产的权重$w_i^b$更改为基金组合里的实际权重$w_i^p$，此时所得到的加权总收益率反映的是仅做资产配置而不做标的选择时的组合收益率，也即前述资产配置虚拟组合的收益率，记为$R_A$，由于配置产生的超额收益记为$AR$。 
$$
R^A=\sum_{i=1}^N w_i^pr_i^b\\
AR=R^A-R^b=\sum_{i=1}^N (w_i^p-w_i^b)r_i^b
$$
对于标的选择，如果我们固定基准组合里各类资产的权重$w_i^b$不变，而将基准组合里各资产的收益率$r-i^b$更改为基金组合里的实际收益率$r_i^p$， 此时所得到的加权总收益率反映的是仅做标的选择而不做资产配置的合收益率，也即前述标的选择虚拟组合的收益率，记为$R_S$，由于配置产生的超额收益记为$SR$。
$$
R^S=\sum_{i=1}^N w_i^br_i^p\\
SR=R^A-R^b=\sum_{i=1}^N w_i^b(r_i^p-r_i^b)
$$
BHB 方案中，超额收益$R^p-R^b$减去配置收益 $AR$与选择收益 $AR$ 后的剩余收益， 称之为交互收益$IR$，反映了配置与选择的协同效应。配置收益，选择收益，交互收益三者共同构成了超额收益$RE$。  
$$
IR=R^p-R^b-AR-SR=\sum_{i=1}^N (w_i^p-w_i^b)(r_i^p-r_i^b)
$$
用坐标轴表示业绩分解情况如下图：

<img src="result/Brinson业绩归因.png" style="zoom:48%;" />

<center><font size=2><b> 图50：Brinson业绩归因示意图</b> </font></center>

用单期Brinson模型的BHB收益分解方案对易方达消费行业基金进行实证分析，业绩比较基准采用中证内地消费主题指数（代码：`000942.CSI`）收益率* 85 + 中债总指数（Wind宏观经济数据库，代码：`M0051553`）收益率 * 15%。单支股票的基准采用其所处的申万一级行业指数的数据。

由于基金的全部持仓为每半年披露一次，我们无法获取每日的具体持仓，因此只能简单假设2020年6月30日的持仓数据在2020年4月1日至2020年9月30日都保持不变，并且这一假设并不会严重影响归因分析的结果。

![](result/单期Brinson/单期Brinson分解.png)

<center><font size=2><b> 图51：Brinson每半年度业绩归因结果</b> </font></center>

每一期按照行业进行Brinson分解，可以看出行业配置存在收缩的情况，以最近两年为例，其余年份详见附录。

![](result/单期Brinson/20181231_brinson.png)

<center><font size=2><b> 图52：Brinson2018年下半年行业业绩归因结果</b> </font></center>

![](result/单期Brinson/20190630_brinson.png)

<center><font size=2><b> 图53：Brinson2019年上半年行业业绩归因结果</b> </font></center>

![](result/单期Brinson/20191231_brinson.png)

<center><font size=2><b> 图53：Brinson2019年下半年行业业绩归因结果</b> </font></center>



![](result/单期Brinson/20200630_brinson.png)

<center><font size=2><b> 图54：Brinson2020年上半年行业业绩归因结果</b> </font></center>

![](result/单期Brinson/20201231_brinson.png)

<center><font size=2><b> 图55：Brinson2020下半年行业业绩归因结果</b> </font></center>

<div STYLE="page-break-after: always;"></div>

## 多期Brinson模型

由于各期之间存在复利效应，因此需要进行多期归因。多期可以理解为每一个单独周期的组合。以下采用Carino算法进行推导。

分别考虑 t 期的基准累计收益率$R_p$和组合累计收益率 $R_b$：
$$
\begin{align}
1+R_t^p&=\prod_{i=1}^N(1+r_i^p)\\
1+R_t^b&=\prod_{i=1}^N(1+r_i^b)
\end{align}
$$
对两边取对数运算，再相减
$$
ln(1+R_t^p)=\sum_{i=1}^N ln(1+r_i^p)\\
ln(1+R_t^b)=\sum_{i=1}^N ln(1+r_i^b)\\
ln(1+R_t^p)-ln(1+R_t^b)=\sum_{i=1}^N [ln(1+r_i^p)-ln(1+r_i^b)]\\
\frac{ln(1+R_t^p)-ln(1+R_t^b)}{R_t^p-R_t^b}(R_t^p-R_t^b)=
\sum_{i=1}^N\frac{[ln(1+r_i^p)-ln(1+r_i^b)]}{r_t^p-r_t^b}(r_t^p-r_t^b)
$$
定义乘数因子
$$
\begin{align}
F_t&=\frac{ln(1+R_t^p)-ln(1+R_t^b)}{R_t^p-R_t^b}\\
f_t&=\sum_{i=1}^N\frac{[ln(1+r_i^p)-ln(1+r_i^b)]}{r_t^p-r_t^b}
\end{align}
$$
则有：
$$
R_t^p-R_t^b=\sum_{t=1}^N\frac{f_t}{F_t}(r_t^p-r_t^b)
=\sum_{t=1}^N\frac{f_t}{F_t}AR_t+\sum_{t=1}^N\frac{f_t}{F_t}SR_t+\sum_{t=1}^N\frac{f_t}{F_t}IR_t
=AR(t)+SR(t)+IR(t)
$$
对于易方达消费行业基金，多期的Brinson分解结果和单期的差别不大。

![](result/多期Brinson/多期Brinson分解.png)

<center><font size=2><b> 图56：Brinson多期业绩归因结果</b> </font></center>

每一期按照行业进行Brinson分解，同样以最近两年为例：

![](result/多期Brinson/20181231_brinson.png)

<center><font size=2><b> 图57：Brinson2018下半年多期行业业绩归因结果</b> </font></center>

![](result/多期Brinson/20190630_brinson.png)

<center><font size=2><b> 图58：Brinson2019上半年多期行业业绩归因结果</b> </font></center>

![](result/多期Brinson/20191231_brinson.png)

<center><font size=2><b> 图59：Brinson2019下半年多期行业业绩归因结果</b> </font></center>



![](result/多期Brinson/20200630_brinson.png)

<center><font size=2><b> 图60：Brinson2020上半年多期行业业绩归因结果</b> </font></center>

![](result/多期Brinson/20201231_brinson.png)

<center><font size=2><b> 图61：Brinson2020下半年多期行业业绩归因结果</b> </font></center>

本课题采用的“BHB”方案可能存在交互收益无法划分的情况，未来可以采用BF方案，即在计算配置收益时采取对标的资产基准收益扣减基准组合整体收益的操作， 降低了市场波动对单个资产配置收益测算的影响，使每个资产的 配置能力在不同市场条件下能够得到更客观的体现，同时不单列 BHB 方案中的含义不明的交互收益，能够更清晰地反映基金经理的在各资产类别上的 配置能力和选择能力。

在之后的研究中，在计算多期Brinson分解模型时，可以对比了常见的六种实现多期 Brinson 模型的算法进行分析，包括名义组合复合法 、AKH 算法 、Carino 算法  、Menchero 算法  、Frongello 算法 和GRAP算法。

<div STYLE="page-break-after: always;"></div>

# Barra风险收益归因

1974 年，美国学者 Barr Rosenberg 第一次提出采用多因子风险模型来对投资组合的风险和收益进行分析。多因子模型的基础理论认为：股票的收益是由一些共同的因子来驱动的，不能被这些因子解释的部分被称为股票的“特质收益率”，而每支股票的特质收益率之间是互不相关的。Rosenberg 之后成立了 Barra，并于 1975 年提出 Barra USE1 模型。随后在 1985 年、1997 年和 2011 年相继发布 USE2、USE3、USE4 等版本的 Barra 模型，对市场收益及风险的归因模型进行不断优化。

假设市场上有 K 个驱动股票收益的共同因子，那么Barra 模型的主要形式可以表示为：
$$
r_i=\sum_{k=1}^KX_{ik}f_k+u_i
$$
其中，$r_i$为股票的收益率，$f_k$为因子的收益率，$X_{ik}$表示股票i在因子k上的暴露程度，一般取前一期的因子暴露度，$u_i$表示股票的特质收益率。
假设有一个由 N 只股票组成的资产组合，股票$i$在该组合中的权重为$w_i$，那么该投资组合的收益率$R_p$可表示为：
$$
R_p=\sum_{i=1}^N w_ir_i
$$
整个投资组合在风险因子𝑘上的暴露程度可以表示为：  
$$
X_k^p=\sum_{i=1}^N w_iX_{ik}
$$
投资组合的收益可以进一步表示为单个因子收益的加权形式，权重即为$X_k^p$。
$$
R_p=\sum_{k=1}^K X_k^pf_k+\sum_{i=1}^Nw_iu_i
$$
由上式可以看到，利用多因子模型可以将对 N 只股票的收益-风险分析转换为对 K 个因子的收益-风险分析。在实际运用过程中，股票数量 N 要远远大于共同因子数量 K，因此借助多因子模型进行分析可以起到降维的效果，在降低分析工作量的同时提高了预测准确度。由于单个因子的收益与特质收益率互不相关，且不同股票的特质收益率之间也互不相关，因此投资组合的风险可以表示为：  
$$
var(R_p)=\sum_{k,l}X_k^pF_{kl}X_k^p+\sum_{i=1}^N w_i^2var(u_i)
$$
由于不同因子在数量级上存在差别，因此在实际回归中需要对单个因子在横截面上进行标准化，从而得到均值为0、标准差为 1 的标准化因子。为保证全市场基准指数对每个风格因子的暴露程度均为 0，我们需要对每个因子减去其市值加权均值，再除以其标准差，计算方法如下：  
$$
X_{ik}=\frac{X_{ik}^{Raw}-\mu_k}{\sigma_k}\\
\mu_k=\sum_{i=1}^N w_iX_{ik}^{Raw}\\
$$
考虑一个由市值加权构成的投资组合，可以通过如下验证看出，该投资组合对于任意因子的暴露度均为 0。  
$$
X_k^p=\sum_{i=1}^Nw_iX_{ik}=\sum_{i=1}^Nw_i\frac{X_{ik}^{Raw}-\mu_k}{\sigma_k}\\
=\frac{1}{\sigma_k}(\sum_{i=1}^Nw_iX_{ik}^{Raw}-\mu_k\sum_{i=1}^Nw_i)\\
=\frac{1}{\sigma_k}(\sum_{i=1}^Nw_iX_{ik}^{Raw}-\mu_k)=0
$$
在 Barra 模型中我们假设每只股票的特质收益率互不相关，但是每只股票的特质收益率序列的方差并不相同，这就导致了回归模型出现异方差性。为解决这一问题，可以采用加权最小二乘WLS 方法进行回归，对不同的股票赋予不同的权重。  
$$
r=Xf+u\\
f=(X^TWX)^{-1}X^TWr
$$
在计量经济学方法中，WLS 回归模型的权重 W 通常选定为特质收益率方差的倒数$1/var(r)$，然而在模型解出之前股票的特质收益率是未知的，无法直接使用。观察到股票特质收益率方差通常与股票的市值规模成反比，即大市值股票的特质收益率方差通常较小，因此在实际回归中我们将以市值的平方根占比作为每只股票的回归权重。  

## Barra风格因子

Barra风险因子模型中主要有十类因子，本课题使用wind API接口提取易方达消费行业基金2018年-2020年成分股的因子数据。每一类中的因子在进行因子归一化之后进行简单加权平均。

<center> <font size=2><b> 表13： Barra风格因子指标说明</b> </font></center>

| 风格     | 指标               | 指标说明                                                     |
| -------- | ------------------ | ------------------------------------------------------------ |
| 价值     | 市盈率 PE          | PE＝市值/归属母公司股东净利润                                |
| 价值     | 市净率 PB          | PB＝市值/归属母公司股东权益                                  |
| 价值     | 市销率 PS          | PS＝市值/营业收入                                            |
| 价值     | 市现率 PCF         | PCF＝市值/经营现金流量净额                                   |
| 价值     | PEG 指标           | 市盈率/eps 增长速度                                          |
| 价值     | EV2/EBITDA         | 企业价值倍数=公司价值/税息折旧及摊销     前利润              |
| 价值     | 每股派息 DP        | DP=分红/总市值                                               |
| 成长     | 营业收入增长率     | 营业收入（同比增长率）     营业收入（N 年，增长率）          |
| 成长     | 经营性现金流增长率 | 经营活动产生的现金流量净额（同比增长     率）                |
| 成长     | 净利润增长率       | 净利润-扣除非经常损益（近  N 年增长率）     净利润-扣除非经常损益（复合年增长率） |
| 成长     | EPS 增长率         | 基本每股收益（同比增长率）     基本每股收益（近 N 年增长率） |
| 成长     | 净资产收益率增长率 | 净资产收益率（同比增长率）     净资产收益率（近 N 年增长率） |
| 盈利     | 销售毛利率         | （营业收入-营业成本）/营业收入*100%                          |
| 盈利     | 销售净利率         | （归属母公司股东的净利润+少数股东损     益）/营业收入*100%   |
| 盈利     | 净资产收益 ROE     | 净利润/（期初归属母公司股东损益+期末     归属母公司股东权益）/2*100% |
| 盈利     | 总资产报酬率 ROA   | （股东应战溢礼+少数股东损益）/（期初     总资产+期末总资产）/2 |
| 规模     | 市值               | 流通市值 = 指定证券指定交易日收盘价*     截至日该证券的发行上市股数     总市值 = 个股当日股价*当日总股本 |
| 动量反转 | 过去 n 月的收益率  | 过去 N 月的收益率/过去 N 月收益率减去     最近一月收益率     |
| 波动率   | 收益率的标准差     | 取最近 N 日收益率标准差                                      |
| 流动性   | 换手率             | 取最近 N 日换手率平均                                        |
| Beta     | Beta 因子          | CAPM 回归                                                    |
| 杠杆     | 资产负债率         | 资产负债率 = 负债总额／资产总额     长期资产负债率 = 非流动负债合计／（非     流动负债合计+归属母公司股东的权益） |
| 杠杆     | 现金比率           | (货币资金+交易性金融资产+应收票据)／     流动负债合计        |
| 杠杆     | 速动比率           | (流动资产－存货净额)／流动负债                               |
| 杠杆     | 流动比率           | 流动资产／流动负债                                           |

## Barra风格分解结果

以下为2019-2020年两年的Barra因子收益率的热力图，其中食品饮料、家用电器、汽车、轻工制造、电子、农林牧渔、商业贸易、医药生物、计算机这几个行业因子收益率显著不为0，规模因子、beta因子、动量因子、盈利性因子、波动率因子、流动性因子和杠杆因子这几个行业因子收益率显著不为0。

**回归的$R^2$平均值在80%左右，该模型能较好的解释易方达消费行业基金的收益**。

![](result/barra_factor_ret_heatmap2018.png)

<center> <font size=2><b> 图62： 2018年Barra风格因子收益率热力图</b> </font></center>

![](result/barra_factor_ret_heatmap2019.png)

<center> <font size=2><b> 图63： 2019年Barra风格因子收益率热力图</b> </font></center>



![](result/barra_factor_ret_heatmap2020.png)

<center> <font size=2><b> 图64： 2020年Barra风格因子收益率热力图</b> </font></center>

![](result/barra_r2.png)

<center> <font size=2><b> 图65： 横截面广义最小二乘回归R2</b> </font></center>

<div STYLE="page-break-after: always;"></div>

<div STYLE="page-break-after: always;"></div>

# 参考文献

1. [Jensen, M.C., “The Performance of Mutual Funds in the Period 1945-1964,” Journal of Finance 23, 1968, pp. 389-416.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=244153). 

2. Sharpe, W. F. Mutual Fund Performance. Journal of Business. 1966, **39** (S1): 119–138. [doi:10.1086/294846](https://dx.doi.org/10.1086%2F294846).

3. Bayley, D. and M. López de Prado (2012): "The Sharpe Ratio Efficient Frontier", Journal of Risk, 15(2), pp.3-44. Available at http://ssrn.com/abstract=1821643

4. [Measurement H . A Universal Performance Measure.](https://faculty.fuqua.duke.edu/~charvey/Teaching/BA453_2006/Keating_A_universal_performance.pdf) 

5. [Goetzmann, William N. et al. “Portfolio Performance Manipulation and Manipulation-Proof Performance Measures.” *Review of Financial Studies* 20 (2007): 1503-1546.](https://www.semanticscholar.org/paper/Portfolio-Performance-Manipulation-and-Performance-Goetzmann-Ingersoll/51bb77035cac7e07e5119b0fd769af08b99dacce)

6. Brinson, G.P., Hood, L.R. and Beebower, G.L. (1986) Determinants of Portfolio Performance. Financial Analysts Journal, 42, 39-44. https://doi.org/10.2469/faj.v42.n4.39

7. [Measuring non-US. equity portfolio performance[J]. Journal of Portfolio Management, 1985, 11(3):73-76.](https://jpm.pm-research.com/content/11/3/73)

8. [MBA智库百科：基金绩效评价](https://wiki.mbalib.com/wiki/%E5%9F%BA%E9%87%91%E7%BB%A9%E6%95%88%E8%AF%84%E4%BB%B7)

9. [Jcy Ji Cherie的学习室：教你一种可以年化30%的低风险投资策略之基金筛选系统](https://mp.weixin.qq.com/s/_90lTDyMfzeIRwV-Mv6DvQ)

10. [量化投资 -- 技术篇(6)投资组合策略性能评价（上)](https://blog.csdn.net/weixin_43171270/article/details/102947507?spm=1001.2014.3001.5501)

11. [量化投资技术--技术篇(7) 投资组合收益性能评价(下)](https://blog.csdn.net/weixin_43171270/article/details/102948347?spm=1001.2014.3001.5501)

12. [【原创】私募云通带你了解15种基金业绩风险指标（上）](https://mp.weixin.qq.com/s/3h19Ia8BwtRC0mhVkoeNdA)

13. [【原创】私募云通带你了解15种基金业绩风险指标（下）](https://mp.weixin.qq.com/s/PEbqGoN8UDBg2EyqGOaPxw)

14. [【云通原创】基金业绩归因之基于T-M模型的选时选股能力研究](https://mp.weixin.qq.com/s/0tYzMy6ud-uv_5y0_5eI4w)

15. [【云通原创】基金业绩归因之基于C-L模型的选时选股能力研究](https://mp.weixin.qq.com/s/2ve0MUuIcFSl_3AU7GlYTA)

16. [【云通原创】基金业绩归因之基于H-M模型的选时选股能力研究](https://mp.weixin.qq.com/s/sYEJAm8nYbT61KrgPC05Lg)

17. [【重磅原创】基金业绩归因系列第三篇：单期Brinson绩效分解模型](https://mp.weixin.qq.com/s/mT9dtT_XeSjq5Ghi-8WfXg)

18. [【重磅原创】基金业绩归因系列第十篇：多期Brinson模型算法（下）](https://mp.weixin.qq.com/s/MAbS1ZnL0xGJI5EAyEGlkQ)

    

<div STYLE="page-break-after: always;"></div>
# 附录

## 附录1：代码使用指南


```python
# 导入相关程序包
import numpy as np
import pandas as pd
from data_get import *
from index_cal import *
from index_plot import *
# 如果未下载外加数据，可以通过加载wind API下载
# from WindPy import *
# w.start()
```


```python
# 设定参数
index = '110022.OF'
begin_date = '2010-08-20'
end_date = '2021-06-08'
```


```python
# 导入计算所需的相关dataframe
df, df_with_rf,df_with_ben, df_with_rf_market,df_with_rf_ben, df_with_rf_market_ben, rf, market, benchmark_df = data_load(index,begin_date,end_date)
```


```python
# 实例化指标计算类
index = Index()
```


```python
# 计算整个投资期内的最大回撤
print('MaxDrawdown',index.MaxDrawdown(df,colname='net_value',period='all'))
```

    MaxDrawdown -0.25860662424539077

```python
# 滚动计算从期初至当前日期的夏普比率
rolling(df_with_rf_market_ben, index.case_to_function('Sharp'), method='begin_end')
```


    array([        nan, -3.980801  , -3.64611105, ..., -1.77854157,
           -1.77999005, -1.81278671])


```python
# 滚动计算从每年年初至当前日期的信息比率
rolling(df_with_rf_market_ben, index.case_to_function('Information'), method='year')
```


    array([        nan, -2.70818785,  6.97847912, ...,  0.17190935,
           -0.40077014,  0.22465114])


```python
# 滚动计算投资期为3个月时的累积收益
rolling(df_with_rf_market_ben, index.case_to_function('Cumret'), method='rolling')
```


    array([       nan,        nan,        nan, ..., 0.06539295, 0.06145793,
           0.11023622])


```python
# 画出指标随时间变化的趋势图
plot_line(rolling(df, index.Cumret, method='begin_end'),df.date[1:].apply(lambda x: str(x)),'Cumret')
```

<img src="./result/output_9_0.png" alt="png" style="zoom:20%;" />



```python
# 画出期初投资至今的胜率的箱线图
plot_box(rolling(df, index.Winfreq, method='begin_end'),'Sharpe Ratio')
```

<img src="./result/output_10_0.png" alt="png" style="zoom:20%;" />



```python
# 画出收益率分布图
plot_dist(rolling(df, index.Dayret, method='begin_end'),'Dailyret')
```

<img src="./result/output_11_0.png" alt="png" style="zoom:20%;" />



```python
# 画出收益率与夏普比率两两相关分布图
plot_relat_ret(rolling(df_with_rf_market, index.Sharp, method='begin_end'),rolling(df_with_rf_market, index.Dayret, method='begin_end'),'Sharpe')
```

<img src="./result/output_12_0.png" alt="png" style="zoom: 60%;" />

<div STYLE="page-break-after: always;"></div>

## 附录2：同类型基金指标计算结果（排名前十）

|               | 嘉实新兴产业 | 建信改革红利 | 工银瑞信前沿医疗A | 安信价值精选 | 鹏华环保产业 |
| ------------- | ------------ | ------------ | ----------------- | ------------ | ------------ |
| Cumret        | 4.794        | 4.279        | 4.093             | 4.072        | 3.554        |
| Compoundedret | 0.307216     | 0.272304     | 0.366349          | 0.262411     | 0.238491     |
| mean          | 2.4148       | 2.244385     | 1.913456          | 2.572097     | 1.8325       |
| Annulstd      | 0.250572     | 0.275719     | 0.227618          | 0.230649     | 0.266602     |
| Downsiderisk  | 0            | 0            | 0                 | 0            | 0            |
| MaxDrawdown   | -0.25138     | -0.46326     | -0.23805          | -0.29643     | -0.25264     |
| MaxLoss       | 0            | 0            | -0.021            | -0.002       | -0.003       |
| Winfreq       | 0.531592     | 0.524798     | 0.522536          | 0.540309     | 0.530073     |
| AR1T          | 0.561843     | 0.685367     | 0.040988          | 0.713038     | 0.28626      |
| his_VaR       | 0.040904     | 0.04591      | 0.035978          | 0.039249     | 0.045243     |
| his_CVaR      | 0.000717     | 0.000571     | 0.00091           | 0.000568     | 0.000456     |

|               | 工银瑞信医疗保健行业 | 鹏华养老产业 | 交银医药创新 | 景顺长城成长之星 |
| ------------- | -------------------- | ------------ | ------------ | ---------------- |
| Cumret        | 3.466                | 3.254        | 3.2243       | 3.204            |
| Compoundedret | 0.263316             | 0.255532     | 0.418251     | 0.217308         |
| mean          | 1.799789             | 1.904557     | 1.830955     | 1.908014         |
| Annulstd      | 0.287714             | 0.293629     | 0.242173     | 0.28651          |
| Downsiderisk  | 0                    | 0            | 0            | 0                |
| MaxDrawdown   | -0.56954             | -0.56538     | -0.26473     | -0.54014         |
| MaxLoss       | 0                    | -0.031       | -0.0247      | -0.056           |
| Winfreq       | 0.525202             | 0.510958     | 0.542029     | 0.535188         |
| AR1T          | 0.310054             | 0.506378     | 0.086792     | 0.545977         |
| his_VaR       | 0.045603             | 0.046663     | 0.035978     | 0.046332         |
| his_CVaR      | 0.00054              | 0.000552     | 0.001068     | 0.000402         |

<div STYLE="page-break-after: always;"></div>

## 附录3：Brinson行业分解结果

单期分解结果
![](result/单期Brinson/20111231_brinson.png)

![](result/单期Brinson/20120630_brinson.png)

![](result/单期Brinson/20121231_brinson.png)

![](result/单期Brinson/20130630_brinson.png)

![](result/单期Brinson/20131231_brinson.png)

![](result/单期Brinson/20140630_brinson.png)

![](result/单期Brinson/20141231_brinson.png)

![](result/单期Brinson/20150630_brinson.png)

![](result/单期Brinson/20151231_brinson.png)

![](result/单期Brinson/20160630_brinson.png)

![](result/单期Brinson/20161231_brinson.png)

![](result/单期Brinson/20170630_brinson.png)

![](result/单期Brinson/20171231_brinson.png)

![](result/单期Brinson/20180630_brinson.png)

多期分解结果
![](result/多期Brinson/20111231_brinson.png)



![](result/多期Brinson/20120630_brinson.png)

![](result/多期Brinson/20121231_brinson.png)

![](result/多期Brinson/20130630_brinson.png)

![](result/多期Brinson/20131231_brinson.png)

![](result/多期Brinson/20140630_brinson.png)

![](result/多期Brinson/20141231_brinson.png)

![](result/多期Brinson/20150630_brinson.png)

![](result/多期Brinson/20151231_brinson.png)

![](result/多期Brinson/20160630_brinson.png)

![](result/多期Brinson/20161231_brinson.png)

![](result/多期Brinson/20170630_brinson.png)

![](result/多期Brinson/20171231_brinson.png)

![](result/多期Brinson/20180630_brinson.png)


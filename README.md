# 2023年（第11届）“泰迪杯”数据挖掘挑战赛
## 一、赛题背景
近年来企业外部环境越来越不确定，复杂多变的外部环境，让企业供应链面临较多难题。需求预测作为企业供应链的第一道防线，重要程度不言而喻，然而需求预测受多种因素的影响，导致预测准确率普遍较低，因此需要更加优秀的算法来解决这个问题。需求预测是基于历史数据和未来的预判得出的有理论依据的结论，有利于公司管理层对未来的销售及运营计划、目标，资金预算做决策参考；其次，需求预测有助于采购计划和安排生产计划的制定，减少受业务波动的影响。如果没有需求预测或者预测不准，公司内部很多关于销售、采购、财务预算等决策都只能根据经验而来了，会导致对市场预测不足，产生库存和资金的积压或不足等问题，增加企业库存成本。
## 二、赛题任务
### 需要解决的问题
1. 请对附件中的训练数据（order_train1.csv）进行深入地分析，可参照但不限于下述主题。<br>
（1） 产品的不同价格对需求量的影响；<br>
（2） 产品所在区域对需求量的影响，以及不同区域的产品需求量有何特性；<br>
（3） 不同销售方式（线上和线下）的产品需求量的特性；<br>
（4） 不同品类之间的产品需求量有何不同点和共同点；<br>
（5） 不同时间段（例如月头、月中、月末等）产品需求量有何特性；<br>
（6） 节假日对产品需求量的影响；<br>
（7） 促销（如618、双十一等）对产品需求量的影响；<br>
（8） 季节因素对产品需求量的影响。 <br>
2. 基于上述分析，建立数学模型，对附件预测数据（predict_sku1.csv）中给出的产品，预测未来3月（即2019年1月、2月、3月）的月需求量，将预测结果按照表3的格式保存为文件result1.xlsx，与论文一起提交。请分别按天、周、月的时间粒度进行预测，试分析不同的预测粒度对预测精度会产生什么样的影响。

![month_avg_ord.png](image/qeustion5/month_avg_ord.png)
![month_total_ord.png](image/qeustion5/month_total_ord.png)
![month_total_ord.png](image/question3/cate_sales.png)
![month_total_ord.png](image/question3/month_way.png)
![month_total_ord.png](image/question3/offline.png)
![month_total_ord.png](image/question6/产品大类_节假日.png)
![month_total_ord.png](image/question6/产品细类_节假日.png)
![month_total_ord.png](image/question6/销售区域_节假日.png)

### Author

By 云淡风轻 肇庆学院 202124114132<br>
blog:http://blog.winkovo.top<br>
QQ:1026771081<br>

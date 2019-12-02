# -*- coding: utf-8 -*-
import time
import os
import pandas as pd
import numpy as np

os.chdir("C:\Workspace\PythonWS\QyjsCompare\Table") # 更改工作目录
# print(os.getcwd()) # 打印当前工作目录
start = time.time()
#————————————————————————————————————————————————————————————————————————————————————————————-
print("开始读取输入表格")
#读取输入表格
flow = pd.read_csv("flow.csv",encoding = 'UTF-8')
route = pd.read_csv("route.csv",encoding = 'UTF-8')
distance = pd.read_csv("85中心局之间的距离.csv",encoding = 'UTF-8')
end = time.time()
print("输入表格读取完毕，总用时：",(end-start))
#————————————————————————————————————————————————————————————————————————————————————————————-
#函数
def statistics(flow,route,distance):
    statistics = pd.DataFrame()
    route['总距离'] = 0 #初始化距离列
    for i in range(0,route.shape[0]):
        temp_route = route.loc[i,'路线'].split('-') #拆路线
        print(i)
        for m in range(0,(len(temp_route) - 1)):
            route.loc[i,'总距离'] += float(distance.loc[(distance['收寄城市'] == temp_route[m]) & (distance['寄达城市'] == temp_route[m+1])]['距离'])  #单个提取距离并累加

    total_data = pd.merge(route, flow, how='left', on=['收寄城市', '寄达城市'])  #连接总流量
    total_flow = total_data['总流量'].sum()
    total_data['加权距离'] = total_data.apply(lambda x: x['总距离'] * x['总流量'] / total_flow,axis = 1 )
    total_data['加权经转次数'] =  total_data.apply(lambda x:x['经转次数']*x['总流量']/total_flow,axis = 1 )

    per_yunj =  total_data['加权距离'].sum()
    statistics = statistics.append([['平均运距',per_yunj]])
    per_jingz = total_data['加权经转次数'].sum()
    statistics = statistics.append([['平均经转次数', per_jingz]])

    statistics = pd.DataFrame(np.array(statistics),columns = ['统计项','结果'])


    return statistics,total_data

#————————————————————————————————————————————————————————————————————————————————————————————-
print("计算输出")
statis,total_data = statistics(flow,route,distance)
statis.to_csv("统计结果.csv",index = 0, encoding = 'utf_8_sig')
total_data.to_csv("统计总表.csv",index = 0, encoding = 'utf_8_sig')
end = time.time()
print("计算输出完毕，总用时：",(end-start))
#————————————————————————————————————————————————————————————————————————————————————————————-









depreciation = {'12t': 0.93, '20t': 1.17,'40t': 1.77}   #每公里折旧费x1（元）
toll = {'12t': 1.51, '20t': 1.63, '40t': 2.26}   #每公里路桥费x2（元）
fuel_cost_full = {'12t': 1.59, '20t': 1.91, '40t': 2.54}   #每公里油耗费x3（元）
fuel_cost_empty = {'12t': 1.28, '20t': 1.60, '40t': 2.23}   #每公里空车油耗费x4（元）
other_cost = {'12t': 0.2, '20t': 0.23, '40t': 0.3}   #每公里其他费用x5（元）
driver_cost = {'12t': 84.84, '20t': 84.84, '40t': 84.84}   #每小时司机人工费x6（元）
loading_weight = {'12t': 4500, '20t': 6000, '40t': 8000}   #每辆车可装载邮件重量（公斤）
coeff_assign = {'12t': 1.5, '20t': 1.5, '40t': 1.5}   #单程委办邮路成本系数（倍）
#coeff_assign = {'12t': 1, '20t': 1, '40t': 1}   #单程委办邮路成本系数（倍）
zb_weight = 8.355 #集包件平均重量，单位kg
big_weight = 2.8288 #大件平均重量，单位kg
r1 = 0.8 #中心局之间直达往返之一运量够80%，r1≥r2
r2 = 0.4 #中心局之间直达往返之一运量够40%，r1≥r2



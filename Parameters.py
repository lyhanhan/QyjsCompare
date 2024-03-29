#注：以12t，20t，40t的顺序，与函数里的顺序相反
GL_DEP = [0.93,1.17,1.77]         # 车辆价格/每公里折旧（x1）
GL_LQ = [1.51,1.63,2.26]          # 路桥费用/公里（x2）
GL_OIL = [1.59,1.91,2.54]         # 油耗/每公里价格（x3）
GL_EMP_OIL = [1.28,1.6,2.23]      # 空车油耗/每公里价格（x4）
GL_OTHER = [0.2,0.23,0.3]         # 其他费用/公里（x5)
GL_LABOR = [84.84,84.84,84.84]    # 司机费用/小时(x6)
GL_CAP_1 = [3629,4839,6452]         # 容量/件(x7)
GL_K = [1.5,1.5,1.5]              # 单程委办邮路成本系数（倍）
#GL_K = [1,1,1]              # 单程委办邮路成本系数（倍）
GL_CAP = [4500,6000,8000]        # 每辆车载重量（公斤）
GL_V = [60.0,60.0,60.0]                 # 车速/小时
GL_DSP = 400                      #里程约束，大于该里程司机需2名
GL_PERW = [2.8288,8.355]              #单个大件和集包件的重量
GL_HANDLEC = [0.34,0.5]    #单个大件和集包件的处理成本
GL_MAX = 50     #最大车量数
GL_PERCENT = 0.8     #够量自开比例

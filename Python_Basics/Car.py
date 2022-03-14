# 导入的python自带库
import math
import datetime


# 封装运行的函数
# Car_Name为车的名称，Mob_Time为进场时间，APP_time为出场时间
def Time_tick(Car_Name, Mob_Time, APP_time):
    if Car_Name == '面包车':
        StartTime = Mob_Time
        # 利用datetime时间函数
        Start = datetime.datetime.strptime(StartTime, "%Y-%m-%d %H:%M:%S")
        EndTime = APP_time
        End = datetime.datetime.strptime(EndTime, "%Y-%m-%d %H:%M:%S")
        # 取两者时间差
        delta = End - Start
        delta_minute = delta.seconds / 60  # 分钟的差
        # 判断是否停到次日及以后
        if delta.days == 0:
            # 不超过30分钟的
            if delta_minute <= 30:
                money = 0
                print("你的车辆已停了", delta.days, "天", "%.0f" % delta_minute, "分钟!", "需要支付", money, "元")
            # 超过30分钟的
            elif delta_minute > 30:
                delta_hour = delta_minute / 60
                # 不超过12小时正常收费
                if delta_hour <= 12:
                    money = math.ceil(delta_hour) * 5
                    print("你的车辆已停了", delta.days, "天", "%.0f" % delta_minute, "分钟!", "需要支付", money, "元")
                # 封顶收费为12小时的费用
                elif delta_hour > 12:
                    money = 60
                    print("你的车辆已停了", delta.days, "天", "%.0f" % delta_minute, "分钟!", "需要支付", money, "元")
        # 停车到次日或者以后
        elif delta.days > 0:
            # 最好的结果为无分钟计算
            if delta.seconds == 0:
                money = delta.days * 60
                print("你的车辆已停了", delta.days, "天", "%.0f" % delta_minute, "分钟!", "需要支付", money, "元")
            # 如果有分钟计算
            elif delta.seconds != 0:
                delta_hour = delta.seconds / 3600
                # 向上取整，次日之后都算超过半小时了
                if math.ceil(delta_hour) <= 12:
                    money = delta.days * 60 + math.ceil(delta_hour) * 5
                    print("你的车辆已停了", delta.days, "天", "%.0f" % delta_minute, "分钟!", "需要支付", money, "元")
                # 小时费达到12小时的封顶，可以直接加24小时的费用
                elif math.ceil(delta_hour) > 12:
                    money = delta.days * 60 + 60
                    print("你的车辆已停了", delta.days, "天", "%.0f" % delta_minute, "分钟!", "需要支付", money, "元")
    else:
        print("输入的车型有误！")

Time_tick("面包车", '2021-01-18 00:00:00', '2021-01-19 10:59:00')

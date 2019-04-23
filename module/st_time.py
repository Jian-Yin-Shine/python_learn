# time 时间，日期
# calendar，日历
import time

# 时间戳
ticks = time.time()
print(ticks)

# 转换为时间元组
# localtime()
localtime = time.localtime(time.time())
print(localtime)

tm_year, tm_mon, tm_mday, *_ = localtime
print(tm_year, tm_mon, tm_mday)

# 获取格式化的时间
# 常用 asctime

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
# Tue Apr 23 13:58:42 2019

# 格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
# 2019-04-23 14:00:18

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# Tue Apr 23 14:02:23 2019

# 将格式化字符串转为时间戳
str = "Tue Apr 23 14:02:23 2019"
print(time.mktime( time.strptime(str, "%a %b %d %H:%M:%S %Y")))

'''
python 格式化日期符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

import calendar

# 获取某一年某一月的日历

cal = calendar.month(2019, 4)
print(cal)
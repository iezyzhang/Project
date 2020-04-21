
# import------引入外部功能
# 引入整个模块import datetime
# print(datetime.datetime.now())

# 如果import后面直接加上模块的名称，  调用某一个类的时候，必须携带模块名，比如，datetime.datetime.now()
# 引入模块部分类    from   模块名   import  类名，调用的时候  无序加上模块，比如：datetime.now()
from datetime import datetime, timedelta
from datetime import *  # 引入datetime中 所有的类
print(datetime.now())


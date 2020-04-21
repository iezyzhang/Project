import os
import re
# 案例演示：在mbile.txt中 追加手机号

new_path = "C:\\Users\\iezyzhang\\Desktop\\office\\mobile.txt"
new_mobile = "15083333479"
try:
    with open(new_path,mode="a",encoding="utf-8") as fd:
        fd.write("追加写入：" + new_mobile)
except:
    print("写入文件异常")
else:
    print("写入成功")
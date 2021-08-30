import os  # 系统目录操作相关
import shutil # 日常文件和目录管理
import glob  # 通过通配符在当前目录下进行搜索
import sys  # 系统相关
import re  # 正则表达式
import math  # 数学运算
import zlib  # 用于数据压缩
from timeit import Timer  # 细粒度时间主要用于性能


# print(os.getcwd())
# os.system("mkdir today")
# os.chdir('today')
# print(os.getcwd())

# shutil.copyfile('./test_try.py', './try.py')  # copyfile(src, destination)
# shutil.move('./try.py', './today/')  # 移动文件

print(glob.glob("test_*.py"))  # 通过通配符在当前目录下进行搜索
print(sys.argv)

# import matplotlib
# from matplotlib import font_manager
# import matplotlib.pyplot as plt
# # define figure
# fig = plt.figure()
#
# # define data
# # x = [1, 2, 3, 4, 5, 6, 7]
# # y = [1, 3, 4, 2, 5, 8, 6]
# x= [1]
# y=[5]
# left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
#
# ax1 = fig.add_axes([left, bottom, width, height])
# # type1 = ax1.plot(x, y, 'bo', label='$blue$')
# plt.scatter(x, y, s=200, label = '$car$', c = 'blue', marker='.', alpha = None, edgecolors= 'white')
# # 用scatter绘制散点图,可调用marker修改点型, label图例用$$包起来，edgecolors边缘颜色，只有前两个是必备参数
#
# # 显示图例
# plt.legend()
# plt.show()



# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_title('test')

# Method 1
# left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
# ax2 = fig.add_axes([left, bottom, width, height])
# ax2.plot(x, y, 'r')
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# plt.xlim((4,7))
# ax2.set_title('part1')


# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 创建测试数据
# x = np.random.randn(20)
# y = np.random.randn(20)
# # x=1
# # y=5
# # 绘制点
# plt.scatter(x, y, s=200, label = 'like', c = 'blue', marker='.', alpha = None, edgecolors= 'white')
# # 用scatter绘制散点图,可调用marker修改点型, label图例用$$包起来，edgecolors边缘颜色，只有前两个是必备参数
#
# # 显示图例
# plt.legend()
# plt.show()
# !/usr/bin/env python
# -*-  coding:utf-8  -*-
# version: Python 3.6.3 on win32
# author:  Suranyi    time:  2018/1/16

import numpy as np
import matplotlib.pyplot as plt

# 创建测试数据
x = np.random.randn(20)
y = np.random.randn(20)

# 绘制点
plt.scatter(x, y, s=200, label = '$like$', c = 'blue', marker='.', alpha = None, edgecolors= 'white')
# 用scatter绘制散点图,可调用marker修改点型, label图例用$$包起来，edgecolors边缘颜色，只有前两个是必备参数

# 显示图例
plt.legend()
plt.show()

x = np.random.randn(10)
y = np.random.randn(10)
plt.scatter(x, y, s=200, label = '$dislike$', c = 'red', marker='.', alpha = None, edgecolors= 'white')
plt.legend()  # 每次都要执行


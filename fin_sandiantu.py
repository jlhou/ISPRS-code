import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])









# 创建测试数据
x = 58.92
y = 79.16
# 绘制点
ax1.scatter(x, y, s=400, label = '$MobileNet$', c = 'black', marker='.', alpha = None, edgecolors= 'white')
# 用scatter绘制散点图,可调用marker修改点型, label图例用$$包起来，edgecolors边缘颜色，只有前两个是必备参数

# 显示图例
ax1.legend()

x = 100.57
y = 81.39
ax1.scatter(x, y, s=400, label = '$Xp-single-scale$', c = 'red', marker='.', alpha = None, edgecolors= 'white')
ax1.legend()  # 每次都要执行

font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 1,
}
x = 101.02
y = 82.69
ax1.scatter(x, y, s=400, label = '$Xp-mutil-scale$', c = 'green', marker='.', alpha = None, edgecolors= 'white')
ax1.legend(prop=font1)  # 每次都要执行
# legend.get_title().set_fontsize(fontsize = 10)



x = 107.35
y = 83.35
ax1.scatter(x, y, s=400, label = '$Xp-decoder$', c = 'blue', marker='.', alpha = None, edgecolors= 'white')
ax1.legend()  # 每次都要执行

x = 1286.56
y = 85.18
ax1.scatter(x, y, s=400, label = '$Xp-output8$', c = 'orange', marker='.', alpha = None, edgecolors= 'white')
ax1.legend()  # 每次都要执行
# plt.ylim(78,100)
plt.xlabel('times(ms)')
plt.ylabel('mean-F1-score(%)')
plt.xlim(0,2500)




# Method 1
# left, bottom, width, height = 0.15, 0.45, 0.4, 0.4
left, bottom, width, height = 0.2, 0.6, 0.29, 0.29
plt.axes([bottom, left, width, height])
x = 58.92
y = 79.16
# 绘制点
plt.scatter(x, y, s=200, label = '$MobileNet$', c = 'black', marker='.', alpha = None, edgecolors= 'white')
# 用scatter绘制散点图,可调用marker修改点型, label图例用$$包起来，edgecolors边缘颜色，只有前两个是必备参数

# 显示图例
# ax1.legend()

x = 100.57
y = 81.39
plt.scatter(x, y, s=200, label = '$Xp-single-scale$', c = 'red', marker='.', alpha = None, edgecolors= 'white')
# ax1.legend()  # 每次都要执行


x = 101.02
y = 82.69
plt.scatter(x, y, s=200, label = '$Xp-mutil-scale$', c = 'green', marker='.', alpha = None, edgecolors= 'white')
# plt.legend()  # 每次都要执行

x = 107.35
y = 83.35
plt.scatter(x, y, s=200, label = '$Xp-decoder$', c = 'blue', marker='.', alpha = None, edgecolors= 'white')
# ax1.legend()  # 每次都要执行


# plt.xlim(55,110)
# plt.ylim(79,84)
plt.xlabel('times(ms)')
plt.ylabel('mean-F1-score(%)')
plt.title('part')

plt.show()












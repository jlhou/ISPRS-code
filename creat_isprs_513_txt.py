import os
import random
from PIL import  Image
for root, dirs, files in os.walk('E:\\bishe\SAR\div_train_images'):
    file_lenth = len(files)
    for k in range(file_lenth):
        file_name = files[k]
        cut_file_name = file_name[0:45]
        print(cut_file_name)
        f = open('E:\\bishe\SAR\\txt\\trainval.txt','a')
        f.write(cut_file_name+'\n')
        f = open('E:\\bishe\SAR\\txt\\train.txt', 'a')
        f.write(cut_file_name + '\n')
for root, dirs, files in os.walk('E:\\bishe\SAR\div_val_images'):
    file_lenth = len(files)
    for k in range(file_lenth):
        file_name = files[k]
        cut_file_name = file_name[0:45]
        print(cut_file_name)
        f = open('E:\\bishe\SAR\\txt\\trainval.txt','a')
        f.write(cut_file_name+'\n')
        f = open('E:\\bishe\SAR\\txt\\val.txt', 'a')
        f.write(cut_file_name + '\n')
# # for root, dirs, files in os.walk('E:\\bishe\SAR\div_lucky_train_images_down'):
#     file_lenth = len(files)
#     for k in range(file_lenth):
#         file_name = files[k]
#         cut_file_name = file_name[0:52]
#         f = open('E:\\bishe\SAR\\rota_left_down_text\\trainval.txt','a')
#         f.write(cut_file_name+'\n')
#         f = open('E:\\bishe\SAR\\rota_left_down_text\\train.txt', 'a')
#         f.write(cut_file_name + '\n')
# for root, dirs, files in os.walk('E:\\bishe\SAR\div_lucky_train_images_rota'):
#     file_lenth = len(files)
#     for k in range(file_lenth):
#         file_name = files[k]
#         cut_file_name = file_name[0:52]
#         f = open('E:\\bishe\SAR\\rota_left_down_text\\trainval.txt','a')
#         f.write(cut_file_name+'\n')
#         f = open('E:\\bishe\SAR\\rota_left_down_text\\train.txt', 'a')
#         f.write(cut_file_name + '\n')
#
#
#
#
#
#
#
#
# for root, dirs, files in os.walk('E:\\bishe\SAR\div_lucky_val_images'):
#     file_lenth = len(files)
#     for k in range(file_lenth):
#         file_name = files[k]
#         cut_file_name = file_name[0:45]
#         f = open('E:\\bishe\SAR\\rota_left_down_text\\trainval.txt', 'a')
#         f.write(cut_file_name + '\n')
#         f = open('E:\\bishe\SAR\\rota_left_down_text\\val.txt', 'a')
#         f.write(cut_file_name + '\n')
#     #             print('..................................')
# # import os
# # import random
#
# rootdir = "d:\\face\\train"
# file_names = []
# for parent, dirnames, filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
#     file_names = filenames
#     # for filename in filenames:                        #输出文件信息
#     #     print("parent is" + parent)
#     #     print("filename is:" + filename)
#     #     print("the full name of the file is:" + os.path.join(parent, filename))
# x = random.randint(0, len(file_names)-1)
# # print(file_names[x])
# import random
# if random.random()>0.1:
#     print(random.random())
# else:
#     print('none')
from PIL import  Image
import os
import math
from PIL import  Image
print('resize_images')
for root, dirs, files in os.walk('/home/ubuntu/MyFiles/auto_upload_20190707124204/shuangchuan/untitled/tensorflow_gaofen_dataset/Images/full_val'):
    file_lenth = len(files)
    for k in range(file_lenth):
        file_name = files[k]
        # print(file)
        # print('........................................................')
        # from PIL import  Image
        im = Image.open('/home/ubuntu/MyFiles/auto_upload_20190707124204/shuangchuan/untitled/tensorflow_gaofen_dataset/Images/full_val/%s'%file_name)
        im_size = im.size
        w_stride = 256
        h_stride = 256
        w_rate = math.ceil(im_size[0]/(w_stride))
        h_rate = math.ceil(im_size[1]/(h_stride))
        im = im.resize((w_rate*(w_stride), h_rate*(h_stride)))      #此处m为resize后的m
        # w_stride = 256
        # h_stride = 256
        # for i in range(w_rate-1):
        #     for j in range(h_rate-1):
        for j in range(h_rate - 1):
            for i in range(w_rate - 1):
                print(i, j)
                x = w_stride*i
                y = h_stride*j
                region = im.crop((x, y, x+w_stride*2, y+h_stride*2))   #
                # region = region.resize((513, 513))
                cut_file_name = file_name[0:37]
                cut_file_name_ = '%s %s'%(cut_file_name, '_')
                cut_file_name_ = '%s %3d'%(cut_file_name_, w_stride)
                cut_file_name_ = '%s %s' % (cut_file_name_, '_')
                cut_file_name_ = '%s %3d' % (cut_file_name_, h_stride)
                cut_file_name_ = '%s %s' % (cut_file_name_, '_')
                cut_file_name = '%s %s'%(cut_file_name_, '%03d_%03d'%(i, j))
                finish_name = '%s %s' %(cut_file_name, '_image')

                region.save('/home/ubuntu/MyFiles/auto_upload_20190707124204/shuangchuan/untitled/tensorflow_gaofen_dataset/Images/val/%s.jpg'%finish_name)
                # region.save('E:\\bishe\SAR\div_lucky_full_images\\%s.jpg' % finish_name)
print('resized_labels_about_images')
for root, dirs, files in os.walk('/home/ubuntu/MyFiles/auto_upload_20190707124204/shuangchuan/untitled/tensorflow_gaofen_dataset/Labels/full_val'):
    file_lenth = len(files)
    for k in range(file_lenth):
        file_name = files[k]
        # print(file)
        # print('........................................................')
        # from PIL import  Image
        la = Image.open('/home/ubuntu/MyFiles/auto_upload_20190707124204/shuangchuan/untitled/tensorflow_gaofen_dataset/Labels/full_val/%s'%file_name)
        la_size = la.size
        w_stride = 256
        h_stride = 256
        w_rate = math.ceil(la_size[0]/(w_stride))
        h_rate = math.ceil(la_size[1]/(h_stride))
        la = la.resize((w_rate*(w_stride), h_rate*(w_stride)))      #此处m为resize后的m
        # for i in range(w_rate-1):
        #     for j in range(h_rate-1):
        for j in range(h_rate - 1):
            for i in range(w_rate - 1):
                print(i, j)
                x = w_stride*i
                y = h_stride*j
                region = la.crop((x, y, x+w_stride*2, y+h_stride*2))   #
                # region = region.resize((513, 513))
                cut_file_name = file_name[0:37]
                cut_file_name_ = '%s %s'%(cut_file_name, '_')
                cut_file_name_ = '%s %3d' % (cut_file_name_, w_stride)
                cut_file_name_ = '%s %s' % (cut_file_name_, '_')
                cut_file_name_ = '%s %3d' % (cut_file_name_, h_stride)
                cut_file_name_ = '%s %s' % (cut_file_name_, '_')
                cut_file_name = '%s %s'%(cut_file_name_, '%03d_%03d'%(i, j))
                finish_name = '%s %s' % (cut_file_name, '_label')
                region.save('/home/ubuntu/MyFiles/auto_upload_20190707124204/shuangchuan/untitled/tensorflow_gaofen_dataset/Labels/val/%s.png'%finish_name)
                # region.save('E:\\bishe\SAR\div_lucky_val_labels\\%s.png'%finish_name)


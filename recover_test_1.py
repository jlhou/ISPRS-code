from PIL import  Image
import os
import math
from PIL import  Image
print('recover_images')
w_stride = 0
h_stride = 0

for root, dirs, files in os.walk('E:\\bishe\SAR\\test'):
    file_lenth = len(files)
    for k in range(file_lenth):
        file_name = files[k]
        i = file_name[39:41]
        i = int(i)
        # print('show i')
        # print(i)
        if i>w_stride:
            w_stride = i
        j = file_name[43:45]
        j = int(j)
        if j > w_stride:
            h_stride = j

        # print('show j')
        # print(j)
print('w_stride:%s'%w_stride)
print('h_stride:%s'%h_stride)
toImage = Image.new('RGBA', (300*(w_stride+1), 300*(h_stride+1)))

for i in range(w_stride+1):
    for j in range(h_stride+1):
        for root, dirs, files in os.walk('E:\\bishe\SAR\\test'):
            file_lenth = len(files)
            for k in range(file_lenth):
                file_name = files[k]
                output_name = file_name[0:23]
                image_i = file_name[39:41]
                image_i = int(image_i)
                image_j = file_name[43:45]
                image_j = int(image_j)
                if i == image_i and j == image_j:
                    from_image = Image.open('E:\\bishe\SAR\\test\\%s'%file_name)
        loc = ((i*300), (j*300))
        toImage.paste(from_image, loc)
toImage = toImage.resize((1887, 2557))   #变换尺寸

toImage.save('E:\\bishe\SAR\\recover\\%s.png'%output_name)






        # print(file)
        # print('........................................................')
        # # from PIL import  Image
        # im = Image.open('E:\\bishe\SAR\lucky_val_images\\%s'%file_name)
        # im_size = im.size
        # w_stride = 300
        # h_stride = 300
        # w_rate = math.ceil(im_size[0]/(w_stride))
        # h_rate = math.ceil(im_size[1]/(h_stride))
        # im = im.resize((w_rate*(w_stride), h_rate*(h_stride)))      #此处m为resize后的m
        # # w_stride = 256
        # # h_stride = 256
        # for i in range(w_rate):
        #     for j in range(h_rate):
        #         print(i, j)
        #         x = w_stride*i
        #         y = h_stride*j
        #         region = im.crop((x, y, x+w_stride, y+h_stride))   #
        #         # region = region.resize((513, 513))
        #         cut_file_name = file_name[0:23]
        #         cut_file_name_ = '%s %s'%(cut_file_name, '_')
        #         cut_file_name_ = '%s %3d'%(cut_file_name_, w_stride)
        #         cut_file_name_ = '%s %s' % (cut_file_name_, '_')
        #         cut_file_name_ = '%s %3d' % (cut_file_name_, h_stride)
        #         cut_file_name_ = '%s %s' % (cut_file_name_, '_')
        #         finish_name = '%s %s'%(cut_file_name_, '%03d_%03d'%(i, j))
        #         region.save('E:\\bishe\SAR\div_lucky_val_images_300\\%s.jpg'%finish_name)
        #         region.save('E:\\bishe\SAR\div_lucky_full_images_300\\%s.jpg' % finish_name)
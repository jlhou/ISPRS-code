# -*- coding: gbk -*-
import cv2
import numpy as np
import os
import random 
import h5py
def eachFile(filepath):				 #将目录内的文件名放入列表中  
	pathDir =  os.listdir(filepath)   
	out = []	
	for allDir in pathDir:		
		child = allDir		
		out.append(child)	
	return out
def split_data(pic_dir_data,pic_dir_out,Width,Height,train_percentage=0.7):   #从文件夹中获取图像数据     
	train_data = os.path.join(pic_dir_out,'train')  
	test_data = os.path.join(pic_dir_out,'test')	    
	if not os.path.isdir(train_data):
		os.mkdir(train_data) 
		os.mkdir(test_data)                     
	pic_dir_set = eachFile(pic_dir_data) 
	X_test = []    
	y_test = []    
	label = 0             
	for pic_dir in pic_dir_set:        
		print(pic_dir_data+"\\"+pic_dir) 
		pic_train_data= os.path.join(train_data,pic_dir) 
		pic_test_data= os.path.join(test_data,pic_dir)     
		if not os.path.isdir(pic_train_data):            
			os.mkdir(pic_train_data) 
			os.mkdir(pic_test_data)            
		pic_set = eachFile(os.path.join(pic_dir_data,pic_dir)) 
		random.shuffle(pic_set)            
		train_count = int(len(pic_set)*train_percentage)      
		for pic_index,pic_name in enumerate(pic_set):            
			if not os.path.isfile(os.path.join(pic_dir_data,pic_dir,pic_name)):                
				continue            
			img = cv2.imread(os.path.join(pic_dir_data,pic_dir,pic_name))            
			if img is None:                
				continue 
			img = cv2.resize(img,(Width,Height))                                     
			if (pic_index < train_count):                
				cv2.imwrite(os.path.join(pic_train_data,pic_name), img)                      
			else:               
				cv2.imwrite(os.path.join(pic_test_data,pic_name), img)
				img = img.reshape(-1,Width,Height,3)	
				X_test.append(img)                
				y_test.append(label)                    
		if len(pic_set) > 0:                    
			label += 1 
	
	file_name= '.\data_101\Caltech101_test_data.h5'  	  
	f = h5py.File(file_name,'w') 
	X_test=np.array(X_test)    
	X_test = np.concatenate(X_test,axis=0)         
	y_test = np.array(y_test)                 
	f.create_dataset('X_test', data = X_test)        
	f.create_dataset('y_test', data = y_test)        
	f.close() 
	print("Dataset has been splited ")       
if __name__ == '__main__':
	split_data('.\Caltech101','.\data_101',224,224)


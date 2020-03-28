# Copyright 2018 The TensorFlow Authors All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Tests for DeepLab model and some helper functions."""
import os
import random
from PIL import  Image
for root, dirs, files in os.walk('E:\\bishe\SAR\ISPRS_semantic_labeling_Vaihingen\images'):
    file_lenth = len(files)
    for k in range(file_lenth):
        file_name = files[k]
        f = open('E:\\bishe\SAR\ISPRS_semantic_labeling_Vaihingen\isprs_text\\full_image_trainval.txt','a')
        f.write(file_name+'\n')
        if random.random()<0.7:
            f = open('E:\\bishe\SAR\ISPRS_semantic_labeling_Vaihingen\isprs_text\\full_image_train.txt','a')
            f.write(file_name+'\n')
            # print(random.random())
        else:
            f = open('E:\\bishe\SAR\ISPRS_semantic_labeling_Vaihingen\isprs_text\\full_image_val.txt','a')
            f.write(file_name+'\n')

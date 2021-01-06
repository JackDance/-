#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import random
import shutil

def moveFile(src, dst,rate):
    pathDir = [jpg for jpg in os.listdir(src) if jpg.endswith('.jpg')] # 获取fileDir文件夹下所有jpg格式的图片的路径
    filenumber = len(pathDir) # fileDir下图片的数量
    sample = random.sample(pathDir, int(filenumber*rate)) # sample的文件路径
    for name in sample:
        # 移动文件到另一个文件
        # shutil.move(pathDir+name, dst+name)
        # 复制文件到另一个文件
        shutil.copyfile(os.path.join(src,name), os.path.join(dst,name))
    return

if __name__ == '__main__':
    src = r'G:\weiyi\About_YOLO\data_processing\xml_coco_yolo\1217_1221\yuantu'
    dst = r'G:\weiyi\About_YOLO\data_processing\xml_coco_yolo\1217_1221\sample'
    moveFile(src,dst,0.2)

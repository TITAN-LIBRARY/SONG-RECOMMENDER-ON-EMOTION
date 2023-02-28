#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:56:48 2020

@author: waiseekweng
"""

import numpy as np
import cv2
import os

os.makedirs("output")

with open("/Users/waiseekweng/Documents/test_facial_expression/dataset/fer2013.csv") as f:
    content = f.readlines()

lines = np.array(content)

num_of_instances = lines.size

for i in range(1,num_of_instances):
    try:
        emotion, img = lines[i].split(",")
        img = img.replace('"', '')
        img = img.replace('\n', '')
        pixels = img.split(" ")

        pixels = np.array(pixels, 'float32')
        image = pixels.reshape(48, 48)

        path_file_name = f"output/{i}_{emotion}.jpg"
        cv2.imwrite(path_file_name, image)

    except Exception as ex:
        print(ex)
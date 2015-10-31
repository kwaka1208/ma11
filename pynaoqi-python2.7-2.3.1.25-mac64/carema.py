#!/usr/bin/env python
# -*- coding: utf-8 -*-

from naoqi import ALProxy

# プロキシのインスタンス生成
photo = ALProxy("ALPhotoCapture", "192.168.10.74", 9559)

# フォーマットの指定(“bmp”, “dib”, “jpeg”, “jpg”, “jpe”, “png”, “pbm”, “pgm”, “ppm”, “sr”, “ras”, “tiff”, “tif”が指定可能)
photo.setPictureFormat("jpeg")

# 解像度の指定(0 = kQQVGA, 1 = kQVGA, 2 = kVGA)
photo.setResolution(4)

# 保存先を指定して画像をキャプチャ
photo.takePicture("/home/nao/recordings/cameras/", "image1")


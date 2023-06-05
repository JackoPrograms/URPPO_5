import cv2
import numpy as np
import matplotlib.pyplot as plt


def build(numDisparities, blockSize):
    img_l = cv2.imread("DSC02692.JPG", 2)
    img_r = cv2.imread("DSC02694.JPG", 2)

build(16, 5)

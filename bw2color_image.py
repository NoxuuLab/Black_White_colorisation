# import libraries and packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
                help="path to input black and white image")
ap.add_argument("-p", "--prototxt", type=str, required=True,
                help="path to Caffe prototxt file")
ap.add_argument("-m", "--model", type=str, required=True,
                help="path to Caffe pre-trained model")
ap.add_argument("-c", "--points", type=str, required=True,
                help="path to cluster center points")
args = vars(ap.parse_args())

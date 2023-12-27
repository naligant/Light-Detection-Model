from ultralytics import YOLO
import os
import glob
import pandas as pd
from IPython.display import Image, display

#where dataset is being derived
from roboflow import Roboflow
rf = Roboflow(api_key="b5bK2k4Wd80qFhpbgaGy")
project = rf.workspace("iaagl").project("traffic-lights-rqds4")
dataset = project.version(3).download("yolov8")
from ultralytics import YOLO
import os
import glob
import pandas as pd
from IPython.display import Image, display

#where dataset is being derived
from roboflow import Roboflow

#downloading dataset
rf = Roboflow(api_key="iOqPD5zonb3Ou6XZ2Xpe")
project = rf.workspace("wawan-pradana").project("cinta_v2")
dataset = project.version(1).download("yolov5")
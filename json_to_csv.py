#-- import base packages
import json
import os
import sys

#-- import Pypi packages
import cv2
import pandas as pd

#-- import custom packages

if __name__ == '__main__':
    dir = sys.argv[1]
    target = ".json"
    print('-----')
    print(dir)
    class_dirs = [i for i in os.listdir(dir) if os.path.isdir(os.path.join(dir, i))]
    print(class_dirs)
    for classif in class_dirs:
        json_files = [i for i in os.listdir(os.path.join(dir, classif)) if i.lower().endswith(target)]
        columns = ['filename', 'width', 'height',
                    'class', 'xmin', 'ymin', 'xmax', 'ymax'
        ]
        csv = pd.DataFrame(columns = columns)

        for f in json_files:
            p = os.path.join(dir, classif, f)
            with open(p) as f:
                js = json.load(f)
            im = cv2.imread(os.path.join(dir, classif, js['image']))
            h, w,c = im.shape
            row = {
                'path': os.path.join(dir, classif),
                'filename': os.path.join(classif, js['image']),
                'width': w,
                'height': h,
                'class': classif,
                'xmin': js['xmin'],
                'ymin': js['ymin'],
                'xmax': js['xmax'],
                'ymax': js['ymax'],
            }
            csv = csv.append(row, ignore_index=True)
    csv.to_csv('fish_finder.csv', index=False)

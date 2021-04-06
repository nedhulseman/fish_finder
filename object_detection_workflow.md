# Sources
https://pythonprogramming.net/training-custom-objects-tensorflow-object-detection-api-tutorial/
https://github.com/datitran/raccoon_dataset


# Object Detection Steps
1. Scrape Images
2. Label Images
3. Install TensforFlow + object_detection API
4. Create TFRecords
5. Create Config Files in TensorFlow API


## 1. Scrape Images
For this I used Instagram # tags 
Run getImages.py with specified # tag
$ python getImages.py

## 2. Label Images

#### Label images with preffered application
This can be done with any number of applications. I created my own to draw bounding boxes onto the images which drops json files with bounding box locations. The only caveat is that you can only draw a single box.

$ bbox_drawer.py

It will be assumed that each class that needs to be labeled will be in its own directory within data. e.g.

#-- Data
|  #--- Class #1
|  #--- Class #2
|  #--- Class.... #n

#### Combine JSON files into csv format
$ python json_to_csv.py data



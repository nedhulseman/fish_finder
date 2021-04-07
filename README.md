# Sources
https://pythonprogramming.net/training-custom-objects-tensorflow-object-detection-api-tutorial/
https://github.com/datitran/raccoon_dataset

# Architecture
- Azure Ubuntu Compute Instance DS12 and trained with....
- tensorflow 1.15.5


# Object Detection Steps
1. Scrape Images
2. Label Images
3. Install TensforFlow + object_detection API
4. Create TFRecords
5. Create Config Files in TensorFlow API
6. Using a trained model


## 1. Scrape Images
For this I used Instagram # tags 
Run getImages.py with specified # tag
$ python getImages.py

## 2. Label Images

#### Label images with preffered application
This can be done with any number of applications. I created my own to draw bounding boxes onto the images which drops json files with bounding box locations. The only caveat is that you can only draw a single box.

$ bbox_drawer.py

It will be assumed that each class that needs to be labeled will be in its own directory within data. e.g.

#-- Data. 
|  #--- Class #1<br>
|  #--- Class #2<br>
|  #--- Class.... #n<br> 

#### Combine JSON files into csv format
$ python json_to_csv.py data

We will also need to split our data into train and test datasets
$ python split_data.py

## 3. Install Tensorflow & object detection API
$ pip install "tensorflow>=1.15,<2.0"
$ pip install --upgrade tensorflow-hub
$ git clone https://github.com/tensorflow/models.git
$ cd models/reseach # be in folder where object_detection folder is
$ protoc object_detection/protos/*.proto --python_out=.
$ export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim # will have to run this with every fresh terminal

May also need to install...
$ Pip install tf_slim
$ Pip install gin-config

## 4. Create TFRecords
Copy tf_records script from : https://github.com/datitran/raccoon_dataset/blob/master/generate_tfrecord.py
and alter the script as needed for data path and labels....

$ python generate_tfrecord.py --csv_input=train.csv  --output_path=train.record --image_dir=data
$ python generate_tfrecord.py --csv_input=test.csv   --output_path=test.record  --image_dir=data

## 5. Creating configuration files for object_detection api and training the model


## 6. Using the trained model



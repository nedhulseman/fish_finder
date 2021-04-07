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
```
$ python getImages.py
```
## 2. Label Images

#### Label images with preffered application
This can be done with any number of applications. I created my own to draw bounding boxes onto the images which drops json files with bounding box locations. The only caveat is that you can only draw a single box.
```
$ bbox_drawer.py
```
It will be assumed that each class that needs to be labeled will be in its own directory within data. e.g.

#-- Data<br>
|  #--- Class #1<br>
|  #--- Class #2<br>
|  #--- Class.... #n<br> 

#### Combine JSON files into csv format
$ python json_to_csv.py data

We will also need to split our data into train and test datasets<br>
```
$ python split_data.py
```

## 3. Install Tensorflow & object detection API
```
$ pip install "tensorflow>=1.15,<2.0"<br>
$ pip install --upgrade tensorflow-hub<br>
$ git clone https://github.com/tensorflow/models.git<br>
$ cd models/reseach # be in folder where object_detection folder is<br>
$ sudo apt-get install protobuf-compiler <br>
$ protoc object_detection/protos/*.proto --python_out=.<br>
$ export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim # will have to run this with every fresh terminal<br>
```

May also need to install...
```
$ Pip install tf_slim<br>
$ Pip install gin-config<br>
```

## 4. Create TFRecords
Copy tf_records script from : https://github.com/datitran/raccoon_dataset/blob/master/generate_tfrecord.py<br>
and alter the script as needed for data path and labels....<br>
```
$ python generate_tfrecord.py --csv_input=train.csv  --output_path=train.record --image_dir=data<br>
$ python generate_tfrecord.py --csv_input=test.csv   --output_path=test.record  --image_dir=data
```

## 5. Creating configuration files for object_detection api and training the model
```
$ mkdir training
$ wget https://raw.githubusercontent.com/tensorflow/models/master/object_detection/samples/configs/ssd_mobilenet_v1_pets.config
$ wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_11_06_2017.tar.gz
```

##### Edit config file for following line items
1. PATHS_TO_BE_CONFIG
2. Alter num_classes to match the number of classes
3. Optional: alter batch_size parameter
4. Optional: alter max steps parameter

##### Create pbtxt file
```
$ nano training/object-detection.pbtxt
item {
  id: 1
  name: 'macncheese'
}
$ cp training/object-detection.pbtxt data
```

##### Copy relevant data & configuration files into object_detection API
1. Data #-- with train.records, test.records & images (I dont think you actually need the images)
2. Training #-- object-detection.pbtxt
3. ssd_mobilenet_v1_pets.config
4. ssd_mobilenet_v1_pets model file
5. Images #-- which has test images we can run afterwards

##### Run train.py
```
$ python3 legacy/train.py --logtostderr --train_dir=training/<br>
                          --pipeline_config_path=training/ssd_mobilenet_v1_pets.config
```

## 6. Using the trained model



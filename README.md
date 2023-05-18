# Directive-research

git clone https://github.com/pjreddie/darknet
cd darknet
make

wget https://pjreddie.com/media/files/yolov3.weights

./darknet detect cfg/yolov3.cfg yolov3.weights <img path or video file>

download KITTI traing Dataset for 2D objects

For testing and generating labels to store in a csv file for the KITTI dataset, run test.py
the example csv file can be found in the repository

To test the accuracy
1. download the training labels from the KITTI Dataset as Ground Truth
2. Run main.py and obtain the accuracy in percentage

import darknet
import csv

def convertBack(x, y, w, h): 
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax

# Clear CSV file
with open('test_labels.csv', 'w') as csvfile:
    pass

# Load YOLO
net = darknet.load_net(b"cfg/yolov3.cfg", b"yolov3.weights", 0)
meta = darknet.load_meta(b"cfg/coco.data")

# Image path
img_path = "training/image_2/"
for i in range(500):  # replace 10 with actual number of images
    img = (img_path + f'{i:06}.png').encode('utf-8')

    # Detect objects
    r = darknet.detect(net, meta, img)

    # Open CSV file to write the labels
    with open('test_labels.csv', 'a', newline='') as csvfile:
        fieldnames = ['index','label', 'confidence', 'x', 'y', 'w', 'h', 'xmin', 'ymin', 'xmax', 'ymax']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only once, i.e., when the loop index i is 0
        if i == 0:
            writer.writeheader()

        for detection in r:
            label = detection[0].decode()
            confidence = detection[1]
            bounds = detection[2]
            x, y, w, h = bounds
            xmin, ymin, xmax, ymax = convertBack(float(x), float(y), float(w), float(h))
            writer.writerow({'index':f'{i:06}','label': label, 'confidence': confidence, 'x': x, 'y': y, 'w': w, 'h': h, 'xmin': xmin, 'ymin': ymin, 'xmax': xmax, 'ymax': ymax})

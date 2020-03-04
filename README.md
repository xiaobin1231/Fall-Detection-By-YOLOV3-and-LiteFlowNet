# Demo

### Our method can tell the difference between falling down and crouhing.

![image](https://github.com/xiaobin1231/Fall-Detection-By-YOLOV3-and-LiteFlowNet/blob/master/fall%20down.gif)
![image](https://github.com/xiaobin1231/Fall-Detection-By-YOLOV3-and-LiteFlowNet/blob/master/normal.gif)

# Requirements

pytorch >= 1.2.0

cuda10.0

cudnn7.6.5



## Pretrained weights

[1.LiteFlowNet](https://drive.google.com/open?id=10stKXIifdceZXqBZ89rfBYyUySK3PcxH)


[2.YOLOV3](https://drive.google.com/open?id=10stKXIifdceZXqBZ89rfBYyUySK3PcxH)




# Run
```
cd/Your Code PATH
python detect.py --source "Your image or video PATH" --weights "YOLOv3 Weights PATH" --LiteFlowNet_weights "Your FlowNet weights" --view-img "True or False"
```
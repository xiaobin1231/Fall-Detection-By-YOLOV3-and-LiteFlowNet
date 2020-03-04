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


[2.YOLOV3](https://drive.google.com/open?id=1qjWD97VYgzjB9qbI6mln0STvH7S_OSns)




# Run
```
Cd/Your Code PATH
python detect.py --source "Your image or video PATH" --weights "YOLOv3 Weights PATH" --LiteFlowNet_weights "Your FlowNet weights" --view-img "True or False"
```


# Citation

[1] @misc{pytorch-liteflownet,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;author = {Simon Niklaus},  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;title = {A Reimplementation of {LiteFlowNet} using {Pytorch}},  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;year = {2019},  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;howpublished = {\url{https://github.com/xiaobin1231/Fall-Detection-By-YOLOV3-and-LiteFlowNet}}  

[2] @misc{yolov3,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;author = {ultralytics},  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;title = {YOLOv3 in PyTorch>ONNX>CoreML>iOS},  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;year = {2019},  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;howpublished = {\url{https://github.com/xiaobin1231/Fall-Detection-By-YOLOV3-and-LiteFlowNet}}  

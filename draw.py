'''
import imageio
import os

def create_gif(image_list, gif_name, duration=0.35):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


def main():
    pth = '/home/iiau/fall_down_detection/YOLOv3_LiteFlowNet/output'
    image_list = [os.path.join(pth, i) for i in  sorted(os.listdir(pth))]
    gif_name = '/home/iiau/fall_down_detection/YOLOv3_LiteFlowNet/normal.gif'
    duration = 0.1
    create_gif(image_list, gif_name, duration)


if __name__ == '__main__':
    main()
'''

import os
import cv2
import numpy as np

path = '/home/iiau/fall_down_detection/URFD_images/Falls/fall_fall-01/'
filelist = sorted(os.listdir(path))

fps = 24 #视频每秒24帧
size = (224, 224) #需要转为视频的图片的尺寸
#可以使用cv2.resize()进行修改

video = cv2.VideoWriter("falldown.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
#视频保存在当前目录下

for item in filelist:
    if item.endswith('.jpg'):
    #找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path + item
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()
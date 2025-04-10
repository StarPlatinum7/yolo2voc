# YOLO，VOC数据集格式转换

> yolo转换为voc，使用之前删除dataset中的所有readme.md

## YOLO数据集格式

- images:存放图片数据
- labels:存放标注txt文本
- 一个标注信息txt对应一张图片，如xxx.txt对应xxx.jpg所有的标注信息

**YOLO标注格式：txt格式**

```
<object-class> <x> <y> <width> <height>
```

## VOC数据集格式

VOC数据集由五个部分构成：JPEGImages，Annotations，ImageSets，SegmentationClass以及SegmentationObject.**

- JPEGImages：存放的是训练与测试的所有图片。
- Annotations：里面存放的是每张图片打完标签所对应的XML文件。
- ImageSets：ImageSets文件夹下本次讨论的只有Main文件夹，此文件夹中存放的主要又有四个文本文件test.txt,train.txt,trainval.txt,val.txt, 其中分别存放的是测试集图片的文件名、训练集图片的文件名、训练验证集图片的文件名、验证集图片的文件名。
- SegmentationClass与SegmentationObject：存放的都是图片，且都是图像分割结果图，对目标检测任务来说没有用。class segmentation 标注出每一个像素的类别
- object segmentation 标注出每一个像素属于哪一个物体。

**XML标注格式**

```
<annotation>
  <folder>17</folder> # 图片所处文件夹
  <filename>77258.bmp</filename> # 图片名
  <path>~/frcnn-image/61/ADAS/image/frcnn-image/17/77258.bmp</path>
  <source>  #图片来源相关信息
    <database>Unknown</database>  
  </source>
  <size> #图片尺寸
    <width>640</width>
    <height>480</height>
    <depth>3</depth>
  </size>
  <segmented>0</segmented>  #是否有分割label
  <object> 包含的物体
    <name>car</name>  #物体类别
    <pose>Unspecified</pose>  #物体的姿态
    <truncated>0</truncated>  #物体是否被部分遮挡（>15%）
    <difficult>0</difficult>  #是否为难以辨识的物体， 主要指要结体背景才能判断出类别的物体。虽有标注， 但一般忽略这类物体
    <bndbox>  #物体的bound box
      <xmin>2</xmin>     #左
      <ymin>156</ymin>   #上
      <xmax>111</xmax>   #右
      <ymax>259</ymax>   #下
    </bndbox>
  </object>
</annotation>
```

## 脚本使用

1. 检查脚本中的文件路径
2. 将所有数据及图片复制到`./dataset/JPEGImages`，将所有标注文件复制到`./dataset/YOLO`

2. ```python
   #得到annotations
   python .\yolo2voc.py 
   ```

3. ```
   \ImageSets\main
   pip install natsort
   python .\get_index.py
   ```

> 参考：
>
> https://github.com/KKKSQJ/DeepLearning/tree/master/others/label_convert
>
> https://blog.csdn.net/BGMcat/article/details/120889683

# DSC-YOLOv4

Safety helmet wearing detection has practical significance in actual production operations. The current target detection method based on YOLOv4 can achieve effective detection of workers wearing helmets. However, it limits the further use in complex scenarios such as dense scenes. To solve this problem, we propose an improved YOLOv4 mode which replaces the CSPdarknet backbone network with a depthwise separable convolutional network that is composed of the depthwise convolution and the pointwise convolution. 

The network structure is shown as

![image](https://user-images.githubusercontent.com/28681601/127974670-68aa6375-1190-47a6-932a-f6937ce31aec.png)

It can be seen that if construction workers cover each other, YOLOv4 appears few people wearing helmet cannot be detected, while DSC-YOLOv4 can still have a better detection performance.


![image](https://user-images.githubusercontent.com/28681601/127973847-80d41e4a-7926-460c-807f-da5682bf3e5e.png)

DSC-YOLOv4 is more adaptable to environment changes.


![image](https://user-images.githubusercontent.com/28681601/127973935-9a1482b6-d4b6-4acd-be92-235204d075bf.png)

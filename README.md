# DSC-YOLOv4

Safety helmet wearing detection has practical significance in actual production operations. The current target detection method based on YOLOv4 can achieve effective detection of workers wearing helmets. However, it limits the further use in complex scenarios such as dense scenes. To solve this problem, we propose an improved YOLOv4 mode which replaces the CSPdarknet backbone network with a depthwise separable convolutional network that is composed of the depthwise convolution and the pointwise convolution.
if construction workers cover each other, YOLOv4 appears few people wearing helmet cannot be detected, while DSC-YOLOv4 can still have a better detection performance.DSC-YOLOv4 is more adaptable to environment changes.


Train. py is used to train.
Predict.by is used to predict. 
Get_map.py is used to obtain AP and mAP.

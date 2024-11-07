This folder holds the major work performed during our project for CMPE258 - Deep Learning course under Professor KaiKai Liu. 

Team Members:
Ankita Jaswal
Jiajun Dai
Akhilandeswari Battineni

The structure of our software process is as follows:

---------------------- Datasets used for training and testing:---------------------------

"train_data_processed" contains data from three sources:
1.) FER2013
2.) MH-FED
3.) Emotic

"test" set contains data from FER2013 only. 

---------------------------------- Train/Test Code --------------------------------------
*** Note ***: 
For training A100 GPU/V100 GPU were used in google colab notebook environment. 
For testing, only CPU was used.
Any and all references used for training the models are linked within each section of their respective colab notebooks. 

The three trained model approaches are in their respective directories. 
For instance, HSemotion contains EfficientNet model approach for train/test. 
MobileNet contains its approach for train/test. 
VGG16 contains its approach for train/test.

-------------------------------- Individual Contributions -------------------------------

Ankita Jaswal - Data collection, preprocessing, EfficientNet training/evaluation, MobileNetV2 CBAM training/evaluation, real-time testing using haarcascade and best performing model.

Jiajun Dia - VGG16 Training and Testing. 

Akhilandeswari Battineni - MobileNetV2 Training and Testing.

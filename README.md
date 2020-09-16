# Body Tracking with Witcher 3 (Openpose)

This is an attempt at playing the game Witcher 3 using pose detection. This is achieved by using OpenCV for capturing frames from webcam, Openpose model for pose estimation and helper libraries such as 'keyboard' and 'pydirectinput' for controlling the game.

The pytorch implementation of pretrained OpenPose model used in this project was taken from 'Hzzone's repository (https://github.com/Hzzone/pytorch-openpose). The repository has implementations for hand pose as well as body pose estimation. In this case only the body pose estimation model was used.

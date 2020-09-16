# Body Tracking with Witcher 3 (Openpose)

This is an attempt at playing the game Witcher 3 using pose detection. This is achieved by using OpenCV for capturing frames from webcam, Openpose model for pose estimation and helper libraries such as 'keyboard' and 'pydirectinput' for controlling the game.

The pytorch implementation of pretrained OpenPose model used in this project was taken from 'Hzzone's' repository (https://github.com/Hzzone/pytorch-openpose). The repository has implementations for hand pose as well as body pose estimation. In this case only the body pose estimation model was used.

As Witcher 3 uses Window's DirectInput, it is not possible to simulate mouse movements using the regular 'pyautogui' library. For this reason the library 'pydirectinput' (https://github.com/learncodebygaming/pydirectinput) was used in this project. This library was built specifically for DirectInput use-cases.

As far as controls are concerened, a different pose is assigned for attack, parrying, casting signs, walking and witcher sense.

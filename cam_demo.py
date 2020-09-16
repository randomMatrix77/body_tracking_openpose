import cv2
import time
import pydirectinput as pd
import keyboard
import numpy as np
from body_tracking import util
from body_tracking.body_model import Body

head = [0, 16, 17]
torso = [2, 1, 5]
hands = [[3, 4], [6, 7]]
keys = ['w', # Move
        'q', # Cast sign
        '0', # witcher sense
        'p', # parry
        '='  # Attack
        ]
body_estimation = Body('D:/Softwares/miniconda/torch_models/checkpoints/body_pose_model.pth')

def cast_sign():

    keyboard.press(keys[1])
    time.sleep(0.1)
    keyboard.release(keys[1])

def mouse_move(curr_loc, prev_loc):

    pd.move(int((curr_loc[0] - prev_loc[0])*0.1),
               int((curr_loc[1] - prev_loc[1])*0.01))

def move_forward(press_flag):
    if press_flag:
        keyboard.press(keys[0])
    else:
        keyboard.release(keys[0])

def witcher_sense(press_flag):
    if press_flag:
        keyboard.press(keys[2])
    else:
        keyboard.release(keys[2])

def parry(press_flag):
    if press_flag:
        keyboard.press(keys[3])
    else:
        keyboard.release(keys[3])

def attack():
    keyboard.press(keys[4])
    time.sleep(0.01)
    keyboard.release(keys[4])

cap = cv2.VideoCapture(0)
cv2.imshow('demo', np.zeros((256, 256)))

print('Starting in...')
for i in reversed(range(15)):

    print(i, end=' ')
    time.sleep(1)
print('\n')

for k in keys:
    keyboard.release(k)

prev_center = pd.position()

while True:

    ret, frame = cap.read()
    frame = frame[60:410, :, :]

    frame = cv2.resize(frame, (256, 256))

    try:
        candidate, subset = body_estimation(frame)

        center = candidate[1][:2]

        left_hand = candidate[4][:2]
        left_elbow = candidate[3][:2]

        right_hand = candidate[7][:2]
        right_elbow = candidate[6][:2]

        head = candidate[0][:2]

        mouse_move(center, prev_center)

        if right_elbow[1] - 10 < right_hand[1] < right_elbow[1] + 10:
            move_forward(1)
            print('Go forward!!!')
        else:
            move_forward(0)

        if left_elbow[1] - 10 < left_hand[1] < left_elbow[1] + 10:
            witcher_sense(1)
            print('Button Pressed')
        else:
            witcher_sense(0)

        if left_hand[1] < left_elbow[1] and right_hand[1] < right_elbow[1]:
            parry(1)
            print('DeeeFenceeee!!!!')
        else:
            parry(0)

        if left_hand[1] < center[1] or right_hand[1] < center[1]:
            cast_sign()
            print('IGNIIIIIIIII')

        if left_hand[0] > center[0] or right_hand[0] < center[0]:
            attack()
            print('Attack!!!!')


        canvas = util.draw_bodypose(frame, candidate, subset)

        cv2.imshow('demo', canvas)

        prev_center = center

    except:
        pass


    k = cv2.waitKey(1)
    if k % 256 == 27:
        cap.release()
        cv2.destroyAllWindows()
        break

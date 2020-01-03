import cv2
import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Parse args for TravelMouse')
parser.add_argument('-f', '--file', help='The path to the video file', required=True, dest='file')
parser.add_argument('-i', '--interval', help='The time interval between two frame captures', dest='interval', type=float, required=False, default=5)
args = parser.parse_args()

filepath = os.path.abspath(args.file)
if not os.path.isfile(filepath):
    print(filepath + " is not a file!")
    sys.exit(1)

output_path = os.path.dirname(filepath)
name = os.path.basename(filepath)
name = name.split('.')[0]
print('Base name: ' + name)


vidcap = cv2.VideoCapture(filepath)
fps = vidcap.get(cv2.CAP_PROP_FPS)
time = 0

image = None
while True:
    frame = int(time * fps)
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame)
    success, image = vidcap.read()
    if not success:
        print('Unable to read from video!')
        break

    cv2.imwrite(os.path.join(output_path, name + '_frame_' + str(frame) + '.jpg'), image)
    time += args.interval

vidcap.release()

if args.delete:
    os.remove(filepath)

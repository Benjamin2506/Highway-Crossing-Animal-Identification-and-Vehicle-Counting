'''----------------------Author---------------------
Kunal Nicose
Benjamin2506
2022, India
'''

import os
import subprocess


for fileName in os.listdir("Input/"):
	lastDotIndex = fileName.rfind(".")

	cmd = "python yolo_video.py --input inputVideos/" + fileName + " --output outputVideos/" + \
		fileName[:lastDotIndex] + ".avi --yolo yolo-coco --use-gpu 1"
	print("Running command:\n" + cmd)
	subprocess.run(cmd, shell=True)

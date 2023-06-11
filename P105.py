import cv2
import os

path = "Images"

image = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
        image.append(file_name)

print(len(image))
count = len(image)

Frame = cv2.imread(image[0])
height, width, chanells = Frame.shape
print(height, width, chanells)
size = (width, height)
print(size)

out = cv2.VideoWriter("P105.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
#P105 video
for i in range(0, count):
	Frame = cv2.imread(image[i])
	out.write(Frame)

out.release()
print("done!")

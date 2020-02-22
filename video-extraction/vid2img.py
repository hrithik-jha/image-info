# Importing all necessary libraries 
import cv2 
import os 

try: 
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
vidcap = cv2.VideoCapture('F:\HexChat\config\scrollback\servlog\lp\lpgmfh.mp4')
count = 0
success = True
fps = int(vidcap.get(cv2.CAP_PROP_FPS))


while success:
    success,image = vidcap.read()
    if count % (2 * fps) == 0 :
         cv2.imwrite('./data/frame%d.jpg'%count,image)
         print('Saved image ', count)
    count+=1
  
# Release all space and windows once done 
vidcap.release() 
cv2.destroyAllWindows() 